"""
projekt_3.py: Třetí projekt do Engeto Online Python Akademie

author: David Šnajdr
email: d.snajdr@email.cz
discord: David Š.#7349
"""

import sys
import csv

import requests
from bs4 import BeautifulSoup

# hlavní funkce
def election_scraper(argv: str):

    url_to_scrap, file_name = check_input_arguments(argv)
    urls, partial_dict_1 = get_urls_codes_names(url_to_scrap)
    partial_dict_2 = get_votes_envelopes(urls, partial_dict_1)
    election_results_dict = get_parties_votes(urls, partial_dict_2)
    save_to_csv(file_name, election_results_dict)

# kontrola vstupních argumentů
def check_input_arguments(argv: str) -> (str, str):

    if len(argv) != 2:
        print("ŠPATNÝ VSTUP")
        sys.exit()

    url = str(argv[0])
    file_name = str(argv[1])

    if not url.startswith('https://volby.cz/pls/ps2017nss'):
        print("ŠPATNÉ URL")
        sys.exit()

    response_check = check_if_website_exists(url)
    if response_check is False:
        print("ŠPATNÉ URL")
        sys.exit()
    elif not file_name.endswith('.csv'):
        print("ŠPATNÝ TYP SOUBORU")
        sys.exit()
    else:
        print(f"STAHUJI DATA Z VYBRANÉHO URL: {url}")
        return url, file_name

# kontrola url
def check_if_website_exists(url: str) -> bool:

    response = requests.get(url)
    if response.status_code == 200:
        return True
    else:
        return False

# url, kódy, názvy obcí
def get_urls_codes_names(url: str) -> (list, list):

    election_results_partial = []
    urls = []
    root = "https://volby.cz/pls/ps2017nss/"
    parsed_html = BeautifulSoup(requests.get(url).text, features="html.parser")
    tr_tags = parsed_html.find_all('tr')

    for tr_tag in tr_tags:
        code_and_name_row = dict()
        code = tr_tag.find('td', {'class': 'cislo'})
        for number in range(1, 4):
            name = tr_tag.find('td', {'headers': f't{number}sa1 t{number}sb2'}) or tr_tag.find('td', {'headers': 's3'})
            if code and name is not None:
                code_and_name_row["code"] = code.text
                code_and_name_row["name"] = name.text
                election_results_partial.append(code_and_name_row)
                urls.append(root + code.find('a')['href'])
                break
    return urls, election_results_partial

# envelopes
def get_votes_envelopes(urls: list, election_results_partial: list) -> list:

    for index, code_and_name in enumerate(election_results_partial):
        url = urls[index]
        parsed_html = BeautifulSoup(requests.get(url).text, features="html.parser")
        code_and_name["registered"] = parsed_html.find("td", {"headers": "sa2"}).text.replace("\xa0", "")
        code_and_name["envelopes"] = parsed_html.find("td", {"headers": "sa5"}).text.replace("\xa0", "")
        code_and_name["valid"] = parsed_html.find("td", {"headers": "sa6"}).text.replace("\xa0", "")
    return election_results_partial

# přiřazení názvu stran a počtu hlasů
def get_parties_votes(urls: list, election_results: list) -> list:

    for index, row_dict in enumerate(election_results):
        url = urls[index]
        parsed_html = BeautifulSoup(requests.get(url).text, features="html.parser")
        div_tags = parsed_html.find("div", {"id": "inner"})
        tr_tags = div_tags.find_all("tr")
        for tr_tag in tr_tags:
            party_name = tr_tag.find("td", {"class": "overflow_name"})
            for number in range(1, 4):
                party_votes = tr_tag.find("td", {"headers": f"t{number}sa2 t{number}sb3"})
                if party_name is not None and party_votes is not None:
                    row_dict[party_name.text] = party_votes.text.replace("\xa0", "")
                    break
    return election_results

# uložení do souboru csv
def save_to_csv(file_name: str, election_results: list):

    with open(file_name, 'w', encoding="utf-8-sig", newline="") as elections_file:
        fieldnames = election_results[0].keys()
        writer = csv.DictWriter(elections_file, fieldnames=fieldnames, delimiter=';')
        writer.writeheader()
        writer.writerows(election_results)
        print(f"UKLÁDÁM DO SOUBORU: {file_name}",
              "UKONČUJI PROGRAM",
              sep="\n")


if __name__ == "__main__":
    election_scraper(sys.argv[1:])