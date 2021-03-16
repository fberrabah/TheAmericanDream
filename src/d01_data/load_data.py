import csv
import pandas as pd
import sys


sys.path.insert(0, "/home/apprenant/Desktop/AmericanDream/")

from src.d00_utils.mysql_utils import mysql_connect, save_to_mysql

data = pd.read_csv('/home/apprenant/Desktop/AmericanDream/Data/01_raw/DataAnalyst.csv')
data2 = pd.read_excel('/home/apprenant/Desktop/AmericanDream/Data/01_raw/2020_Data_Professional_Salary_Survey_Responses.xlsx', skiprows=3)
connect = mysql_connect()
    
# Save the table in mysql database
save_to_mysql(db_connect=connect,df_to_save=data,df_name='Analyst')
save_to_mysql(db_connect=connect,df_to_save=data2,df_name='Salary')

    