from data_importer import fill_f1_graph
from sparql_requester import run_queries
from void_generator import generate_void


ONTOLOGY_PATH = "../ontology.owl"
POPULATED_ONTOLOGY_PATH = "../ontology-with-individuals.owl"
F1_EXTRACTED_DATA_PATH = "../f1_extracted_data"
VOID_VOCAB_FILE = "../VoID.owl"
ONTOLOGY_FORMAT = "turtle"


if __name__ == '__main__':
    fill_f1_graph(ONTOLOGY_PATH, ONTOLOGY_FORMAT, F1_EXTRACTED_DATA_PATH, POPULATED_ONTOLOGY_PATH)
    generate_void(POPULATED_ONTOLOGY_PATH, ONTOLOGY_FORMAT, VOID_VOCAB_FILE)
    run_queries(POPULATED_ONTOLOGY_PATH, ONTOLOGY_FORMAT)
