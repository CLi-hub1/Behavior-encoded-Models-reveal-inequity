import pandas as pd
import math
import numpy as np
import matplotlib.pyplot as plt
import os
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

str55='Travis County,Bexar County,Nueces County,Harris County,Tarrant County,Dallas County,San Diego County,Santa Clara County,Sacramento County,San Joaquin County,Alameda County,San Francisco County,Stanislaus County,Orange County,Fresno County,Riverside County,Pima County,Maricopa County,Allegheny County,Philadelphia County,Duval County,Suffolk County,Franklin County,Wayne County,Hennepin County,Multnomah County,Davidson County,Lancaster County,Shelby County,Fulton County,Mecklenburg County,Miami-Dade County,Cook County,Denver County,King County,Cuyahoga County,Monroe County,Baltimore city,Worcester County,District of Columbia'
list55 = str55.split(',')
  
for i in range(len(list55)):
    drivemode = pd.DataFrame()
    walkmode = pd.DataFrame()
    all_data = pd.DataFrame()
    zonghe = pd.DataFrame()
    drivemode = pd.read_csv(r' path\python\output\results\\'+list55[i]+'_driveResults.csv')
    walkmode = pd.read_csv(r' path\python\output\results\\'+list55[i]+'_walkResults.csv')
    all_data = pd.read_excel(r' path\data\OSMdata\\'+list55[i]+'\\'+list55[i]+'_all.xlsx')
    all_data.rename(columns={'TCGS':'tree_cover_area'}, inplace = True)
    zonghe[['census_block_group']] = all_data[['census_block_group']]
    zonghe['TCGS'] = drivemode['TCGS']*all_data['drive_prop']+walkmode['TCGS']*all_data['walk_prop']
    zonghe['ERPE'] = drivemode['ERPE']*all_data['drive_prop']+walkmode['ERPE']*all_data['walk_prop']
    zonghe['NERPE'] = drivemode['NERPE']*all_data['drive_prop']+walkmode['NERPE']*all_data['walk_prop']
    zonghe = pd.merge(all_data,zonghe,how="left",on=["census_block_group"])
    zonghe.to_excel(r' path\data\OSMdata\\'+list55[i]+'\\AA_zongheresults.xlsx')

for i in range(len(list55)):
    yiyou = pd.DataFrame()
    e = pd.DataFrame()
    AGG = pd.DataFrame()
    yiyou = pd.read_csv(r' path\python\output\results\\'+list55[i]+'_driveResults.csv')
    yiyou.rename(columns={'GID':'census_block_group'}, inplace = True)
    e = pd.read_excel(r' path\data\OSMdata\\'+list55[i]+'\\'+list55[i]+'_all.xlsx')
    e.rename(columns={'TCGS':'tree_cover_area'}, inplace = True)
    AGG = pd.merge(e,yiyou,how="left",on=["census_block_group"])
    AGG.to_excel(r' path\data\OSMdata\\'+list55[i]+'\\'+list55[i]+'_alldrive.xlsx')

