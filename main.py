import requests

# fetch data from houston transtar
def get_data():
    url = "https://traffic.houstontranstar.org/api/incidents_sample.json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        return data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return "error"


if __name__ == "__main__":
    data = get_data()
    if data == 'error':
        exit()
    
    # print(data)
