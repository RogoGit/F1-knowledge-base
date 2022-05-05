from ergast_api_extractor import process_f1_ergast_data
from f1_technical_scrapper import get_f1_technical_data
from f1_fansite_scrapper import get_f1_fansite_data
from f1_books_extractor import get_f1_books_data


if __name__ == '__main__':
    # getting all available data from ergast developer api and saving it to required format
    process_f1_ergast_data("../f1_extracted_data/")
    # getting cars and teams open data from f1-technical.com and saving it to required format
    get_f1_technical_data("../f1_extracted_data/")
    # getting data from f1-fansite.com and saving it to required format
    get_f1_fansite_data("../f1_extracted_data/")
    # getting f1 books data from goodreads and saving it to required format
    get_f1_books_data("../f1_extracted_data/")

