import sys
import requests

api_key = sys.argv[1]
api_token = sys.argv[2]

def calculator(firstname, secondname):

    url = "https://" + api_key + "/getPercentage"

    querystring = {"fname": firstname,"sname": secondname}

    headers = {
        'x-rapidapi-host': api_key,
        'x-rapidapi-key': api_token
        }

    response = requests.request("GET", url, headers=headers, params=querystring)
    jsondata = response.json()
    return jsondata

if __name__ == '__main__':
    data = calculator("Adam", "Eve")
    print(data)
