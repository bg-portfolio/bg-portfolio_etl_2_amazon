import pandas as pd
import numpy as np
import streamlit as st
from pymongo import MongoClient
from pymongo.errors import ConnectionFailure
from time import sleep


@st.cache(allow_output_mutation=True)
def _connect_mongo():
    """
    Connect to mongodb, returns collection
    """
    client = MongoClient("mongodb://root:root@mongodb:27017")
    sleep(5)
    try:  # test the connection
        client.admin.command('ping')
    except ConnectionFailure:
        print("Server not available")
        return None
    db = client["amazon"]
    collection = db["webscrape"]
    return collection


def load_dataframe(collection):
    """
    Loads data into streamlit, returns df and dfs' columns
    """
    try:
        cursor = collection.find()
        df = pd.DataFrame(list(cursor))
        del df['_id']
        columns = list(df.columns)
        columns.append(None)
    except Exception as e:
        print(e)
    return df, columns


def transform_none_to_zero(df):
    df['rating_out_of_5'] = np.where(
        df['rating_out_of_5'] == "None", 0, df['rating_out_of_5'])
