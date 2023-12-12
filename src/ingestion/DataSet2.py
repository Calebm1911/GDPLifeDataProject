# DataSet2.py - script to extract data from its source and load into ADLS.
import requests
import pandas as pd
from azure.storage.filedatalake import DataLakeServiceClient


def get_service_client_sas(account_name: str, sas_token: str) -> DataLakeServiceClient:
    account_url = f"https://{account_name}.dfs.core.windows.net"
    global service_client
    # The SAS token string can be passed in as credential param or appended to the account URL
    service_client = DataLakeServiceClient(account_url, credential=sas_token)

    return service_client
#Get SAS key
account_name = "lifeexpectancystore"
with open("src\ingestion\StorageKey.config") as f:
    sas_key=f.readline()

# Construct the API URL with the indicator name directly in the URL
api_url = f"https://ghoapi.azureedge.net/api/WHOSIS_000001"
response = requests.get(api_url)


if response.status_code == 200:
    data = response.json()
    values = data.get('value', [])  # Get the 'value' list

    if values:
        # Create a DataFrame from the 'value' list
        df = pd.DataFrame(values)
    else:
        print("No data found for the indicator.")

else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

df.to_csv('data/lifeexpectancy.csv', index=False)

get_service_client_sas(account_name, sas_key)
print(service_client)


file_system_client = service_client.create_file_system(file_system="lifeexpectancy-data")    
directory_client=file_system_client.create_directory("lifeexpectancy-csv")

file_client = directory_client.create_file("lifeexpectancy.csv")
pop_file = open('./data/lifeexpectancy.csv','r')

file_contents = pop_file.read()

file_client.upload_data(file_contents, overwrite=True)