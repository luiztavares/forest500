import twint

import pandas as pd

financial = pd.read_excel('../input/forest500.xlsx',sheet_name='financial')
flag = False
for index,row in financial.iterrows():
    if(pd.isna(row['Handles'])):
        continue
    handles = row['Handles'].split(',')
    for handle in handles:
        print(handle)
        if(handle == 'Santander_Ar'):
            flag = True
        if(not flag):
            continue

        # Configure
        c = twint.Config()
        c.Username = handle
        #c.Custom["tweet"] = ["created_at","id", "username"]
        c.Output = f"old_tweets/{handle}.json"
        c.Hide_output = True
        #c.Store_csv = True
        c.Store_json = True
        #c.Elasticsearch = "http://34.95.230.124:9200"


        twint.run.Search(c)