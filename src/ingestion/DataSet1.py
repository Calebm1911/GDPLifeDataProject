# DataSet1.py - script to extract data from its source and load into ADLS.
from kaggle.api.kaggle_api_extended import KaggleApi
import pandas as pd
from azure.storage.filedatalake import DataLakeServiceClient

def get_service_client_sas(account_name: str, sas_token: str) -> DataLakeServiceClient:
    account_url = f"https://{account_name}.dfs.core.windows.net"
    global service_client
    # The SAS token string can be passed in as credential param or appended to the account URL
    service_client = DataLakeServiceClient(account_url, credential=sas_token)

    return service_client

account_name = "lifeexpectancystore"
with open("src\ingestion\StorageKey.config") as f:
    sas_key=f.readline()
print("Got Key")
api = KaggleApi()
api.authenticate()

dataset = 'zgrcemta/world-gdpgdp-gdp-per-capita-and-annual-growths'

api.dataset_download_file(dataset,'gdp_per_capita.csv','data/')

get_service_client_sas(account_name, sas_key)
print(service_client)

file_system_client = service_client.create_file_system(file_system="gdp-data")    
directory_client=file_system_client.create_directory("gdp-csv")

file_client = directory_client.create_file("gdp_per_capita.csv")
pop_file = open('./data/gdp_per_capita.csv','r')

file_contents = pop_file.read()

file_client.upload_data(file_contents, overwrite=True)