for i in range(len(list55)):
    f = pd.DataFrame()
    g = pd.DataFrame()
    g1 = pd.DataFrame()
    f = pd.read_excel(r' path\data\OSMdata\\'+list55[i]+'\\AA_zongheresults.xlsx')
    g = f[['index','census_block_group','latitude','longitude','Hispanic_or_Latino','white','black','American_Indian','Asian','TCGS','ERPE','NERPE']]
    g21 = ((g['Hispanic_or_Latino']*g['TCGS']).sum())/(g['Hispanic_or_Latino'].sum())
    g22 = ((g['white']*g['TCGS']).sum())/(g['white'].sum())
    g23 = ((g['black']*g['TCGS']).sum())/(g['black'].sum())
    g24 = ((g['American_Indian']*g['TCGS']).sum())/(g['American_Indian'].sum())
    g25 = ((g['Asian']*g['TCGS']).sum())/(g['Asian'].sum())
    g31 = ((g['Hispanic_or_Latino']*g['ERPE']).sum())/(g['Hispanic_or_Latino'].sum())
    g32 = ((g['white']*g['ERPE']).sum())/(g['white'].sum())
    g33 = ((g['black']*g['ERPE']).sum())/(g['black'].sum())
    g34 = ((g['American_Indian']*g['ERPE']).sum())/(g['American_Indian'].sum())
    g35 = ((g['Asian']*g['ERPE']).sum())/(g['Asian'].sum())
    g41 = ((g['Hispanic_or_Latino']*g['NERPE']).sum())/(g['Hispanic_or_Latino'].sum())
    g42 = ((g['white']*g['NERPE']).sum())/(g['white'].sum())
    g43 = ((g['black']*g['NERPE']).sum())/(g['black'].sum())
    g44 = ((g['American_Indian']*g['ERPE']).sum())/(g['American_Indian'].sum())
    g45 = ((g['Asian']*g['NERPE']).sum())/(g['Asian'].sum())
    g1 = pd.DataFrame([[g21,g22,g23,g24,g25], [g31,g32,g33,g34,g35], [g41,g42,g43,g44,g45]], columns=['Hispanic_or_Latino','white','black','American_Indian','Asian'])
    g1.index = ['PW_TCGS', 'PW_ERPE', 'PW_NERPE']
    h = pd.DataFrame()
    h1 = pd.DataFrame()
    h1 = f[['index','census_block_group','latitude','longitude','Hispanic_or_Latino','white','black','American_Indian','Asian','HoLP','WP','BP','AIP','AP','TCGS','ERPE','NERPE']]
    h11 = h1[['HoLP','WP','BP','AIP','AP']]
    h111 = h11.loc[:,:].mean()
    h1111 = h111.reset_index()
    h1111 = h1111['index']
    for z in range(len(h111)):
       h2 = h1[(h1[h1111[z]]>=float(h111[z]))]
       h21 = h2[['TCGS']].mean()
       h211 = h2[['TCGS']].std()/((h2[['TCGS']].count())**0.5)*1.96
       h22 = h2[['ERPE']].mean()
       h221 = h2[['ERPE']].std()/((h2[['ERPE']].count())**0.5)*1.96
       h23 = h2[['NERPE']].mean()
       h231 = h2[['NERPE']].std()/((h2[['NERPE']].count())**0.5)*1.96
       h[str(z)] = [float(h21),float(h22),float(h23),float(h211),float(h221),float(h231)]
    h.index = ['M_TCGS', 'M_ERPE', 'M_NERPE','CI_TCGS', 'CI_ERPE', 'CI_NERPE']
    h.columns = ['Hispanic_or_Latino','white','black','American_Indian','Asian']
    j = pd.DataFrame()
    j_1 = pd.DataFrame()
    j_2 = pd.DataFrame()
    j1 = f[['index','census_block_group','latitude','longitude','total','Hispanic_or_Latino','white','black','American_Indian','Asian','API','Hispanic_or_Latino_income','white_income','black_income','American_Indian_income','Asian_income','TCGS','ERPE','NERPE']]
    j11 = j1[['API','Hispanic_or_Latino_income','white_income','black_income','American_Indian_income','Asian_income']]
    j111 = j11.loc[:,:].quantile(0.3)
    j112 = j11.loc[:,:].quantile(0.7)
    j113 = ['API','Hispanic_or_Latino_income','white_income','black_income','American_Indian_income','Asian_income']
    j114 = ['total','Hispanic_or_Latino','white','black','American_Indian','Asian']
    for x in range(len(j111)):
        j2 = j1[(j1[j113[x]]<=float(j111[x]))]
        j21 = ((j2[j114[x]]*j2['TCGS']).sum())/(j2[j114[x]].sum())
        j22 = ((j2[j114[x]]*j2['ERPE']).sum())/(j2[j114[x]].sum())
        j23 = ((j2[j114[x]]*j2['NERPE']).sum())/(j2[j114[x]].sum())
        j_1[str(x)] = [float(j21),float(j22),float(j23)]
    for y in range(len(j112)):
        j3 = j1[(j1[j113[x]]>=float(j112[y]))]
        j31 = ((j3[j114[x]]*j3['TCGS']).sum())/(j3[[j114[x]]].sum())
        j32 = ((j3[j114[x]]*j3['ERPE']).sum())/(j3[[j114[x]]].sum())
        j33 = ((j3[j114[x]]*j3['NERPE']).sum())/(j3[[j114[x]]].sum())
        j_2[str(y)] = [float(j31),float(j32),float(j33)]
    j_3 = j_2.div(j_1, axis = 0)
    j = j_1.append(j_2, ignore_index=True)
    j = j.append(j_3, ignore_index=True)
    j.index = ['poor_TCGS', 'poor_ERPE', 'poor_NERPE','rich_TCGS', 'rich_ERPE', 'rich_NERPE','gap_TCGS', 'gap_ERPE', 'gap_NERPE']
    j.columns = ['total','Hispanic_or_Latino','white','black','American_Indian','Asian']
    writer = pd.ExcelWriter(r' path\data\OSMdata\\'+list55[i]+'\\AA_results.xlsx')
    g1.to_excel(writer,sheet_name='POP_WEIGHT')
    h.to_excel(writer,sheet_name='MEAN',encoding="utf-8")
    j.to_excel(writer,sheet_name='GAP')
    writer.save()

