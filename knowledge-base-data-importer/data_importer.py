from rdflib import URIRef, Literal, Graph
from rdflib.namespace import RDF, XSD
import json
import datetime
import re


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
drivingHasHappenedInSeason_op = URIRef(f"{ONTOLOGY_IRI}#drivingHasHappenedInSeason")    #
grandPrixResultIsRelatedTo_op = URIRef(f"{ONTOLOGY_IRI}#grandPrixResultIsRelatedTo")
hasCarDriving_op = URIRef(f"{ONTOLOGY_IRI}#hasCarDriving")  #
hasConstructorStandingResult_op = URIRef(f"{ONTOLOGY_IRI}#hasConstructorStandingResult")    #
hasDiedIn_op = URIRef(f"{ONTOLOGY_IRI}#hasDiedIn")
hasDriver_op = URIRef(f"{ONTOLOGY_IRI}#hasDriver")  #
hasDriverDriving_op = URIRef(f"{ONTOLOGY_IRI}#hasDriverDriving")    #
hasDriverGrandPrixResult_op = URIRef(f"{ONTOLOGY_IRI}#hasDriverGrandPrixResult")
hasDriverParticipation_op = URIRef(f"{ONTOLOGY_IRI}#hasDriverParticipation")    #
hasDriverStandingResult_op = URIRef(f"{ONTOLOGY_IRI}#hasDriverStandingResult")
hasEverBeenATeammate_op = URIRef(f"{ONTOLOGY_IRI}#hasDriver")
hasGrandPrixResult_op = URIRef(f"{ONTOLOGY_IRI}#hasGrandPrixResult")
hasResult_op = URIRef(f"{ONTOLOGY_IRI}#hasResult")  #
hasSeasonConstructorResult_op = URIRef(f"{ONTOLOGY_IRI}#hasSeasonConstructorResult")
hasSeasonDriverResult_op = URIRef(f"{ONTOLOGY_IRI}#hasSeasonDriverResult")  #
hasTeam_op = URIRef(f"{ONTOLOGY_IRI}#hasTeam")  #
hasTeamParticipation_op = URIRef(f"{ONTOLOGY_IRI}#hasTeamParticipation")    #
inEvent_op = URIRef(f"{ONTOLOGY_IRI}#inEvent")
isAbout_op = URIRef(f"{ONTOLOGY_IRI}#isAbout")
isConstructedBy_op = URIRef(f"{ONTOLOGY_IRI}#isConstructedBy")  #
isConstructorOf_op = URIRef(f"{ONTOLOGY_IRI}#isConstructorOf")  #
isHappendInSeason_op = URIRef(f"{ONTOLOGY_IRI}#isHappendInSeason")  #
isPartOf_op = URIRef(f"{ONTOLOGY_IRI}#isPartOf")
seasonConstructorResultIsRelatedTo_op = URIRef(f"{ONTOLOGY_IRI}#seasonConstructorResultIsRelatedTo")    #
seasonDriverResultIsRelatedTo_op = URIRef(f"{ONTOLOGY_IRI}#seasonDriverResultIsRelatedTo")  #
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
distance_dp = URIRef(f"{ONTOLOGY_IRI}#distance")
# Circuit (ergast, f1 fansite)
circuitName_dp = URIRef(f"{ONTOLOGY_IRI}#circuitName")
circuitCountry_dp = URIRef(f"{ONTOLOGY_IRI}#circuitCountry")
circuitLocality_dp = URIRef(f"{ONTOLOGY_IRI}#circuitLocality")
circuitLocationLat_dp = URIRef(f"{ONTOLOGY_IRI}#circuitLocationLat")
circuitLocationLong_dp = URIRef(f"{ONTOLOGY_IRI}#circuitLocationLong")
circuitType_dp = URIRef(f"{ONTOLOGY_IRI}#circuitType")
lapDistance_dp = URIRef(f"{ONTOLOGY_IRI}#lapDistance")


def load_json_from_file(file_path):
    json_file = open(file_path, 'r')
    result = json.load(json_file)
    json_file.close()
    return result


