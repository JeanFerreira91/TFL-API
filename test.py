import requests
import pprint

#  Variable to hold the URL
api_url = "https://api.tfl.gov.uk/journey/journeyresults/forest-hill/to/brockley"
url_append = "https://api.tfl.gov.uk"

# Function to call the API and return the JSON
def get_json(url):
    # Make the request
    response = requests.get(url)
    final_data = response.json()
    final_data = final_data['fromLocationDisambiguation']['disambiguationOptions']
    pp = pprint.PrettyPrinter()
    # pp.pprint(final_data)
    
    for trip in range(len(final_data)):
        # pp.pprint(final_data[trip])
        print(f"Area Name: {final_data[trip]['place']['commonName']}")
        print(f"Place Type: {final_data[trip]['place']['placeType']}")
        # Checking if there is a mode of transport:
        if 'modes' in final_data[trip]['place']:
            # Looping through the modes of transport:
            for mode in range(len(final_data[trip]['place']['modes'])):
                print(f"Mode of Transport: {final_data[trip]['place']['modes'][mode]}")
        print(f"Area Url: " + url_append + f"{final_data[trip]['place']['url']}")
        print(f"Journey Uri: " + url_append + f"{final_data[trip]['uri']}" + "\n")
        
    
    # Return the JSON
    return response.json()

get_json(api_url)