for i in range(len(list55)):
    f = pd.DataFrame()
    f = pd.read_excel(r' path\data\OSMdata\\'+list55[i]+'\\AA_zongheresults.xlsx')
    j = pd.DataFrame()
    j_1 = pd.DataFrame()
    j_2 = pd.DataFrame()
    j_3 = pd.DataFrame()
    j_4 = pd.DataFrame()
    j_5 = pd.DataFrame()
    j_6 = pd.DataFrame()
    j_7 = pd.DataFrame()
    j_8 = pd.DataFrame()
    j_9 = pd.DataFrame()
    j_10 = pd.DataFrame()
    j1 = f[['index','census_block_group','latitude','longitude','total','Hispanic_or_Latino','white','black','American_Indian','Asian','API','Hispanic_or_Latino_income','white_income','black_income','American_Indian_income','Asian_income','TCGS','ERPE','NERPE']]
    j11 = j1[['API','Hispanic_or_Latino_income','white_income','black_income','American_Indian_income','Asian_income']]
    j111 = j11.iloc[:,:].quantile(0.1)
    j112 = j11.iloc[:,:].quantile(0.2)
    j113 = j11.iloc[:,:].quantile(0.3)
    j114 = j11.iloc[:,:].quantile(0.4)
    j115 = j11.iloc[:,:].quantile(0.5)
    j116 = j11.iloc[:,:].quantile(0.6)
    j117 = j11.iloc[:,:].quantile(0.7)
    j118 = j11.iloc[:,:].quantile(0.8)
    j119 = j11.iloc[:,:].quantile(0.9)
    j120 = j11.iloc[:,:].max()
    j_88 = pd.concat([j111,j112,j113,j114,j115,j116,j117,j118,j119,j120], axis=1, ignore_index=True)
    j888 = j_88.reset_index()
    j8888 = j888['index']
    j88888 = ['total','Hispanic_or_Latino','white','black','American_Indian','Asian']
    for x in range(len(j8888)):
      j2 = j1[(j1[j8888[x]]<=float(j_88.iloc[x,0]))]
      j21 = ((j2[j88888[x]]*j2['TCGS']).sum())/(j2[j88888[x]].sum())
      j22 = ((j2[j88888[x]]*j2['ERPE']).sum())/(j2[j88888[x]].sum())
      j23 = ((j2[j88888[x]]*j2['NERPE']).sum())/(j2[j88888[x]].sum())
      j_1[str(x)] = [float(j21),float(j22),float(j23)]
      j2 = pd.DataFrame()
      j2 = j1[(j1[j8888[x]]>float(j_88.iloc[x,0]))&(j1[j8888[x]]<=float(j_88.iloc[x,1]))]
      j21 = ((j2[j88888[x]]*j2['TCGS']).sum())/(j2[j88888[x]].sum())
      j22 = ((j2[j88888[x]]*j2['ERPE']).sum())/(j2[j88888[x]].sum())
      j23 = ((j2[j88888[x]]*j2['NERPE']).sum())/(j2[j88888[x]].sum())
      j_2[str(x)] = [float(j21),float(j22),float(j23)]
      j2 = pd.DataFrame()
      j2 = j1[(j1[j8888[x]]>float(j_88.iloc[x,1]))&(j1[j8888[x]]<=float(j_88.iloc[x,2]))]
      j21 = ((j2[j88888[x]]*j2['TCGS']).sum())/(j2[j88888[x]].sum())
      j22 = ((j2[j88888[x]]*j2['ERPE']).sum())/(j2[j88888[x]].sum())
      j23 = ((j2[j88888[x]]*j2['NERPE']).sum())/(j2[j88888[x]].sum())
      j_3[str(x)] = [float(j21),float(j22),float(j23)]
      j2 = pd.DataFrame()
      j2 = j1[(j1[j8888[x]]>float(j_88.iloc[x,2]))&(j1[j8888[x]]<=float(j_88.iloc[x,3]))]
      j21 = ((j2[j88888[x]]*j2['TCGS']).sum())/(j2[j88888[x]].sum())
      j22 = ((j2[j88888[x]]*j2['ERPE']).sum())/(j2[j88888[x]].sum())
      j23 = ((j2[j88888[x]]*j2['NERPE']).sum())/(j2[j88888[x]].sum())
      j_4[str(x)] = [float(j21),float(j22),float(j23)]
      j2 = pd.DataFrame()
      j2 = j1[(j1[j8888[x]]>float(j_88.iloc[x,3]))&(j1[j8888[x]]<=float(j_88.iloc[x,4]))]
      j21 = ((j2[j88888[x]]*j2['TCGS']).sum())/(j2[j88888[x]].sum())
      j22 = ((j2[j88888[x]]*j2['ERPE']).sum())/(j2[j88888[x]].sum())
      j23 = ((j2[j88888[x]]*j2['NERPE']).sum())/(j2[j88888[x]].sum())
      j_5[str(x)] = [float(j21),float(j22),float(j23)]
      j2 = pd.DataFrame()
      j2 = j1[(j1[j8888[x]]>float(j_88.iloc[x,4]))&(j1[j8888[x]]<=float(j_88.iloc[x,5]))]
      j21 = ((j2[j88888[x]]*j2['TCGS']).sum())/(j2[j88888[x]].sum())
      j22 = ((j2[j88888[x]]*j2['ERPE']).sum())/(j2[j88888[x]].sum())
      j23 = ((j2[j88888[x]]*j2['NERPE']).sum())/(j2[j88888[x]].sum())
      j_6[str(x)] = [float(j21),float(j22),float(j23)]
      j2 = pd.DataFrame()
      j2 = j1[(j1[j8888[x]]>float(j_88.iloc[x,5]))&(j1[j8888[x]]<=float(j_88.iloc[x,6]))]
      j21 = ((j2[j88888[x]]*j2['TCGS']).sum())/(j2[j88888[x]].sum())
      j22 = ((j2[j88888[x]]*j2['ERPE']).sum())/(j2[j88888[x]].sum())
      j23 = ((j2[j88888[x]]*j2['NERPE']).sum())/(j2[j88888[x]].sum())
      j_7[str(x)] = [float(j21),float(j22),float(j23)]
      j2 = pd.DataFrame()
      j2 = j1[(j1[j8888[x]]>float(j_88.iloc[x,6]))&(j1[j8888[x]]<=float(j_88.iloc[x,7]))]
      j21 = ((j2[j88888[x]]*j2['TCGS']).sum())/(j2[j88888[x]].sum())
      j22 = ((j2[j88888[x]]*j2['ERPE']).sum())/(j2[j88888[x]].sum())
      j23 = ((j2[j88888[x]]*j2['NERPE']).sum())/(j2[j88888[x]].sum())
      j_8[str(x)] = [float(j21),float(j22),float(j23)]
      j2 = pd.DataFrame()
      j2 = j1[(j1[j8888[x]]>float(j_88.iloc[x,7]))&(j1[j8888[x]]<=float(j_88.iloc[x,8]))]
      j21 = ((j2[j88888[x]]*j2['TCGS']).sum())/(j2[j88888[x]].sum())
      j22 = ((j2[j88888[x]]*j2['ERPE']).sum())/(j2[j88888[x]].sum())
      j23 = ((j2[j88888[x]]*j2['NERPE']).sum())/(j2[j88888[x]].sum())
      j_9[str(x)] = [float(j21),float(j22),float(j23)]
      j2 = pd.DataFrame()
      j2 = j1[(j1[j8888[x]]>float(j_88.iloc[x,8]))&(j1[j8888[x]]<=float(j_88.iloc[x,9]))]
      j21 = ((j2[j88888[x]]*j2['TCGS']).sum())/(j2[j88888[x]].sum())
      j22 = ((j2[j88888[x]]*j2['ERPE']).sum())/(j2[j88888[x]].sum())
      j23 = ((j2[j88888[x]]*j2['NERPE']).sum())/(j2[j88888[x]].sum())
      j_10[str(x)] = [float(j21),float(j22),float(j23)]
    j = pd.concat([j_1,j_2,j_3,j_4,j_5,j_6,j_7,j_8,j_9,j_10], axis=0, ignore_index=True)
    j =j.reindex([0,3,6,9,12,15,18,21,24,27,1,4,7,10,13,16,19,22,25,28,2,5,8,11,14,17,20,23,26,29])
    j.index = ['TCGS_10%','TCGS_20%','TCGS_30%','TCGS_40%','TCGS_50%','TCGS_60%','TCGS_70%','TCGS_80%','TCGS_90%','TCGS_100%','ERPE_10%','ERPE_20%','ERPE_30%','ERPE_40%','ERPE_50%','ERPE_60%','ERPE_70%','ERPE_80%','ERPE_90%','ERPE_100%','NERPE_10%','NERPE_20%','NERPE_30%','NERPE_40%','NERPE_50%','NERPE_60%','NERPE_70%','NERPE_80%','NERPE_90%','NERPE_100%']
    j.columns = ['total','Hispanic_or_Latino','white','black','American_Indian','Asian']
    j.to_excel(r' path\data\OSMdata\\'+list55[i]+'\\AA_shidengfen.xlsx')