def add_driver_individual(individual_id, driver_data):
    individual = URIRef(f"{ONTOLOGY_IRI}#{individual_id}")
    f1_graph.add((individual, RDF.type, driver_class))
    if driver_data["name"] and driver_data["name"].strip():
        f1_graph.add((individual, firstName_dp, Literal(driver_data["name"], datatype=XSD.string)))
    if driver_data["surname"] and driver_data["surname"].strip():
        f1_graph.add((individual, lastName_dp, Literal(driver_data["surname"], datatype=XSD.string)))
    if driver_data["birth_date"] and driver_data["birth_date"].strip():
        f1_graph.add((individual, birthDate_dp,
                      Literal(datetime.datetime.strptime(driver_data["birth_date"], "%d.%m.%Y").strftime("%Y-%m-%d"),
                              datatype=XSD.date)))
    if driver_data["nationality"] and driver_data["nationality"].strip():
        f1_graph.add((individual, nationality_dp, Literal(driver_data["nationality"], datatype=XSD.string)))
    if driver_data["permanent_number"] and driver_data["permanent_number"].strip():
        f1_graph.add((individual, permanentNumber_dp, Literal(driver_data["permanent_number"], datatype=XSD.nonNegativeInteger)))
    if driver_data["driver_code"] and driver_data["driver_code"].strip():
        f1_graph.add((individual, driverCode_dp, Literal(driver_data["driver_code"], datatype=XSD.string)))
    if driver_data["wikipedia_page_url"] and driver_data["wikipedia_page_url"].strip():
        f1_graph.add((individual, wikipediaUrl_dp, Literal(driver_data["wikipedia_page_url"], datatype=XSD.string)))
    return individual


def add_team_individual(individual_id, team_data_ergast, team_data_technical):
    individual = URIRef(f"{ONTOLOGY_IRI}#{individual_id}")
    f1_graph.add((individual, RDF.type, team_class))
    if "name" in team_data_ergast and team_data_ergast["name"].strip():
        f1_graph.add((individual, teamName_dp, Literal(team_data_ergast["name"], datatype=XSD.string)))
    if "wikipedia_page_url" in team_data_ergast and team_data_ergast["wikipedia_page_url"].strip():
        f1_graph.add((individual, wikipediaUrl_dp, Literal(team_data_ergast["wikipedia_page_url"], datatype=XSD.string)))
    if "nationality" in team_data_ergast and team_data_ergast["nationality"].strip():
        f1_graph.add((individual, teamCountry_dp, Literal(team_data_ergast["nationality"], datatype=XSD.string)))
    if team_data_technical is not None and "founded" in team_data_technical and team_data_technical["founded"].strip():
        f1_graph.add((individual, foundYear_dp, Literal(team_data_technical["founded"], datatype=XSD.string)))
    if team_data_technical is not None and "based_in" in team_data_technical and team_data_technical["based_in"].strip():
        f1_graph.add((individual, teamBasedIn_dp, Literal(team_data_technical["based_in"], datatype=XSD.string)))
    return individual


def add_car_individual(individual_id, car_data, teams_data):
    individual = URIRef(f"{ONTOLOGY_IRI}#{individual_id}")
    f1_graph.add((individual, RDF.type, car_class))
    if car_data["model"] and car_data["model"].strip():
        f1_graph.add((individual, carModel_dp, Literal(car_data["model"], datatype=XSD.string)))
    if "designer" in car_data and car_data["designer"].strip():
        f1_graph.add((individual, carDesigners_dp, Literal(car_data["designer"], datatype=XSD.string)))
    if "chassis" in car_data and car_data["chassis"].strip():
        f1_graph.add((individual, chassisDescription_dp, Literal(car_data["chassis"], datatype=XSD.string)))
    if "dimensions" in car_data and car_data["dimensions"].strip():
        f1_graph.add((individual, dimensions_dp, Literal(car_data["dimensions"], datatype=XSD.string)))
    if "engine" in car_data and car_data["engine"].strip():
        f1_graph.add((individual, engineDescription_dp, Literal(car_data["engine"], datatype=XSD.string)))
    if "specifications" in car_data and car_data["specifications"].strip():
        f1_graph.add((individual, specifications_dp, Literal(car_data["specifications"], datatype=XSD.string)))
    if "transmission" in car_data and car_data["transmission"].strip():
        f1_graph.add((individual, transmission_dp, Literal(car_data["transmission"], datatype=XSD.string)))

    # finding constructor
    constructor_team_matching = next(iter([key for key, value in teams_data.items()
                                           if key.lower() in car_data["team"].replace(' ', '_').lower()]), None)

    if constructor_team_matching is not None:
        team = URIRef(f"{ONTOLOGY_IRI}#team_{teams_data[constructor_team_matching]['name'].replace(' ', '_').lower()}")
        f1_graph.add((individual, isConstructedBy_op, team))
        f1_graph.add((team, isConstructorOf_op, individual))

    return individual


