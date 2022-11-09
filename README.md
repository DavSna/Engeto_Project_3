# Engeto_Project_3

Třetí projekt na Python Akademii od Engeto.

## Popis projektu
Tento projekt slouží k extrahování výsledků z parlamentních voleb 2017. Odkaz k prohlédnutí [zde](https://volby.cz/pls/ps2017nss/ps3?xjazyk=CZ).

## Instalace knihoven
Knihovny použity v kódu jsou uložené v souboru `requirements.txt`. Před instalací se doporučuje použít nové virtualní prostředí a s nainstalovaným manažerem spustit nasledovně:
```
$ pip3 --version                    # overim verzi manazeru
$ pip3 install -r requirements.txt  # nainstalujeme knihovny
```

## Spuěštění projektu
Spuštění souboru `projekt_3.py` v rámci příkazového řádku požaduje dva povinné argumenty.
```
python projekt_3.py <odkaz_uzemniho_celku> <nazev_vystupniho_souboru>
```
Následně se vám stáhnou výsledky, jako soubor s příponou `.csv`.

## Ukázka projektu
Výsledky hlasování pro okres Praha - východ:

1. argument:  `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2109`
2. argument:  `praha_vychod.csv`

###### Spuštění programu:
```
python projekt_3.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2109' 'praha_vychod.csv'   
```

###### Průběh stahovaní:
```
STAHUJI DATA Z VYBRANÉHO URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=2&xnumnuts=2109
UKLÁDÁM DO SOUBORU: praha_vychod.csv
UKONČUJI PROGRAM
```

###### Částečný výstup:
```
code;name;registered;envelopes;valid;Občanská demokratická strana...
538043;Babice;732;533;531;79;0;1;17;0;56;6;5;1;20;0;0;80;0;2;48;128;0;0;24;0;12;0;0;51;1
538051;Bašť;1409;966;961;212;4;0;39;3;61;40;17;4;22;0;1;139;0;2;84;239;1;2;16;1;5;0;2;66;1
534684;Borek;242;170;170;27;1;0;11;0;15;5;1;0;2;0;1;24;0;0;15;64;1;0;0;0;2;0;0;1;02
...
```
