import pandas as pd

temp1 = pd.read_csv(r'\OSMdata\UScounty.csv')
temp2 = pd.read_csv(r'datapath\OSMdata\cbg_geographic.csv')
temp3 = pd.read_excel(r'datapath\OSMdata\cbg_race.xlsx')
temp4 = pd.read_csv(r'datapath\OSMdata\cbg_income.csv')
temp5 = pd.read_csv(r'datapath\OSMdata\cbg_vehicle.csv')
temp6 = pd.read_csv(r'datapath\OSMdata\US_tree.txt')
temp41 = temp4[['census_block_group','B19301e1','B19301Ie1','B19301He1','B19301Be1','B19301Ce1','B19301De1']]
temp51 = temp5[['census_block_group','B25044e1','B25044e10','B25044e2','B25044e3']]
temp51['drive_prop'] = temp51.apply(lambda x:(x['B25044e1']+x['B25044e2']-x['B25044e10']-x['B25044e3'])/(x['B25044e1']+x['B25044e2']),axis=1)
temp51['walk_prop'] = temp51.apply(lambda x:(x['B25044e10']+x['B25044e3'])/(x['B25044e1']+x['B25044e2']),axis=1)
temp51 = temp51[['census_block_group','drive_prop','walk_prop']]
temp6['TCGS'] = temp6.apply(lambda x:(x['AREA']*x['MEAN'])/100,axis=1)
temp6.rename(columns={'CENSUSBLOC':'census_block_group'}, inplace = True)
temp61 = temp6[['census_block_group','TCGS']]

str6='Travis County,Bexar County,Nueces County,Harris County,Tarrant County,Dallas County,San Diego County,Santa Clara County,Sacramento County,San Joaquin County,Alameda County,San Francisco County,Stanislaus County,Orange County,Fresno County,Riverside County,Pima County,Maricopa County,Allegheny County,Philadelphia County,Duval County,Suffolk County,Franklin County,Wayne County,Hennepin County,Multnomah County,Davidson County,Lancaster County,Shelby County,Fulton County,Mecklenburg County,Miami-Dade County,Cook County,Denver County,King County,Cuyahoga County,Monroe County,Baltimore city,Worcester County,District of Columbia'
str66 = 'TX,TX,TX,TX,TX,TX,CA,CA,CA,CA,CA,CA,CA,CA,CA,CA,AZ,AZ,PA,PA,FL,MA,OH,MI,MN,OR,TN,NE,TN,GA,NC,FL,IL,CO,WA,OH,NY,MD,MA,DC'##适用于其他state
list6 = str6.split(',')
list66 = str66.split(',')

for i in range(len(list6)):
    df = pd.DataFrame()
    temp1.loc[(temp1['County']==list6[i])&(temp1['State']==list66[i]),'chuli'] = temp1['CensusBloc']
    df["census_block_group"] = temp1["chuli"]
    df.dropna(axis=0, how='any',subset=["census_block_group"],inplace=True)
    df=df.sort_values(by=['census_block_group'])
    df = df.reset_index() 
    temp1.drop(['chuli'],axis=1,inplace=True)
    df = pd.merge(df,temp2,how="left",on=["census_block_group"])
    df = pd.merge(df,temp3,how="left",on=["census_block_group"])
    df = df[['index','census_block_group','latitude','longitude','P0020001','P0020002','P0020005','P0020006','P0020007','P0020008']]
    df.rename(columns={'P0020001':'total','P0020002':'Hispanic_or_Latino','P0020005':'white','P0020006':'black','P0020007':'American_Indian','P0020008':'Asian'}, inplace = True)
    df['HoLP'] = df.apply(lambda x:x['Hispanic_or_Latino']/x['total'],axis=1)
    df['WP'] = df.apply(lambda x:x['white']/x['total'],axis=1)
    df['BP'] = df.apply(lambda x:x['black']/x['total'],axis=1)
    df['AIP'] = df.apply(lambda x:x['American_Indian']/x['total'],axis=1)
    df['AP'] = df.apply(lambda x:x['Asian']/x['total'],axis=1)
    df = pd.merge(df,temp41,how="left",on=["census_block_group"])
    df.rename(columns={'B19301e1':'API','B19301Ie1':'Hispanic_or_Latino_income','B19301He1':'white_income','B19301Be1':'black_income','B19301Ce1':'American_Indian_income','B19301De1':'Asian_income'}, inplace = True)
    df = pd.merge(df,temp51,how="left",on=["census_block_group"])
    df = pd.merge(df,temp61,how="left",on=["census_block_group"])
    tree = df[['census_block_group','TCGS']]
    tree.rename(columns={'census_block_group':'SID','TCGS':'SC'}, inplace = True)
    tree.to_csv(r'datapath\OSMdata\\'+list6[i]+'\\TCGS.csv', index = True)
    pop = df[['census_block_group','latitude','longitude','total']]
    pop.rename(columns={'census_block_group':'GID','total':'pop'}, inplace = True)
    pop.to_csv(r'datapath\OSMdata\\'+list6[i]+'\\population.csv', index = True)
    df.to_excel(r'datapath\OSMdata\\'+list6[i]+'\\'+list6[i]+'_all.xlsx', index = True)