def add_season_individual(individual_id, year, wiki_url):
    individual = URIRef(f"{ONTOLOGY_IRI}#{individual_id}")
    f1_graph.add((individual, RDF.type, season_class))
    f1_graph.add((individual, seasonYear_dp, Literal(year, datatype=XSD.integer)))
    f1_graph.add((individual, wikipediaUrl_dp, Literal(wiki_url, datatype=XSD.string)))
    return individual


def add_team_participation_individual(individual_id, year, participation_data):
    driver_name = participation_data["driver"].replace(" ", "_").replace(";", "")\
        .replace("(has_contract)", "").replace("(confirmed)", "").lower()
    individual = URIRef(f"{ONTOLOGY_IRI}#{individual_id}")
    f1_graph.add((individual, RDF.type, team_participation_class))
    f1_graph.add((individual, isHappendInSeason_op, URIRef(f"{ONTOLOGY_IRI}#season_{year}")))
    f1_graph.add((individual, hasDriver_op, URIRef(f'{ONTOLOGY_IRI}#driver_{driver_name}')))
    f1_graph.add((individual, hasTeam_op,
                  URIRef(f"{ONTOLOGY_IRI}#team_{participation_data['team'].replace(' ', '_').lower()}")))
    f1_graph.add((URIRef(f'{ONTOLOGY_IRI}#driver_{driver_name}'), hasDriverParticipation_op, individual))
    f1_graph.add((URIRef(f"{ONTOLOGY_IRI}#team_{participation_data['team'].replace(' ', '_').lower()}"),
                  hasTeamParticipation_op, individual))
    return individual


def add_car_driving_individual(individual_id, year, car_data, driver_name):
    individual = URIRef(f"{ONTOLOGY_IRI}#{individual_id}")
    f1_graph.add((individual, RDF.type, car_driving_class))
    f1_graph.add((individual, drivingHasHappenedInSeason_op, URIRef(f"{ONTOLOGY_IRI}#season_{year}")))
    car = URIRef(f"{ONTOLOGY_IRI}#car_{car_data['model'].replace(' ', '_').replace('(', '').replace(')', '').lower()}")
    driver = URIRef(f"{ONTOLOGY_IRI}#driver_{driver_name}")
    f1_graph.add((car, hasCarDriving_op, individual))
    f1_graph.add((driver, hasDriverDriving_op, individual))
    return individual


def add_driver_standing_individual(individual_id, year, season_result, driver_data):
    individual = URIRef(f"{ONTOLOGY_IRI}#{individual_id}")
    f1_graph.add((individual, RDF.type, driver_standing_class))
    f1_graph.add((individual, totalPoints_dp,  Literal(season_result["points"], datatype=XSD.nonNegativeInteger)))
    f1_graph.add((individual, totalPosition_dp, Literal(season_result["position"], datatype=XSD.positiveInteger)))
    f1_graph.add((individual, winsNum_dp,  Literal(season_result["wins"], datatype=XSD.nonNegativeInteger)))
    f1_graph.add((URIRef(f"{ONTOLOGY_IRI}#season_{year}"), hasResult_op, individual))
    driver = URIRef(f"{ONTOLOGY_IRI}#driver_{driver_data['name'].replace(' ', '_').lower()}"
                    f"_{driver_data['surname'].replace(' ', '_').lower()}")
    f1_graph.add((individual, seasonDriverResultIsRelatedTo_op, driver))
    f1_graph.add((driver, hasSeasonDriverResult_op, individual))
    return individual


