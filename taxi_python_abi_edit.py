# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

import pymysql
import pandas as pd

conn = pymysql.connect(host='192.168.15.15',
							 user='abi',
							 password='bab',
							 db='kaggle_taxi',
							)

conn.connect()

est = pd.read_sql("""select * from taxi_train
				   where vendor_id is not null limit 100""", conn)

est