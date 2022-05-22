from data_importer import fill_f1_graph
from sparql_requester import run_queries


ONTOLOGY_PATH = "../ontology.owl"
RESULT_ONTOLOGY_PATH = "../ontology-with-individuals.owl"
F1_EXTRACTED_DATA_PATH = "../f1_extracted_data"


if __name__ == '__main__':
    fill_f1_graph(ONTOLOGY_PATH, "turtle", F1_EXTRACTED_DATA_PATH, RESULT_ONTOLOGY_PATH)
    run_queries(RESULT_ONTOLOGY_PATH, "turtle")