def add_constructor_standing_individual(individual_id, year, season_result, constructor_data):
    individual = URIRef(f"{ONTOLOGY_IRI}#{individual_id}")
    f1_graph.add((individual, RDF.type, constructor_standing_class))
    f1_graph.add((individual, totalPoints_dp,  Literal(season_result["points"], datatype=XSD.nonNegativeInteger)))
    f1_graph.add((individual, totalPosition_dp, Literal(season_result["position"], datatype=XSD.positiveInteger)))
    f1_graph.add((individual, winsNum_dp,  Literal(season_result["wins"], datatype=XSD.nonNegativeInteger)))
    f1_graph.add((URIRef(f"{ONTOLOGY_IRI}#season_{year}"), hasResult_op, individual))
    constructor = URIRef(f"{ONTOLOGY_IRI}#team_{constructor_data['name'].replace(' ', '_').lower()}")
    f1_graph.add((individual, seasonConstructorResultIsRelatedTo_op, constructor))
    f1_graph.add((constructor, hasConstructorStandingResult_op, individual))
    return individual


def add_circuit_individual(individual_id, circuit_data_ergast, circuit_data_fansite):
    individual = URIRef(f"{ONTOLOGY_IRI}#{individual_id}")
    f1_graph.add((individual, RDF.type, circuit_class))
    f1_graph.add((individual, circuitName_dp, Literal(circuit_data_ergast["name"], datatype=XSD.string)))
    f1_graph.add((individual, circuitCountry_dp, Literal(circuit_data_ergast["country"], datatype=XSD.string)))
    f1_graph.add((individual, circuitLocality_dp, Literal(circuit_data_ergast["locality"], datatype=XSD.string)))
    f1_graph.add((individual, wikipediaUrl_dp, Literal(circuit_data_ergast["wikipedia_page_url"], datatype=XSD.string)))
    f1_graph.add((individual, circuitLocationLat_dp, Literal(circuit_data_ergast["latitude"], datatype=XSD.double)))
    f1_graph.add((individual, circuitLocationLong_dp, Literal(circuit_data_ergast["longitude"], datatype=XSD.double)))
    if circuit_data_fansite is not None:
        f1_graph.add((individual, circuitType_dp, Literal(circuit_data_fansite["type"], datatype=XSD.string)))
        f1_graph.add((individual, lapDistance_dp, Literal(circuit_data_fansite["lap_dist_km"], datatype=XSD.string)))
    return individual


