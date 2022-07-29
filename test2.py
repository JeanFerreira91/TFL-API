import requests
import pprint
import config

# Variable to hold the code of the station (check codes here: https://en.wikipedia.org/wiki/List_of_London_railway_stations):
trainStation = "FOH" # Forest Hill Station in South London
# Variable to hold the URL
api_url = "https://transportapi.com/v3/uk/train/station/" + trainStation + "/timetable.json?app_id=" + config.appId + "&app_key=" + config.appKey + "&train_status=passenger"

def get_json(url):
    # Make the request:
    response = requests.get(url)
    data = response.json()
    # Using pprinter to style the output when checking the data for the first time (not used in the final code):
    pp = pprint.PrettyPrinter()
    # Variable to count the number of trips in the timetable (for loop):
    counter = 1
    # Looping through the data:
    for service in range(len(data['departures']['all'][0:5])):
        # Getting all the relevant data:
        print(f"Service: {counter}")
        print(f"Train to: " + data['departures']['all'][service]['destination_name'])
        print(f"Train arrival time: " + data['departures']['all'][service]['aimed_arrival_time'])
        print(f"Train departure time: " + data['departures']['all'][service]['aimed_departure_time'])
        print(f"Mode of transportation: " + data['departures']['all'][service]['mode'])
        print(f"Train operator name: " + data['departures']['all'][service]['operator_name'])
        print(f"Train origin station: " + data['departures']['all'][service]['origin_name'])
        print(f"Platform number: " + data['departures']['all'][service]['platform'])
        print(f"Service number: " + data['departures']['all'][service]['service'])
        print(f"Service timetable: " + data['departures']['all'][service]['service_timetable']['id'])
        print(f"Train uid: " + data['departures']['all'][service]['train_uid'] + "\n")
        counter += 1
        

get_json(api_url)