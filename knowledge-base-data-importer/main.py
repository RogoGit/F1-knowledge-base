from data_importer import fill_f1_graph


ONTOLOGY_PATH = "../ontology.owl"
RESULT_ONTOLOGY_PATH = ".."
F1_EXTRACTED_DATA_PATH = "../f1_extracted_data"


if __name__ == '__main__':
    fill_f1_graph(ONTOLOGY_PATH, "turtle", F1_EXTRACTED_DATA_PATH, RESULT_ONTOLOGY_PATH)
