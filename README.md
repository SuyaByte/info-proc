# info-proc
Acquiring and Processing Information on the World's Largest Banks

## Scenario:
To create a code that can be used to compile the list of the top 10 largest banks in the world ranked by market capitalization in billion USD. Further, the data needs to be transformed and stored in GBP, EUR, and INR as well, per the exchange rate information that has been made available to you as a CSV file. The processed information table is to be saved locally in a CSV format and as a database table.

The task is to create an automated system to generate this information so that the same can be executed in every financial quarter to prepare the report.

| Parameter | Value             |
| ------ | ------------------------- |
| Data URL | [List of Largest Banks](https://web.archive.org/web/20230908091635/https://en.wikipedia.org/wiki/List_of_largest_banks) |
| Exchange rate CSV path  | [CSV](https://cf-courses-data.s3.us.cloud-object-storage.appdomain.cloud/IBMSkillsNetwork-PY0221EN-Coursera/labs/v2/exchange_rate.csv) |
| Table Attributes (upon Extraction only) | Name, MC_USD_Billion |
| Table Attributes (final) | Name, MC_USD_Billion, MC_GBP_Billion, MC_EUR_Billion, MC_INR_Billion |
| Output CSV Path | ./Largest_banks_data.csv |
| Database name | Banks.db |
| Table name | Largest_banks |
| Log file | code_log.txt |

## Set Up:
This project is done as a part of IBM Data Engineering Certification Course. It is developed and executed in a Cloud IDE. In this project, the database is created on a dummy server using SQLite3 Library.

The libraries needed for the code are:
- requests: The library is used for accessing the information from the URL.
- bs4: The library containing the BeautifulSoup function is used for webscraping.
- pandas: The library is used for processing the extracted data, storing it in required formats, and communicating with the databases.
- sqlite3: The library is required to create a database server connection.
- numpy: The library required for the mathematical rounding operations.
- datetime: The library containing the function datetime is used for extracting the timestamp for logging purposes.

## Code:
### Code for ETL operations on Country-GDP data

Importing the required libraries

def log_progress(message):

''' This function logs the mentioned message of a given stage of the code execution to a log file. The function returns nothing'''

def extract(url,table_attribs):

''' This function aims to extract the required information from the website and save it to a data frame. The function returns the data frame for further processing. '''
return df

def transform(df,csv_path):

''' This function accesses the CSV file for exchange rate information, and adds three columns to the data frame, each containing the transformed version of Market Cap column to respective currencies'''
return df

def load_to_csv(df,output_path):

''' This function saves the final data frame as a CSV file in the provided path. Function returns nothing.'''

def load_to_db(df,sql_connection,table_name):

''' This function saves the final data frame to a database table with the provided name. Function returns nothing.'''

def run_query(query_statement,sql_connection):

''' This function runs the query on the database table and prints the output on the terminal. Function returns nothing. '''
''' Here, you define the required entities and call the relevant functions in the correct order to complete the project. Note that this portion is not inside any function.'''

## Acknowledgement
[IBM - Python Project for Data Engineering](https://www.coursera.org/programs/computer-science-comps-alternatives-zphna/learn/python-project-for-data-engineering?authProvider=ttu)