def fill_f1_graph(ontology_path, data_format, f1_data_path, result_path):
    f1_graph.parse(ontology_path, format=data_format)

    drivers_data_dict = load_json_from_file(f'{f1_data_path}/ergast-drivers.json')
    for driver in drivers_data_dict:
        add_driver_individual(f"driver_{drivers_data_dict[driver]['name'].replace(' ', '_').lower()}_"
                              f"{drivers_data_dict[driver]['surname'].replace(' ', '_').lower()}",
                              drivers_data_dict[driver])

    teams_data_dict_ergast = load_json_from_file(f'{f1_data_path}/ergast-constructors.json')
    teams_data_dict_technical = load_json_from_file(f'{f1_data_path}/f1-technical-teams.json')
    for team in teams_data_dict_ergast:
        f1_technical_match_team = next(iter([key for key, value in teams_data_dict_technical.items()
                                   if teams_data_dict_ergast[team]["name"].replace(' ', '_').lower() in key.lower()]), None)

        if f1_technical_match_team is not None:
            team_key = teams_data_dict_technical[f1_technical_match_team]
        else:
            team_key = None

        add_team_individual(f"team_{teams_data_dict_ergast[team]['name'].replace(' ', '_').lower()}",
                            teams_data_dict_ergast[team], team_key)

    cars_data_dict = load_json_from_file(f'{f1_data_path}/f1-technical-cars.json')
    for car in cars_data_dict:
        add_car_individual(f"car_{cars_data_dict[car]['model'].replace(' ', '_').replace('(', '').replace(')', '').lower()}",
                           cars_data_dict[car], teams_data_dict_ergast)

    seasons_data_dict = load_json_from_file(f'{f1_data_path}/ergast-seasons.json')
    for season in seasons_data_dict:
        add_season_individual(f"season_{seasons_data_dict[season]['year']}",
                              int(seasons_data_dict[season]['year']), seasons_data_dict[season]['wikipedia_page_url'])

    team_participation_data_dict = load_json_from_file(f'{f1_data_path}/f1-fansite-team-participations.json')
    for season in team_participation_data_dict:
        season_participations = team_participation_data_dict[season]
        for participation in season_participations:
            if int(season) <= 2013:
                add_team_participation_individual(f"team_participation_{season}_{participation['driver'].replace(' ', '_').replace('(has_contract)', '').replace('(confirmed)', '').lower()}"
                                                  f"_{participation['team'].replace(' ', '_').lower()}", season, participation)
            else:
                add_team_participation_individual(
                    f"team_participation_{season}_{participation['drivers'][0]['driver'].replace(' ', '_').replace('(has_contract)', '').replace('(confirmed)', '').lower()}"
                    f"_{participation['team'].replace(' ', '_').lower()}", season,
                    {"driver": participation['drivers'][0]['driver'], "team": participation['team']})
                add_team_participation_individual(
                    f"team_participation_{season}_{participation['drivers'][1]['driver'].replace(' ', '_').replace('(has_contract)', '').replace('(confirmed)', '').lower()}"
                    f"_{participation['team'].replace(' ', '_').lower()}", season,
                    {"driver": participation['drivers'][1]['driver'], "team": participation['team']})

    # car driving
    for car in cars_data_dict:
        if "years" in cars_data_dict[car]:
            for year in cars_data_dict[car]["years"]:
                if "drivers" in cars_data_dict[car]:
                    for driver in re.split('[,/]', re.sub(r'\([^)]*\)', '', cars_data_dict[car]["drivers"])):
                        driver_name = re.sub(r'\([^)]*\)', '', driver).strip().lower().replace(' ', '_')
                        add_car_driving_individual(f"car_driving_{year}_{driver_name}_"
                                                   f"{cars_data_dict[car]['model'].replace(' ', '_').replace('(', '').replace(')', '').lower()}",
                                                   year, cars_data_dict[car], driver_name)

    driver_standings_data_dict = load_json_from_file(f'{f1_data_path}/ergast-driver-standings.json')
    for season_year in driver_standings_data_dict:
        for standing in driver_standings_data_dict[season_year]:
            year = season_year.split("_")[0]
            driver = drivers_data_dict[standing["ergast_driver_id"]]
            add_driver_standing_individual(f"driver_standing_{year}_{driver['name'].replace(' ', '_').lower()}"
                                           f"_{driver['surname'].replace(' ', '_').lower()}", year, standing, driver)

    constructor_standings_data_dict = load_json_from_file(f'{f1_data_path}/ergast-constructor-standings.json')
    for season_year in constructor_standings_data_dict:
        for standing in constructor_standings_data_dict[season_year]:
            year = season_year.split("_")[0]
            team = teams_data_dict_ergast[standing["ergast_constructor_id"]]
            add_constructor_standing_individual(f"constructor_standing_{year}_{team['name'].replace(' ', '_').lower()}",
                                                year, standing, team)

    circuits_data_dict_ergast = load_json_from_file(f'{f1_data_path}/ergast-circuits.json')
    circuits_data_dict_fansite = load_json_from_file(f'{f1_data_path}/f1-fansite-circuit.json')
    for circuit in circuits_data_dict_ergast:
        fansite_matching_circuit = next(iter([key for key, value in circuits_data_dict_fansite.items() if circuit in key]), None)
        if fansite_matching_circuit is not None:
            fansite_data = circuits_data_dict_fansite[fansite_matching_circuit]
        else:
            fansite_data = None
        add_circuit_individual(f"circuit_{circuits_data_dict_ergast[circuit]['name'].replace(' ', '_').lower()}",
                               circuits_data_dict_ergast[circuit], fansite_data)

    death_accidents_data_dict = load_json_from_file(f'{f1_data_path}/f1-fansite-deaths.json')

    f1_graph.serialize(destination=f'{result_path}/ontology-with-individuals.owl', format='turtle')

