import pandas as pd
from recombee_api_client.api_client import RecombeeClient, Region
from recombee_api_client.api_requests import SetItemValues, Batch
from recombee_api_client.exceptions import APIException
import os
from dotenv import load_dotenv
from pathlib import Path

load_dotenv(Path(__file__).with_name(".env"))

DB_NAME = os.environ["RECOMBEE_DATABASE_ID"]
PRIVATE_TOKEN = os.environ["RECOMBEE_PRIVATE_TOKEN"]
REGION = 'eu-west'

client = RecombeeClient(DB_NAME, PRIVATE_TOKEN, region = Region.EU_WEST)

PATH_DATASET = 'perfumes.csv'

def send_items():
    """Functie care citeste dataset-ul si trimite item-urile in Recombee"""
    df = pd.read_csv(PATH_DATASET)
    print(f"Se trimit {len(df)} item-uri in Recombee...")
    
    requests = []
    
    for index, row in df.iterrows():
        item_id = str(row['id'])
        
        properties = {
            "brand": str(row['brand']),
            "perfume": str(row['perfume']),
            "type": str(row['type']),
            "category": str(row['category']),
            "target_audience": str(row['target_audience']),
            "longevity": str(row['longevity'])
        }
        
        requests.append(SetItemValues(item_id, properties, cascade_create=True))
        
        # Trimitem in loturi (batch) de cate 100 pentru eficienta
        if len(requests) == 100:
            client.send(Batch(requests))
            requests = []
            print("S-a trimis un lot de 100 item-uri...")
            
    if requests:
        client.send(Batch(requests))
        print("S-a trimis ultimul lot de item-uri.")
        
    print("Toate item-urile au fost trimise cu succes!")

if __name__ == "__main__":
    send_items()
