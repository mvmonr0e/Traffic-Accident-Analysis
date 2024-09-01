import requests
import pandas as pd
from datetime import datetime

# fetch data from houston transtar
def get_data():
    url = "https://traffic.houstontranstar.org/api/incidents_sample.json"

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        incidents_data = data['result']['incidents']
        return incidents_data
    else:
        print(f"Failed to retrieve data. Status code: {response.status_code}")
        return "error"

# clean & preprocess data
def preprocess_data(df):
    
    # convert date strings to dateime objs
    df['date'] = pd.to_datetime(datetime.now()) # all dates in the sample data are "today"
    
    # convert latitude and longitude to float
    print(df['lat'])
    df['lat'] = df['lat'].astype(float)
    df['lng'] = df['lng'].astype(float)

    # remove cleared incidents
    #df = df[df['status'] != 'cleared']

    # reset index after filtering
    df = df.reset_index(drop=True)

    return df

if __name__ == "__main__":
    data = get_data()
    if data == 'error':
        exit()
    #print(data)

    # convert json data to data frame
    df = pd.DataFrame(data)
    #print(df)

    df = preprocess_data(df)
    #print(df)