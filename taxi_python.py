# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 16:49:09 2017

@author: Hungy
"""
import pymysql
import pandas as pd

conn = pymysql.connect(host='localhost',
							 user='hungy',
							 password='1234qwer',
							 db='kaggle_taxi',
							 charset='utf8mb4',
							 cursorclass=pymysql.cursors.DictCursor)

conn.connect()

test = pd.read_sql("""select * from taxi_train
				   where vendor_id is not null limit 100""", conn)