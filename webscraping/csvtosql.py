# -*- coding: utf-8 -*-
"""
Created on Wed Nov 10 14:37:25 2021

@author: moni
"""

import pandas as pd
import pyodbc
import logging
logger = logging.getLogger(__name__)  


logger.setLevel(logging.WARNING)

file_handler = logging.FileHandler('logfile.log')
formatter    = logging.Formatter('%(asctime)s : %(levelname)s : %(name)s : %(message)s')
file_handler.setFormatter(formatter)

# add file handler to logger
logger.addHandler(file_handler)
logger.debug('This is a debug message')
logger.info('This is an info message')
logger.warning('This is a warning message')
logger.error('This is an error message')
logger.critical('This is a critical message')

def csvtosql():
    data = pd.read_csv (r'out.csv')   
    df = pd.DataFrame(data)
    conn = pyodbc.connect('Driver={SQL Server};''Server=LAPTOP-B68C5LBV\SQLEXPRESS;''Database=WEB_SCRAP;''Trusted_Connection=yes;')
    cursor = conn.cursor()

    for row in df.itertuples():
        cursor.execute('''INSERT INTO products (Product, Price, Stock_Availability) VALUES (?,?,?)''', row.Prodname,row.price,row.stock )
    logger.info('Values Inserted into the table')
    conn.commit()
    
csvtosql()