for i in range(len(list55)):
    df88 = pd.DataFrame()
    df88 = pd.read_excel(r' path\data\OSMdata\\'+list55[i]+'\\'+list55[i]+'_resultschuliwalk.xlsx',sheet_name='MEAN')
    df88.drop(df88.columns[[0]],axis=1,inplace=True)
    plt.rcParams['font.sans-serif']=['Microsoft YaHei']
    TCGS = (df88.loc[0,:]/500).tolist()
    ERPE = (df88.loc[1,:]).tolist()
    NERPE = (df88.loc[2,:]/20).tolist()
    CI_TCGS = (df88.loc[3,:]/500).tolist()
    CI_ERPE = (df88.loc[4,:]).tolist()
    CI_NERPE = (df88.loc[5,:]/20).tolist()
    totalWidth=0.7
    labelNums=3
    barWidth=totalWidth/labelNums
    seriesNums=5
    error_params=dict(elinewidth=2,ecolor='black',capsize=3,)
    plt.clf() 
    plt.cla() 
    plt.bar([x for x in range(seriesNums)], TCGS, label="TCGS", width=barWidth,color='#5686bf',yerr=CI_TCGS,error_kw=error_params)
    plt.bar([x+barWidth for x in range(seriesNums)], ERPE, label="ERPE", width=barWidth,color='#006374',yerr=CI_ERPE,error_kw=error_params)
    plt.bar([x+2*barWidth for x in range(seriesNums)], NERPE, label="NERPE", width=barWidth,color='#c5a2b6',yerr=CI_NERPE,error_kw=error_params)
    plt.xticks([x+barWidth/2*(labelNums-1) for x in range(seriesNums)], ['Hispanic_or_Latino','white','black','American_Indian','Asian'])
    plt.xlabel("race/ethnicity")
    plt.ylabel("PCE accessibility")
    plt.title(''+list55[i]+'')
    plt.legend(loc="upper right")
    plt.savefig(r' path\python\output_figures\meansfigures\\'+list55[i]+'_PCEMEANwalk.jpg')

