import urllib.request as urllib_request
import bs4 as bs
from datetime import datetime
import json


BASE_URL = "https://www.f1-fansite.com/"
F1_START_YEAR = 1950
F1_CURRENT_YEAR = datetime.now().year


def save_json_to_file(json_data, file_path):
    data_to_write = json.dumps(json_data, indent=4)
    file = open(file_path, 'w+')
    file.write(data_to_write)
    file.close()


def get_page_html(url):
    req = urllib_request.Request(url)
    req.add_header('User-Agent',
                   'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.11 (KHTML, like Gecko) Chrome/23.0.1271.64 Safari/537.11')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8')
    req.add_header('Accept-Charset', 'ISO-8859-1,utf-8;q=0.7,*;q=0.3')
    req.add_header('Accept-Encoding', 'none')
    req.add_header('Accept-Language', 'en-US,en;q=0.8')
    req.add_header('Connection', 'keep-alive')
    page = urllib_request.urlopen(req)
    html_bytes = page.read()
    html = html_bytes.decode("utf-8")
    return html


def get_grand_prix_data():
    grand_prix_dict = {}
    grand_prixes_page_url = BASE_URL + "all-time-formula-1-grand-prix-list/"
    main_page_html = get_page_html(grand_prixes_page_url)
    soup = bs.BeautifulSoup(main_page_html, features="html.parser")
    table_rows = soup.find("table").findAll("tr")
    for i in range(1, len(table_rows)):
        grand_prix_name = table_rows[i].findAll("td")[0].find("a").string
        grand_prix_years_held = table_rows[i].findAll("td")[1].string
        grand_prix_href = table_rows[i].findAll("td")[0].find("a")["href"]
        grand_prix_id = grand_prix_name.lower().replace(" ", "_")
        grand_prix_dict[grand_prix_id] = {
            "name": grand_prix_name,
            "years_held": grand_prix_years_held,
            "f1_fansite_url": grand_prix_href
        }
        grand_prix_page_html = get_page_html(grand_prix_href)
        soup = bs.BeautifulSoup(grand_prix_page_html, features="html.parser")
        info_table_rows = soup.find("table").findAll("tr")
        grand_prix_dict[grand_prix_id]["grand_prix_no"] = info_table_rows[1].findAll("td")[1].string
        grand_prix_dict[grand_prix_id]["date"] = info_table_rows[2].findAll("td")[1].string
        grand_prix_dict[grand_prix_id]["track"] = info_table_rows[3].findAll("td")[1].find("a").string
        grand_prix_dict[grand_prix_id]["lap_distance_km"] = info_table_rows[4].findAll("td")[1].string
        grand_prix_dict[grand_prix_id]["total_laps"] = info_table_rows[5].findAll("td")[1].string
        grand_prix_dict[grand_prix_id]["distance_km"] = info_table_rows[6].findAll("td")[1].string
    return grand_prix_dict


def get_circuit_data():
    circuit_dict = {}
    circuits_page_url = BASE_URL + "f1-circuits/"
    main_page_html = get_page_html(circuits_page_url)
    soup = bs.BeautifulSoup(main_page_html, features="html.parser")
    circuits = soup.find("table").findAll("td")
    for circuit in circuits:
        try:
            circuit_name = circuit.find("a").string
            circuit_id = circuit_name.lower().replace(" ", "_")
            circuit_href = circuit.find("a")["href"]
            circuit_dict[circuit_id] = {
                "name": circuit_name,
                "f1_fansite_url": circuit_href
            }
            circuit_page_html = get_page_html(circuit_href)
            soup = bs.BeautifulSoup(circuit_page_html, features="html.parser")
            details_table = soup.find("table")
            details_table_rows = details_table.findAll("tr")
            circuit_dict[circuit_id]["used"] = details_table_rows[3].findAll("td")[1].string
            circuit_dict[circuit_id]["type"] = details_table_rows[4].findAll("td")[1].string
            circuit_dict[circuit_id]["lap_dist_km"] = details_table_rows[5].findAll("td")[1].string
            lap_record_table = soup.findAll("table")[1]
            lap_record_table_rows = lap_record_table.findAll("tr")
            circuit_dict[circuit_id]["lap_record"] = lap_record_table_rows[0].findAll("td")[1].string
            circuit_dict[circuit_id]["lap_record_date"] = lap_record_table_rows[1].findAll("td")[1].string
            circuit_dict[circuit_id]["lap_record_driver"] = lap_record_table_rows[2].findAll("td")[1].find("a").string
            circuit_dict[circuit_id]["lap_record_car"] = lap_record_table_rows[3].findAll("td")[1].string
            circuit_dict[circuit_id]["lap_record_speed"] = lap_record_table_rows[4].findAll("td")[1].string
            pole_record_table = soup.findAll("table")[2]
            pole_record_table_rows = pole_record_table.findAll("tr")
            circuit_dict[circuit_id]["pole_record"] = pole_record_table_rows[0].findAll("td")[1].string
            circuit_dict[circuit_id]["pole_record_date"] = pole_record_table_rows[1].findAll("td")[1].string
            circuit_dict[circuit_id]["pole_record_driver"] = pole_record_table_rows[2].findAll("td")[1].find("a").string
            circuit_dict[circuit_id]["pole_record_car"] = pole_record_table_rows[3].findAll("td")[1].string
            circuit_dict[circuit_id]["pole_record_speed"] = pole_record_table_rows[4].findAll("td")[1].string

        except AttributeError:
            print(f'Cannot find link for {circuit.string}')
            continue
        except IndexError:
            print(f'No pole information for {circuit.string}')
            continue

    print(circuit_dict)
    return circuit_dict


def get_f1_fansite_data(results_dir_path):
    grand_prix_dict = get_grand_prix_data()
    save_json_to_file(grand_prix_dict, results_dir_path + 'f1-fansite-grand-prix.json')
    circuit_dict = get_circuit_data()
    save_json_to_file(circuit_dict, results_dir_path + 'f1-fansite-circuit.json')

