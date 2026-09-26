"""Henter avgangstavla fra torp.no (i dag og i morgen) og skriver torp.json med gate per fly.

Avinor-dataene mangler gate for Torp. Denne fila fyller hullet og hentes av index.html.
Bare standardbiblioteket, så jobben trenger ingen installasjon.
"""
import datetime as dt
import html
import json
import re
import sys
import urllib.request
from zoneinfo import ZoneInfo

URL = "https://torp.no/wp-admin/admin-ajax.php?action=get_timetables&lang=no&showArrivals=false&dato={}"
UA = "Mozilla/5.0 (reisesok; +https://sabajan-ki.github.io/reisesok/)"
TZ = ZoneInfo("Europe/Oslo")


def cell(row, cls):
    m = re.search(r"<td class='%s[^']*'[^>]*>(.*?)</td>" % cls, row, re.S)
    return html.unescape(re.sub(r"<[^>]+>", " ", m.group(1))).strip() if m else ""


def fetch(day_param, date):
    req = urllib.request.Request(URL.format(day_param), headers={"User-Agent": UA})
    data = json.load(urllib.request.urlopen(req, timeout=30))
    out = []
    for row in re.findall(r"<tr class='[^']*'>(.*?)</tr>", data.get("html", ""), re.S):
        flight = cell(row, "flightcode")
        if not flight:
            continue
        gate = cell(row, "gate").replace("\xa0", "").strip()
        out.append({
            "date": date.isoformat(),
            "time": cell(row, "time"),
            "flight": flight.replace(" ", ""),
            "to": cell(row, "location"),
            "status": cell(row, "status"),
            "gate": gate or None,
        })
    return out


def main():
    today = dt.datetime.now(TZ).date()
    flights = fetch("today", today) + fetch("tomorrow", today + dt.timedelta(days=1))
    if not flights:
        print("Fant ingen avganger – lar forrige fil stå", file=sys.stderr)
        sys.exit(1)
    json.dump({"updated": dt.datetime.now(TZ).isoformat(timespec="seconds"),
               "source": "torp.no", "departures": flights},
              open("torp.json", "w"), ensure_ascii=False, indent=1)
    print(f"{len(flights)} avganger, {sum(1 for f in flights if f['gate'])} med gate")


if __name__ == "__main__":
    main()