for i in range(len(list55)):
    df99 = pd.DataFrame()
    df99 = pd.read_excel(r' path\data\OSMdata\\'+list55[i]+'\\'+list55[i]+'_shidengfendrive.xlsx')
    df99.drop(df99.columns[[0]],axis=1,inplace=True)
    x = [1,2,3,4,5,6,7,8,9,10]
    co = ['dimgray','chocolate','palegreen','orange','turquoise','pink']
    leg = ['total','Hispanic_or_Latino','white','black','American_Indian','Asian']
    mak = ['*','o','^','s','+','d']
    for m in range(df99.shape[1]):
       df999 = (df99.iloc[:10,m].apply(np.log10)).tolist()
       plt.plot(x,df999, linewidth=1, color=co[m], marker=mak[m],label=leg[m],alpha=0.8)
       plt.legend(['total','Hispanic_or_Latino','white','black','American_Indian','Asian'],loc="upper right")
       plt.xlabel("Income deciles")
       plt.ylabel("TCGS accessibility")
    plt.grid() 
    plt.savefig(r' path\python\output_figures\incomefigures\\'+list55[i]+'_TCGSdrive.jpg')
    for m in range(df99.shape[1]):
       plt.plot(x,(df99.iloc[10:20,m]).tolist(), linewidth=1, color=co[m], marker=mak[m],label=leg[m])
       plt.legend(['total','Hispanic_or_Latino','white','black','American_Indian','Asian'],loc="upper right")
       plt.xlabel("Income deciles")
       plt.ylabel("ERPE accessibility")
       plt.title(''+list55[i]+'')
    plt.grid()
    for m in range(df99.shape[1]):
       plt.plot(x,(df99.iloc[20:30,m]).tolist(), linewidth=1, color=co[m], marker=mak[m],label=leg[m])
       plt.legend(['total','Hispanic_or_Latino','white','black','American_Indian','Asian'],loc="upper right")
       plt.xlabel("Income deciles")
       plt.ylabel("NERPE accessibility")
       plt.title(''+list55[i]+'')
    plt.grid()

