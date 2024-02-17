import osm2gmns as og
import pandas as pd
import os 
import numpy as np

str88 = 'Allegheny County,Philadelphia County,Duval County,Suffolk County,Franklin County,Wayne County,Hennepin County,Multnomah County,Davidson County,Lancaster County,Shelby County,Fulton County,Mecklenburg County,Miami-Dade County,Cook County,Denver County,King County,Cuyahoga County,Monroe County,Baltimore city,Worcester County,District of Columbia'
list88 = str88.split(',')
for i in range(len(list88)):
    net = og.getNetFromFile(r'datapath\OSMdata\\'+list88[i]+'.osm', network_types=('auto'), POI=True,default_speed=True)
    og.outputNetToCSV(net,output_folder=r'datapath\OSMdata\counties\\'+list88[i]+'')
    df = pd.read_csv(r'datapath\OSMdata\counties\\'+list88[i]+'\\poi.csv',encoding='gbk')
    str1='restaurant/fast_food/cafe/arts_centre/theatre/bar/pub/cinema'
    str2='bank/place_of_worship/fountain/food_court/shelter/college/marketplace/community_centre/library/university/bus_station/hospital/social_facility/pharmacy'
    list1 = str1.split('/')
    list2 = str2.split('/')
    df1=df[(df["amenity"]==list1[0])|(df["amenity"]==list1[1])|(df["amenity"]==list1[2])|(df["amenity"]==list1[3])|(df["amenity"]==list1[4])|(df["amenity"]==list1[5])|(df["amenity"]==list1[6])|(df["amenity"]==list1[7])]
    df2=df[(df["amenity"]==list2[0])|(df["amenity"]==list2[1])|(df["amenity"]==list2[2])|(df["amenity"]==list2[3])|(df["amenity"]==list2[4])|(df["amenity"]==list2[5])|(df["amenity"]==list2[6])|(df["amenity"]==list2[7])|(df["amenity"]==list2[8])|(df["amenity"]==list2[9])|(df["amenity"]==list2[10])|(df["amenity"]==list2[11])|(df["amenity"]==list2[12])|(df["amenity"]==list2[13])]
    df1['point'] = df1['centroid'].map(lambda x:x.split('(')[0])
    df1['zuobiao'] = df1['centroid'].map(lambda x:x.split('(')[1])
    df1['longitude'] = df1['zuobiao'].map(lambda x:x.split(' ')[0])
    df1['zuobiao2'] = df1['zuobiao'].map(lambda x:x.split(' ')[1])
    df1['latitude'] = df1['zuobiao2'].map(lambda x:x.split(')')[0])
    df1=df1[['name','poi_id','amenity','area','longitude','latitude']]
    df1=df1.iloc[:,[0,1,2,5,4,3]]
    df1.rename(columns={'poi_id':'SID'}, inplace = True)
    df1.rename(columns={'area':'SC'}, inplace = True)
    ERPE = df1.to_csv(r'datapath\OSMdata\counties\\'+list88[i]+'\\ERPE.csv', index = True)
    df2['point'] = df2['centroid'].map(lambda x:x.split('(')[0])
    df2['zuobiao'] = df2['centroid'].map(lambda x:x.split('(')[1])
    df2['longitude'] = df2['zuobiao'].map(lambda x:x.split(' ')[0])
    df2['zuobiao2'] = df2['zuobiao'].map(lambda x:x.split(' ')[1])
    df2['latitude'] = df2['zuobiao2'].map(lambda x:x.split(')')[0])
    df2=df2[['name','poi_id','amenity','area','longitude','latitude']]
    df2=df2.iloc[:,[0,1,2,5,4,3]]
    df2.rename(columns={'poi_id':'SID'}, inplace = True)
    df2.rename(columns={'area':'SC'}, inplace = True)
    NERPE = df2.to_csv(r'datapath\OSMdata\counties\\'+list88[i]+'\\NERPE.csv', index = True)

