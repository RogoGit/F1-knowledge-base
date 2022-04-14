import urllib.request as urllib_request
import urllib.parse as urllib_parse
from datetime import datetime
import os
import json


BASE_URL = "https://ergast.com/api/f1/"


def build_ergast_data_request_url(data_type, data_format, year, limit, offset):
    data_url = BASE_URL
    if year is not None:
        data_url += f'{year}/'
    if data_type is not None:
        data_url += f'{data_type}'
        if data_format is not None:
            data_url += f'.{data_format.lower()}'
    if limit is not None or offset is not None:
        data_url += '?'
        url_params = urllib_parse.urlencode(
            {param_name: param_value for param_name, param_value in (('limit', limit), ('offset', offset))
             if param_value is not None})
        data_url += url_params
    return data_url


def get_ergast_json_data_by_request(data_url):
    data_response = urllib_request.urlopen(data_url)
    data = json.load(data_response)
    return data


def save_json_to_file(json_data, file_path):
    data_to_write = json.dumps(json_data, indent=4)
    file = open(file_path, 'w+')
    file.write(data_to_write)
    file.close()


def parse_ergast_driver_data(json_driver_data):
    ergast_drivers_array = json_driver_data['MRData']['DriverTable']['Drivers']
    final_drivers_array = []
    print(ergast_drivers_array)
    for ergast_driver in ergast_drivers_array:
        driver = {
            'name': ergast_driver['givenName'],
            'surname': ergast_driver['familyName'],
            'birth_date': datetime.strptime(ergast_driver['dateOfBirth'], '%Y-%m-%d').date().strftime('%d.%m.%Y'),
            'nationality': ergast_driver['nationality'],
            'permanent_number': ergast_driver['permanentNumber'] if 'permanentNumber' in ergast_driver else ' ',
            'driver_code': ergast_driver['code'] if 'code' in ergast_driver else ' ',
            'wikipedia_page_url': ergast_driver['url'],
            'ergast_driver_id': ergast_driver['driverId']
        }
        final_drivers_array.append(driver)
    return final_drivers_array


# process f1 data from ergast api
# arg - dir with output files
def process_f1_ergast_data(results_dir_path):
    if not os.path.exists(results_dir_path):
        os.makedirs(results_dir_path)

    drivers_url = build_ergast_data_request_url("drivers", "json", None, 1000, None)
    drivers_ergast_data = get_ergast_json_data_by_request(drivers_url)
    drivers_data = parse_ergast_driver_data(drivers_ergast_data)
    save_json_to_file(drivers_data, results_dir_path + 'ergast-drivers.json')

