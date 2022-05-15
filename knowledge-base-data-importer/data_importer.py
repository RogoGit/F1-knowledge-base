from rdflib import URIRef, Literal, Graph
from rdflib.namespace import RDF, XSD
import json


ONTOLOGY_IRI = "https://github.com/RogoGit/F1-knowledge-base/f1-ontology"
f1_graph = Graph()


# Classes
driver_class = URIRef(f"{ONTOLOGY_IRI}#Driver")
car_class = URIRef(f"{ONTOLOGY_IRI}#Car")
car_driving_class = URIRef(f"{ONTOLOGY_IRI}#CarDriving")
circuit_class = URIRef(f"{ONTOLOGY_IRI}#Circuit")
death_accident_class = URIRef(f"{ONTOLOGY_IRI}#DeathAccident")
grand_prix_class = URIRef(f"{ONTOLOGY_IRI}#GrandPrix")
grand_prix_result_class = URIRef(f"{ONTOLOGY_IRI}#GrandPrixResult")
race_result_class = URIRef(f"{ONTOLOGY_IRI}#RaceResult")
qualifying_result_class = URIRef(f"{ONTOLOGY_IRI}#QualifyingResult")
related_creation_class = URIRef(f"{ONTOLOGY_IRI}#RelatedCreation")
book_class = URIRef(f"{ONTOLOGY_IRI}#Book")
movie_class = URIRef(f"{ONTOLOGY_IRI}#Movie")
season_class = URIRef(f"{ONTOLOGY_IRI}#Season")
season_result_class = URIRef(f"{ONTOLOGY_IRI}#SeasonResult")
driver_standing_class = URIRef(f"{ONTOLOGY_IRI}#DriverStanding")
constructor_standing_class = URIRef(f"{ONTOLOGY_IRI}#ConstructorStanding")
team_class = URIRef(f"{ONTOLOGY_IRI}#Team")
team_participation_class = URIRef(f"{ONTOLOGY_IRI}#TeamParticipation")

# Object properties
drivingHasHappenedInSeason_op = URIRef(f"{ONTOLOGY_IRI}#drivingHasHappenedInSeason")
grandPrixResultIsRelatedTo_op = URIRef(f"{ONTOLOGY_IRI}#grandPrixResultIsRelatedTo")
hasCarDriving_op = URIRef(f"{ONTOLOGY_IRI}#hasCarDriving")
hasConstructorStandingResult_op = URIRef(f"{ONTOLOGY_IRI}#hasConstructorStandingResult")
hasDiedIn_op = URIRef(f"{ONTOLOGY_IRI}#hasDiedIn")
hasDriver_op = URIRef(f"{ONTOLOGY_IRI}#hasDriver")
hasDriverDriving_op = URIRef(f"{ONTOLOGY_IRI}#hasDriverDriving")
hasDriverGrandPrixResult_op = URIRef(f"{ONTOLOGY_IRI}#hasDriverGrandPrixResult")
hasDriverParticipation_op = URIRef(f"{ONTOLOGY_IRI}#hasDriverParticipation")
hasDriverStandingResult_op = URIRef(f"{ONTOLOGY_IRI}#hasDriverStandingResult")
hasEverBeenATeammate_op = URIRef(f"{ONTOLOGY_IRI}#hasDriver")
hasGrandPrixResult_op = URIRef(f"{ONTOLOGY_IRI}#hasGrandPrixResult")
hasResult_op = URIRef(f"{ONTOLOGY_IRI}#hasResult")
hasSeasonConstructorResult_op = URIRef(f"{ONTOLOGY_IRI}#hasSeasonConstructorResult")
hasSeasonDriverResult_op = URIRef(f"{ONTOLOGY_IRI}#hasSeasonDriverResult")
hasTeam_op = URIRef(f"{ONTOLOGY_IRI}#hasTeam")
hasTeamParticipation_op = URIRef(f"{ONTOLOGY_IRI}#hasTeamParticipation")
inEvent_op = URIRef(f"{ONTOLOGY_IRI}#inEvent")
isAbout_op = URIRef(f"{ONTOLOGY_IRI}#isAbout")
isConstructedBy_op = URIRef(f"{ONTOLOGY_IRI}#isConstructedBy")
isConstructorOf_op = URIRef(f"{ONTOLOGY_IRI}#isConstructorOf")
isHappendInSeason_op = URIRef(f"{ONTOLOGY_IRI}#isHappendInSeason")
isPartOf_op = URIRef(f"{ONTOLOGY_IRI}#isPartOf")
seasonConstructorResultIsRelatedTo_op = URIRef(f"{ONTOLOGY_IRI}#seasonConstructorResultIsRelatedTo")
seasonDriverResultIsRelatedTo_op = URIRef(f"{ONTOLOGY_IRI}#seasonDriverResultIsRelatedTo")
tookPlaceIn_op = URIRef(f"{ONTOLOGY_IRI}#tookPlaceIn")

