# Reisesøk

Et enkelt reisesøk for hele Norge, samlet på én side. Siden er laget for å slå opp busstider,
ferjetider, togavganger og innenriksfly uansett hvor i landet du er, og for å planlegge en reise
fra ett sted til et annet med alle bytter underveis.

**Åpne siden:** https://sabajan-ki.github.io/reisesok/

## Hva siden gjør

**Reise.** Du skriver inn hvor du skal fra og til, og siden finner reiser med buss, tog,
flytog, trikk, T-bane, bilferje, hurtigbåt og innenriksfly. Du ser alle bytter, gangavstander,
spor og plattform, forsinkelser i sanntid, innstilte avganger og avviksmeldinger. For flyetapper
hentes flightnummer, gate og status fra Avinor. Du kan søke etter avreisetid eller når du vil
være framme, bla til tidligere og senere reiser, og velge bort transportmidler.

**Avganger.** Avgangstavle for en holdeplass, stasjon eller ferjekai. Tavla oppdateres hvert
30. sekund, og stopp du bruker ofte kan lagres.

**Fly.** Avganger og ankomster for Avinors 43 lufthavner og Sandefjord lufthavn Torp, med
nye tider, status og gate. Tavla oppdateres hvert minutt.

## Hvor dataene kommer fra

| Kilde | Brukes til | Vilkår |
|-------|------------|--------|
| [Entur](https://developer.entur.org) – Journey Planner og Geocoder | Reisesøk, stoppsøk og avgangstavler for all kollektivtrafikk i Norge, også ferjer og innenriksfly | Åpne data under [NLOD](https://data.norge.no/nlod/no/2.0) |
| [Avinor](https://www.avinor.no) flydata, hentet via [allemannsdata.com](https://allemannsdata.com/wiki/kilder/avinor/) | Offisielle flytider, status og gate | Kilde: Avinor. Allemannsdata videreformidler dataene uten garanti for oppetid |

Sanntid vises der operatøren sender det. For Torp mangler gate i datagrunnlaget, så den må
sjekkes på [torp.no](https://torp.no/avganger-og-ankomster/). Utenlandsfly vises i flytavla,
men er ikke med i reisesøket.

## Personvern

Siden er én HTML-fil som kjører i nettleseren din. Den har ingen innlogging, ingen
sporing og ingen egen server. Siste søk og lagrede stopp ligger bare i din egen nettleser.
Bruker du «min posisjon», sendes koordinatene til Enturs adresseoppslag for å finne navnet
på stedet.

Billetter kjøpes i Entur-appen eller hos operatøren.
