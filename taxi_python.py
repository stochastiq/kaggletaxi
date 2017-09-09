# -*- coding: utf-8 -*-
"""
Created on Sat Sep  9 16:49:09 2017

@author: Hungy
"""
import pymysql
import pandas as pd

conn = pymysql.connect(host='192.168.15.15',
							 user='abi',
							 password='bab',
							 db='kaggle_taxi',
							)

conn.connect()

test = pd.read_sql("""select * from taxi_train
				   where vendor_id is not null limit 100""", conn)