import pymongo
import pandas as pd
# Provide the mongodb localhost url to connect python to mongodb.
client = pymongo.MongoClient("mongodb://localhost:27017/neurolabDB")

DATABASE_NAME = "aps"
COLLECTION_NAME = "sensor"


if __name__ ="__main__":
    df = pd.read_csv(filepath_or_buffer)