# Data properties
wikipediaUrl_dp = URIRef(f"{ONTOLOGY_IRI}#wikipediaUrl")
# Driver (f1_ergast data)
firstName_dp = URIRef(f"{ONTOLOGY_IRI}#firstName")
birthDate_dp = URIRef(f"{ONTOLOGY_IRI}#birthDate")
driverCode_dp = URIRef(f"{ONTOLOGY_IRI}#driverCode")
lastName_dp = URIRef(f"{ONTOLOGY_IRI}#lastName")
nationality_dp = URIRef(f"{ONTOLOGY_IRI}#nationality")
permanentNumber_dp = URIRef(f"{ONTOLOGY_IRI}#permanentNumber")
# Car (f1_technical)
carDesigners_dp = URIRef(f"{ONTOLOGY_IRI}#carDesigners")
carModel_dp = URIRef(f"{ONTOLOGY_IRI}#carModel")
chassisDescription_dp = URIRef(f"{ONTOLOGY_IRI}#chassisDescription")
dimensions_dp = URIRef(f"{ONTOLOGY_IRI}#dimensions")
engineDescription_dp = URIRef(f"{ONTOLOGY_IRI}#engineDescription")
specifications_dp = URIRef(f"{ONTOLOGY_IRI}#specifications")
transmission_dp = URIRef(f"{ONTOLOGY_IRI}#transmission")
# Team (f1_technical, ergast)
foundYear_dp = URIRef(f"{ONTOLOGY_IRI}#foundYear")
teamBasedIn_dp = URIRef(f"{ONTOLOGY_IRI}#teamBasedIn")
teamCountry_dp = URIRef(f"{ONTOLOGY_IRI}#teamCountry")
teamName_dp = URIRef(f"{ONTOLOGY_IRI}#teamName")
# Death Accident (f1_fansite)
accidentDate_dp = URIRef(f"{ONTOLOGY_IRI}#accidentDate")
accidentSession_dp = URIRef(f"{ONTOLOGY_IRI}#accidentSession")
deathCause_dp = URIRef(f"{ONTOLOGY_IRI}#deathCause")
# Season (ergast)
seasonYear_dp = URIRef(f"{ONTOLOGY_IRI}#seasonYear")
# Season results (ergast)
totalPoints_dp = URIRef(f"{ONTOLOGY_IRI}#totalPoints")
totalPosition_dp = URIRef(f"{ONTOLOGY_IRI}#totalPosition")
winsNum_dp = URIRef(f"{ONTOLOGY_IRI}#winsNum")
# Related Creation
creationTitle_dp = URIRef(f"{ONTOLOGY_IRI}#creationTitle")
creationDate_dp = URIRef(f"{ONTOLOGY_IRI}#creationDate")
genre_dp = URIRef(f"{ONTOLOGY_IRI}#genre")
ratingsNum_dp = URIRef(f"{ONTOLOGY_IRI}#ratingsNum")
description_dp = URIRef(f"{ONTOLOGY_IRI}#description")
# Movie
movieDuration_dp = URIRef(f"{ONTOLOGY_IRI}#movieDuration")
imDbRating_dp = URIRef(f"{ONTOLOGY_IRI}#imDbRating")
metacriticRating_dp = URIRef(f"{ONTOLOGY_IRI}#metacriticRating")
# Book
author_dp = URIRef(f"{ONTOLOGY_IRI}#author")
pages_dp = URIRef(f"{ONTOLOGY_IRI}#pages")
reviewsNum_dp = URIRef(f"{ONTOLOGY_IRI}#reviewsNum")
goodreadsRating_dp = URIRef(f"{ONTOLOGY_IRI}#goodreadsRating")
# Grand Prix (ergast, f1 fansite)
grandPrixDate_dp = URIRef(f"{ONTOLOGY_IRI}#grandPrixDate")
grandPrixName_dp = URIRef(f"{ONTOLOGY_IRI}#grandPrixName")
seasonRound_dp = URIRef(f"{ONTOLOGY_IRI}#seasonRound")
totalLaps_dp = URIRef(f"{ONTOLOGY_IRI}#totalLaps")


def load_json_from_file(file_path):
    json_file = open(file_path, 'r')
    result = json.load(json_file)
    json_file.close()
    return result


def add_season_individual(individual_id, year, wiki_url):
    individual = URIRef(f"{ONTOLOGY_IRI}#{individual_id}")
    f1_graph.add((individual, RDF.type, season_class))
    f1_graph.add((individual, seasonYear_dp, Literal(year, datatype=XSD.integer)))
    f1_graph.add((individual, wikipediaUrl_dp, Literal(wiki_url, datatype=XSD.string)))
    return individual


def fill_f1_graph(ontology_path, data_format, f1_data_path, result_path):
    f1_graph.parse(ontology_path, format=data_format)
    seasons_data_dict = load_json_from_file(f'{f1_data_path}/ergast-seasons.json')
    for season in seasons_data_dict:
        add_season_individual(f"season_{seasons_data_dict[season]['year']}",
                              int(seasons_data_dict[season]['year']), seasons_data_dict[season]['wikipedia_page_url'])

    f1_graph.serialize(destination=f'{result_path}/ontology-with-individuals.owl', format='turtle')

