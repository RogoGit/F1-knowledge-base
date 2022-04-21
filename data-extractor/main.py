from ergast_api_extractor import process_f1_ergast_data
from f1_technical_scrapper import get_f1_technical_data

if __name__ == '__main__':
    # getting all available data from ergast developer api and saving it to required format
    process_f1_ergast_data("../f1_extracted_data/")
    # getting cars and teams open data from f1-technical.com and saving it to required format
    get_f1_technical_data("../f1_extracted_data/")