for m in range(0,6):
   y1 = pd.DataFrame(columns=['a','s','d','f','g','h','j','k','l','q'])
   for i in range(len(list55)):
      df99 = pd.DataFrame()
      df99 = pd.read_excel(r' path\data\OSMdata\\'+list55[i]+'\\AA_shidengfen.xlsx')
      df99.drop(df99.columns[[0]],axis=1,inplace=True)
      df999 = df99.iloc[20:30]
      df999 = (df999.iloc[:,:].apply(np.log10))
      x = [1,2,3,4,5,6,7,8,9,10]
      y = (df999.iloc[:,m]).tolist()
      S1 = pd.Series(df999.iloc[:,m])
      S1.index = ['a','s','d','f','g','h','j','k','l','q']
      y1 = y1.append(S1,ignore_index=True) 
      co = ['dimgray','chocolate','deepskyblue','orange','darkgreen','deeppink']
      leg = ['total','Hispanic_or_Latino','white','black','American_Indian','Asian']
      mak = ['*','o','^','s','+','d']
      plt.scatter(x,y, color=co[m], marker=mak[m],label=leg[m],alpha=0.8)
      plt.legend([leg[m]],loc="upper right")
   y11 = y1.loc[:,:].median()
   plt.plot(x,(y11).tolist(),color='red',linewidth =2,markersize=8,marker=mak[m])
   plt.xlabel("Income deciles")
   plt.ylabel("NERPE accessibility")
   plt.grid()
   plt.savefig(r' path\python\output_figures\income_regression\\'+leg[m]+'_NERPEpw.jpg')
   plt.clf()
   plt.cla()