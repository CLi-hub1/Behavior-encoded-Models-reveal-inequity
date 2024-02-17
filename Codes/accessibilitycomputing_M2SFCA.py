import pandas as pd
import math
import numpy as np
import os

## The following codes compute PCE accessibility in the walking scenario, with a similar approach to accessibility in the driving scenario.
 
def func1(name):
    def walkresults(name1):
        df = pd.read_csv(r'path\\'+name1+'_FA_walk.csv', usecols = ['origin_id','destination_id','total_cost'])
        df.columns = ['GID','SID','cost']
        index = df[df["cost"] > 0.0208333 ].index
        df.drop(index, axis = 0, inplace=True)
        df.to_csv(r'path\\'+name1+'_FAdel__walk.csv', index=False)
        demand_data = pd.read_csv(r'datapath\OSMdata\\'+name1+'\population.csv',  usecols = ['GID','pop'],low_memory = False)
        demand_df = pd.DataFrame(demand_data)
        demand_df[['GID']]=demand_df[['GID']]
        demand_df[['pop']]=demand_df[['pop']]
        demand_df.to_csv(r'datapath\OSMdata\\'+name1+'\POIDUIYING.csv', index=False)
        pri_data = pd.read_csv(r'datapath\OSMdata\\'+name1+'\TCGS.csv', usecols = ['SID','SC'],low_memory = False)
        pri_df = pd.DataFrame(pri_data)
        pri_df[['SID']]=pri_df[['SID']]
        pri_df[['SC']]=pri_df[['SC']].astype(float)
        cost_data = pd.read_csv(r'path\\'+name1+'_FAdel__walk.csv', low_memory = False)
        cost_df = pd.DataFrame(cost_data)
        cost_df = cost_df[['SID','GID','cost']]
        cost_df[['GID']]=cost_df[['GID']]
        cost_df[['SID']]=cost_df[['SID']]
        cost_df[['cost']]=cost_df[['cost']].astype(float)
        temp1 = pd.merge(cost_df, demand_df, how='left', on = 'GID')
        temp1[['pop']]= temp1[['pop']].astype(float)
        temp1.drop(temp1.loc[temp1['pop']==0].index, inplace = True)
        temp1['mint']=temp1['cost']*1440 
        temp1['w1']= temp1.apply(lambda x: math.exp(-(np.square(x['mint'])/250)) if x['mint'] >0 else 1, axis=1) 
        temp1['pop2'] = temp1['w1']*temp1['pop']
        temp2 = temp1.groupby(['SID'])['pop2'].sum()
        temp2 = temp2.to_frame()
        temp2['SID']= temp2.index
        temp2 = temp2.reset_index(drop = True)
        temp2 = temp2.rename(columns={'pop2':'vj'})
        temp3 = pd.merge(temp1, temp2, how='left', on = 'SID')
        temp4 = pd.merge(temp3, pri_df, how='left', on = 'SID')
        temp4['R']= temp4.apply(lambda x: x['w1']*x['SC']/x['vj'] if x['vj'] != 0 else 0, axis=1)
        temp4['R']= temp4.apply(lambda x: x['w1']*x['w1']*x['SC']/x['vj'] if x['vj'] != 0 else 0, axis=1)
        MFCA = temp4.groupby(['GID'])['R'].sum()
        MFCA = MFCA.to_frame()
        MFCA['GID']= MFCA.index
        MFCA = MFCA.reset_index(drop = True)
        MFCA = MFCA.rename(columns={'R':'TCGS'})
        MFCA = MFCA.iloc[:,[1,0]]
        MFCA.to_csv(r'path\results\\'+name1+'_walkFA_Results.csv',index= None)
    walkresults(name)
    
    def walkresults2(name1):
        df = pd.read_csv(r'path\\'+name1+'_LA_walk.csv', usecols = ['origin_id','destination_id','total_cost'])
        df.columns = ['GID','SID','cost']
        index = df[df["cost"] > 0.0208333 ].index
        df.drop(index, axis = 0, inplace=True)
        df.to_csv(r'path\\'+name1+'_LAdel__walk.csv', index=False)
        demand_data = pd.read_csv(r'datapath\OSMdata\\'+name1+'\population.csv',  usecols = ['GID','pop'],low_memory = False)
        demand_df = pd.DataFrame(demand_data)
        demand_df[['GID']]=demand_df[['GID']]
        demand_df[['pop']]=demand_df[['pop']]
        pri_data =  pd.read_csv(r'datapath\OSMdata\\'+name1+'\ERPE.csv', usecols = ['SID','SC'],low_memory = False)
        pri_df = pd.DataFrame(pri_data)
        pri_df[['SID']]=pri_df[['SID']]
        pri_df[['SC']]=pri_df[['SC']].astype(float)
        cost_data = pd.read_csv(r'path\\'+name1+'_LAdel__walk.csv', low_memory = False)
        cost_df = pd.DataFrame(cost_data)
        cost_df = cost_df[['SID','GID','cost']]
        cost_df[['GID']]=cost_df[['GID']]
        cost_df[['SID']]=cost_df[['SID']]
        cost_df[['cost']]=cost_df[['cost']].astype(float)
        temp1 = pd.merge(cost_df, demand_df, how='left', on = 'GID')
        temp1[['pop']]= temp1[['pop']].astype(float)
        temp1.drop(temp1.loc[temp1['pop']==0].index, inplace = True)
        temp1['mint']=temp1['cost']*1440 
        temp1['w1']= temp1.apply(lambda x: math.exp(-(np.square(x['mint'])/250)) if x['mint'] >0 else 1, axis=1)
        temp1['pop2'] = temp1['w1']*temp1['pop']
        temp2 = temp1.groupby(['SID'])['pop2'].sum()
        temp2 = temp2.to_frame()
        temp2['SID']= temp2.index
        temp2 = temp2.reset_index(drop = True)
        temp2 = temp2.rename(columns={'pop2':'vj'})
        temp3 = pd.merge(temp1, temp2, how='left', on = 'SID')
        temp4 = pd.merge(temp3, pri_df, how='left', on = 'SID')
        temp4['R']= temp4.apply(lambda x: x['w1']*x['SC']/x['vj'] if x['vj'] != 0 else 0, axis=1)
        temp4['R']= temp4.apply(lambda x: x['w1']*x['w1']*x['SC']/x['vj'] if x['vj'] != 0 else 0, axis=1)
        MFCA = temp4.groupby(['GID'])['R'].sum()
        MFCA = MFCA.to_frame()
        MFCA['GID']= MFCA.index
        MFCA = MFCA.reset_index(drop = True)
        MFCA = MFCA.rename(columns={'R':'ERPE'})
        MFCA = MFCA.iloc[:,[1,0]]
        MFCA.to_csv(r'path\results\\'+name1+'_walkLA_Results.csv',index= None)
    walkresults2(name)

    def walkresults3(name1):
        df = pd.read_csv(r'path\\'+name1+'_HA_walk.csv', usecols = ['origin_id','destination_id','total_cost'])
        df.columns = ['GID','SID','cost']
        index = df[df["cost"] > 0.0208333 ].index
        df.drop(index, axis = 0, inplace=True)
        df.to_csv(r'path\\'+name1+'_HAdel__walk.csv', index=False)
        demand_data = pd.read_csv(r'datapath\OSMdata\\'+name1+'\population.csv',  usecols = ['GID','pop'],low_memory = False)
        demand_df = pd.DataFrame(demand_data)
        demand_df[['GID']]=demand_df[['GID']]
        demand_df[['pop']]=demand_df[['pop']]
        pri_data = pd.read_csv(r'datapath\OSMdata\\'+name1+'\\NERPE.csv', usecols = ['SID','SC'],low_memory = False)
        pri_df = pd.DataFrame(pri_data)
        pri_df[['SID']]=pri_df[['SID']]
        pri_df[['SC']]=pri_df[['SC']].astype(float)
        cost_data = pd.read_csv(r'path\\'+name1+'_HAdel__walk.csv', low_memory = False)
        cost_df = pd.DataFrame(cost_data)
        cost_df = cost_df[['SID','GID','cost']]
        cost_df[['GID']]=cost_df[['GID']]
        cost_df[['SID']]=cost_df[['SID']]
        cost_df[['cost']]=cost_df[['cost']].astype(float)
        temp1 = pd.merge(cost_df, demand_df, how='left', on = 'GID')
        temp1[['pop']]= temp1[['pop']].astype(float)
        temp1.drop(temp1.loc[temp1['pop']==0].index, inplace = True) 
        temp1['mint']=temp1['cost']*1440  
        temp1['w1']= temp1.apply(lambda x: math.exp(-(np.square(x['mint'])/250)) if x['mint'] >0 else 1, axis=1) 
        temp1['pop2'] = temp1['w1']*temp1['pop']
        temp2 = temp1.groupby(['SID'])['pop2'].sum()
        temp2 = temp2.to_frame()
        temp2['SID']= temp2.index
        temp2 = temp2.reset_index(drop = True)
        temp2 = temp2.rename(columns={'pop2':'vj'})
        temp3 = pd.merge(temp1, temp2, how='left', on = 'SID')
        temp4 = pd.merge(temp3, pri_df, how='left', on = 'SID')
        temp4['R']= temp4.apply(lambda x: x['w1']*x['SC']/x['vj'] if x['vj'] != 0 else 0, axis=1)
        temp4['R']= temp4.apply(lambda x: x['w1']*x['w1']*x['SC']/x['vj'] if x['vj'] != 0 else 0, axis=1)
        MFCA = temp4.groupby(['GID'])['R'].sum()
        MFCA = MFCA.to_frame()
        MFCA['GID']= MFCA.index
        MFCA = MFCA.reset_index(drop = True)
        MFCA = MFCA.rename(columns={'R':'NERPE'})
        MFCA = MFCA.iloc[:,[1,0]]
        MFCA.to_csv(r'path\results\\'+name1+'_walkHA_Results.csv',index= None)
    walkresults3(name)
    a = pd.read_csv(r'datapath\OSMdata\\'+name+'\POIDUIYING.csv')
    b = pd.read_csv(r'path\results\\'+name+'_walkFA_Results.csv')
    c = pd.read_csv(r'path\results\\'+name+'_walkLA_Results.csv')
    d = pd.read_csv(r'path\results\\'+name+'_walkHA_Results.csv')
    access = pd.merge(a,b,how="left",on=["GID"])
    access = pd.merge(access,c,how="left",on=["GID"])
    access = pd.merge(access,d,how="left",on=["GID"])
    access.to_csv(r'path\results\\'+name+'_walkResults.csv')
    os.remove(r'path\results\\'+name+'_walkFA_Results.csv')
    os.remove(r'path\results\\'+name+'_walkLA_Results.csv')
    os.remove(r'path\results\\'+name+'_walkHA_Results.csv')

str55='Travis County,Bexar County,Nueces County,Harris County,Tarrant County,Dallas County,San Diego County,Santa Clara County,Sacramento County,San Joaquin County,Alameda County,San Francisco County,Stanislaus County,Orange County,Fresno County,Riverside County,Pima County,Maricopa County,Allegheny County,Philadelphia County,Duval County,Suffolk County,Franklin County,Wayne County,Hennepin County,Multnomah County,Davidson County,Lancaster County,Shelby County,Fulton County,Mecklenburg County,Miami-Dade County,Cook County,Denver County,King County,Cuyahoga County,Monroe County,Baltimore city,Worcester County,District of Columbia'
list55 = str55.split(',')
for i in range(len(list55)):
    func1(list55[i])
 
 
