import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
import statsmodels.api as sm

str6='Travis County,Bexar County,Nueces County,Harris County,Tarrant County,Dallas County,San Diego County,Santa Clara County,Sacramento County,San Joaquin County,Alameda County,San Francisco County,Stanislaus County,Orange County,Fresno County,Riverside County,Pima County,Maricopa County,Allegheny County,Philadelphia County,Duval County,Suffolk County,Franklin County,Wayne County,Hennepin County,Multnomah County,Davidson County,Lancaster County,Shelby County,Fulton County,Mecklenburg County,Miami-Dade County,Cook County,Denver County,King County,Cuyahoga County,Monroe County,Baltimore city,Worcester County,District of Columbia'
str66 = 'TX,TX,TX,TX,TX,TX,CA,CA,CA,CA,CA,CA,CA,CA,CA,CA,AZ,AZ,Northeast,Northeast,Others,Northeast,Northeast,Northeast,Others,Others,Others,Others,Others,Others,Others,Others,Others,Others,Others,Northeast,Northeast,Northeast,Northeast,Northeast'
str99 = 'CA,TX,AZ,Northeast,Others'
list6 = str6.split(',')
list66 = str66.split(',')
list99 = str99.split(',')
mak = ['*','o','^','s','d']
plt.rc('font',family='Times New Roman') 
 
df = pd.read_excel(r'path\output\agg\AA_AggrePCE.xlsx')
df = df.dropna(axis='index',how='any',subset=['TCGS','ERPE','NERPE']) 
df['TCGS'] = df['TCGS'].apply(np.log10)
df['ERPE'] = df['ERPE'].apply(np.log10)
df['NERPE'] = df['NERPE'].apply(np.log10)
X = df[['AP']]
Y = df['NERPE']
for i in range(len(list6)):
    df.loc[(df["county"]==list6[i]) ,'region'] = list66[i]
for i in range(len(list99)):
    xc = df[(df["region"]==list99[i])]
    xc1 = xc[['AP']]
    xc2 = xc['NERPE']
    plt.scatter(xc1,xc2,s=5,c=np.random.rand(len(xc)),marker=mak[i],alpha=0.8)
    plt.legend(['CA','TX','AZ','Northeast','Others'],loc="lower left",bbox_to_anchor=(0, 0))
plt.colorbar()
model = LinearRegression()
model.fit(X,Y)
plt.plot(X,model.predict(X),color='red',linewidth =3)
plt.xlabel('Asian proportion')
plt.ylabel('NERPE accessibility')
plt.show()
model.coef_,model.intercept_
X2 = sm.add_constant(X)
est = sm.OLS(Y,X2).fit()
est.summary()



