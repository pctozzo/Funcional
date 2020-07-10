import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

df=pd.read_csv('2018_Yellow_Taxi_Trip_Data.csv');

df_2_less_pass = df[df.passenger_count<=2]

print(df_2_less_pass['trip_distance'].mean())

df['tpep_pickup_datetime']=pd.to_datetime(df['tpep_pickup_datetime'])
df['week_day'] = df['tpep_pickup_datetime'].dt.day_name()

df_saturday_monday = df[df['week_day'].isin('SATURDAY','MONDAY')]

df_saturday_monday['tpep_dropoff_datetime']=pd.to_datetime(df_saturday_monday['tpep_dropoff_datetime'])
df_saturday_monday['trip_time'] = df_saturday_monday['tpep_dropoff_datetime'] - df_saturday_monday['tpep_pickup_datetime']

print(df_saturday_monday['trip_time'].mean())

