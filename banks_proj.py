import pandas as pd 
import requests
from bs4 import BeautifulSoup
from datetime import datetime
import sqlite3

def log_progress(message):
    time_format = '%Y-%h-%d-%H-%M-%S'
    time_now = datetime.now()
    time_value = time_now.strftime(time_format)
    with open('code_log.txt', 'a') as f1:
        f1.write(time_value+' : '+message+'\n')

def extract(url, table_attribs):
    
    html_obj = requests.get(url).text
    soup_obj = BeautifulSoup(html_obj,'html.parser')
    df = pd.DataFrame(columns = table_attribs, index=[0])
    tables = soup_obj.find_all('tbody')
    rows = tables[0].find_all('tr')
    for i in rows:
        cols = i.find_all('td')
        if len(cols)!=0:
            data_dict = {'Name':cols[1].contents[2], 'MC_USD_Billion':cols[2].contents[0][:-1]}
            temp_df = pd.DataFrame(data_dict, index=[0])
            #temp_df['MC_USD_Billion'] = temp_df['MC_USD_Billion'].replace('\n','')
            df = pd.concat([df, temp_df], ignore_index = True)
    print(df)
    return df        

def transform(df, csv_path):
    df_csv = pd.read_csv(csv_path)
    #dict_csv = df_csv.set_index('Currency').to_dict()['Rate']
    eur = float(df_csv.Rate[0])
    gbp = float(df_csv.Rate[1])
    inr = float(df_csv.Rate[2])
    df['Temp']=df['MC_USD_Billion'].replace(',','',regex=True)
    df['Temp']=df['Temp'].astype(float)
    df['MC_GBP_Billion'] = round(df['Temp'] * gbp,2)
    df['MC_EUR_Billion'] = round(df['Temp'] * eur,2)
    df['MC_INR_Billion'] = round(df['Temp'] * inr,2)
    df = df.drop('Temp', axis = 1)
    return df

def load_to_csv(df, output_path):
    df.to_csv(output_path)

def load_to_db(df, sql_connection, table_name):
    df.to_sql(table_name, sql_connection, if_exists = 'replace', index=False)

def run_query(query_statement, sql_connection):
    print(query_statement)
    data = pd.read_sql(query_statement, sql_connection)
    print(data)

#variables
url_link = 'https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks'
attributes = ['Name', 'MC_USD_Billion']
given_csv_file_path = '/home/project/exchange_rate.csv'
op_csv_path = '/home/project/Largest_banks_data.csv'
table = 'Largest_banks'
db_name = 'Banks.db'
sql_conn = sqlite3.connect(db_name)
query = f"SELECT * FROM {table}"
#body
log_progress('start etl process')
log_progress('start extraction phase')
extracted_data = extract(url_link, attributes)
log_progress('end extraction phase')
log_progress('start transformation phase')
transformed_data = transform(extracted_data, given_csv_file_path)
log_progress('end transformation phase')
log_progress('start csv load phase')
load_to_csv(transformed_data, op_csv_path)
log_progress('end csv load phase')
log_progress('start db load phase')
load_to_db(transformed_data, sql_conn, table)
log_progress('end db load phase')
log_progress('start querying phase')
run_query(query, sql_conn)
log_progress('end querying phase')
sql_conn.close()
log_progress('end etl process')



