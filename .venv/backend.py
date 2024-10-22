import requests


API_KEY = "api key"

def get_data(place, forcast_days, kind):
    url = f"api call and key"
    response = requests.url(url)
    data = response.json()
    return data

if __name__ =="__main__":
    print(get_data(place="Tokyo"))
