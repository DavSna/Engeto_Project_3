# ENGETO_Project_3
Engeto 3rd project - elections scraper.

## Popis projektu
Projekt scrapuje data [vysledku voleb](https://volby.cz/pls/ps2017nss/ps?xjazyk=CZ) Poslanecké sněmovny Parlamentu České republiky konané ve dnech 20.10. – 21.10.2017

## Instalace knihoven
Knihovny pouzity v kodu jsou ulozene v souboru `requirements.txt`. Pred instalaci se doporucuje pouzit nove virtualni prostredi a s nainstalovanym manazerem spustit nasledovne:
```
$ pip3 --version                    # over verzi manazeru
$ pip3 install -r requirements.txt  # nainstaluj knihovny
```

## Spusteni projektu
Spust soubor `ENGETO_PROJECT_3.py` v prikazovem radku pouzitim 2 povinnych argumentu:
```
python ENGETO_PROJECT_3.py <odkaz_uzemniho_celku> <nazev_vystupniho_souboru>
```
Data budou stazeny do souboru s priponou `.csv`.

## Ukazka projektu
Vysledky hlasovani pro kraj Hlavní město Praha:

1. argument:  `https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100`
2. argument:  `praha_mesto.csv`

###### Spusteni programu:
```
python ENGETO_Project_3.py 'https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100' 'Praha-mesto.csv'   
```

###### Prubeh stahovani:
```
STAHUJI DATA Z VYBRANEHO URL: https://volby.cz/pls/ps2017nss/ps32?xjazyk=CZ&xkraj=1&xnumnuts=1100
UKLADAM DO SOUBORU: Praha-mesto.csv
UKONCUJI PROGRAM
```

###### Castecny vystup:
```
code;name;registered;envelopes;valid;Občanská demokratická strana;Řád národa - Vlastenecká unie;CESTA ODPOVĚDNÉ SPOLEČNOSTI;Česká str.sociálně demokrat.;Volte Pr.Blok www.cibulka.net;Radostné Česko;STAROSTOVÉ A NEZÁVISLÍ;Komunistická str.Čech a Moravy;Strana zelených;ROZUMNÍ-stop migraci,diktát.EU;Společ.proti výst.v Prok.údolí;Strana svobodných občanů;Blok proti islam.-Obran.domova;Občanská demokratická aliance;Česká pirátská strana;OBČANÉ 2011-SPRAVEDL. PRO LIDI;Unie H.A.V.E.L.;Referendum o Evropské unii;TOP 09;ANO 2011;Dobrá volba 2016;SPR-Republ.str.Čsl. M.Sládka;Křesť.demokr.unie-Čs.str.lid.;Česká strana národně sociální;REALISTÉ;SPORTOVCI;Dělnic.str.sociální spravedl.;Svob.a př.dem.-T.Okamura (SPD);Strana Práv Občanů
500054;Praha 1;21556;14145;14036;2770;9;13;657;12;1;774;392;514;41;6;241;14;44;2332;5;0;12;2783;1654;1;7;954;3;133;11;2;617;34
500224;Praha 10;79964;52238;51895;8137;40;34;3175;50;17;2334;2485;1212;230;15;1050;35;67;9355;9;8;30;6497;10856;37;53;2398;12;477;69;53;2998;162
...
```
