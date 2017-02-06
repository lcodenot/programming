import pandas as pd
import numpy as np
import scipy as sp
import matplotlib.pyplot as plt
data = pd.read_csv('FMC.txt' ,sep =' ', header = None)
data.columns = ['Enterprise Flag','Record Number','US Postal Code','MSA Code','County','Census Tract','Percent Minority','CT Median Income','LA Median Income','Tract Income Ratio','Borrower Annual Income','Area Median Income','Borrower Income Ratio','Aquisition UPB','Purpose of Loan','Federal Guarantee','Number of Borrowers','First Time','Borrower Race 1','Borrower Race 2','Borrower Race 3','Borrower Race 4','Borrower Race 5','Borrower Ethnicity','Coborrower Race 1','Coborrower Race 2','Coborrower Race 3','Coborrower Race 4','Coborrower Race 5','Coborrower Ethnicity','Borrower Grender','Coborrower Gender','Borrower Age','Coborrower Age','Occupancy Code','Rate Spread','HOEPA Status','Property Type','Lien Status']

#df_upper = data.loc[data['Borrower Income Ratio']>1]
#df_lower = data.loc[data['Borrower Income Ratio']<=1]

#df_minority = data.loc[(data['Borrower Race 1']<5) or (data['Borrower Race 2']<5) or (data['Borrower Race 3']<5) or (data['Borrower Race 4']<5) or (data['Borrower Race 5']<5) or (data['Coborrower Race 1']<5) or (data['Coborrower Race 2']<5) or (data['Coborrower race 3']<5) or (data['Coborrower Race4']<5) or (data['coborrower race5']<5) or (data['Coborrower Ethnicity']=1) or (data['Borrower Ethnicity']=1)]

df = data.loc[(data['Borrower Income Ratio']<9998) & (data['Occupancy Code']==1) & (data['First Time']==1) & (data['Borrower Race 1']<6)]

df_native =df.loc[(data['Borrower Race 1']==1)]
#print (df_native.loc[(df['Federal Guarantee']==4)])['Enterprise Flag'].count()
df_asian =df.loc[(data['Borrower Race 1']==2)]
#print (df_asian.loc[(df['Federal Guarantee']==4)])['Enterprise Flag'].count()
df_black =df.loc[(data['Borrower Race 1']==3)]
#print (df_black.loc[(df['Federal Guarantee']==4)])['Enterprise Flag'].count()
df_pacific =df.loc[(data['Borrower Race 1']==4)]
#print (df_pacific.loc[(df['Federal Guarantee']==4)])['Enterprise Flag'].count()
df_white =df.loc[(data['Borrower Race 1']==5)]
#print (df_white.loc[(df['Federal Guarantee']==4)])['Enterprise Flag'].count()
df_minority =df.loc[(data['Borrower Race 1']<5)]
#print (df_minority.loc[(df['Federal Guarantee']==4)])['Enterprise Flag'].count()


'''
print df_minority[['Borrower Income Ratio']].mean()

print df_native[['Borrower Income Ratio']].mean()

print df_asian[['Borrower Income Ratio']].mean()

print df_black[['Borrower Income Ratio']].mean()

print df_pacific[['Borrower Income Ratio']].mean()

print df_white[['Borrower Income Ratio']].mean()
'''

df.boxplot(column = 'Percent Minority', by = 'Federal Guarantee')
df_Fed2 = df.loc[(df['Federal Guarantee']==2)]
#df_Fed2.boxplot(column = 'Borrower Income Ratio', by = 'Borrower Race 1')
#df.boxplot(column = 'Borrower Annual Income', by = 'Borrower Race 1')
#df.boxplot(column = 'Aquisition UPB', by = 'Borrower Race 1')
#df.boxplot(column = 'Area Median Income', by = 'Borrower Race 1')

#df_Fed2.plot.scatter(x='Percent Minority', y='Borrower Income Ratio',marker='o')
#df_Fed2.plot.scatter(x='Percent Minority', y='Borrower Annual Income',marker='o')
#df_Fed2.plot.scatter(x='Percent Minority', y='Area Median Income',marker='o')
#df_Fed2.plot.scatter(x='Percent Minority', y='Aquisition UPB',marker='o')

'''
df_Fed4 = df.loc[(df['Federal Guarantee']==4)]
df_Fed4.boxplot(column = 'Borrower Income Ratio', by = 'Borrower Race 1')
df_Fed4.boxplot(column = 'Borrower Annual Income', by = 'Borrower Race 1')
df_Fed4.boxplot(column = 'Aquisition UPB', by = 'Borrower Race 1')
df_Fed4.boxplot(column = 'Area Median Income', by = 'Borrower Race 1')
'''

plt.show()

'''

df_rate = data.loc[(data['Rate Spread']>0) & (data['Borrower Income Ratio']<9998) & (data['Occupancy Code']==1)]

print df_rate[['Borrower Income Ratio']].mean()

df_hoepa = data.loc[(data['HOEPA Status']==2) & (data['Borrower Income Ratio']<9998) & (data['Occupancy Code']==1)]

print df_hoepa[['Borrower Income Ratio']].mean()

df = data.loc[(data['Borrower Income Ratio']<9998) & (data['Occupancy Code']==1)]

print df[['Borrower Income Ratio']].mean()

df_None = data.loc[(data['Federal Guarantee']==1) & (data['Borrower Income Ratio']<9998) & (data['Occupancy Code']==1)]

print df_None[['Borrower Income Ratio']].mean()

df_FHA = data.loc[(data['Federal Guarantee']==2) & (data['Borrower Income Ratio']<9998) & (data['Occupancy Code']==1)]

print df_FHA[['Borrower Income Ratio']].mean()

df_VA = data.loc[(data['Federal Guarantee']==3) & (data['Borrower Income Ratio']<9998) & (data['Occupancy Code']==1)]

print df_VA[['Borrower Income Ratio']].mean()

df_FSA = data.loc[(data['Federal Guarantee']==4) & (data['Borrower Income Ratio']<9998) & (data['Occupancy Code']==1)]

print df_FSA[['Borrower Income Ratio']].mean()

df_minority = data.loc[(data['Federal Guarantee']==3) & (data['Borrower Race 1']<5) & (data['Coborrower Race 1']<5) & (data['Borrower Income Ratio']<9998) & (data['Occupancy Code']==1)]

print df_minority[['Borrower Income Ratio']].mean()

df_white = data.loc[(data['Federal Guarantee']==3) & ((data['Borrower Race 1']==5) | (data['Coborrower Race 1']==5)) & (data['Borrower Income Ratio']<9998) & (data['Occupancy Code']==1)]

print df_white[['Borrower Income Ratio']].mean()

df_native = data.loc[(data['Federal Guarantee']==3) & (data['Borrower Race 1']==1) & (data['Coborrower Race 1']==1) & (data['Borrower Income Ratio']<9998) & (data['Occupancy Code']==1)]

print df_native[['Borrower Income Ratio']].mean()

df_asian = data.loc[(data['Federal Guarantee']==3) & (data['Borrower Race 1']==2) & (data['Coborrower Race 1']==2) & (data['Borrower Income Ratio']<9998) & (data['Occupancy Code']==1)]

print df_asian[['Borrower Income Ratio']].mean()

df_black = data.loc[(data['Federal Guarantee']==3) & (data['Borrower Race 1']==3) & (data['Coborrower Race 1']==3) & (data['Borrower Income Ratio']<9998) & (data['Occupancy Code']==1)]

print df_black[['Borrower Income Ratio']].mean()

df_pacific = data.loc[(data['Federal Guarantee']==3) & (data['Borrower Race 1']==4) & (data['Coborrower Race 1']==4) & (data['Borrower Income Ratio']<9998) & (data['Occupancy Code']==1)]

print df_pacific[['Borrower Income Ratio']].mean()
'''

#df_native.plot.scatter(x='Borrower Income Ratio', y='Aquisition UPB',marker='o')
#df_asian.plot.scatter(x='Borrower Income Ratio', y='Aquisition UPB',marker='o')
#df_black.plot.scatter(x='Borrower Income Ratio', y='Aquisition UPB',marker='o')
#df_pacific.plot.scatter(x='Borrower Income Ratio', y='Aquisition UPB',marker='o')
#df_white.plot.scatter(x='Borrower Income Ratio', y='Aquisition UPB',marker='o')

#df_minority.plot.scatter(x='Borrower Income Ratio', y='Aquisition UPB',marker='o')
#plt.show()

print df['Enterprise Flag'].count() 
print (df.loc[(df['Percent Minority']>50)])['Enterprise Flag'].count()
print (df.loc[(df['Percent Minority']>90)])['Enterprise Flag'].count()
print df_native['Enterprise Flag'].count() 
print (df_native.loc[df_native['Percent Minority']>50])['Enterprise Flag'].count()
print (df_native.loc[df_native['Percent Minority']>90])['Enterprise Flag'].count()
print df_asian['Enterprise Flag'].count() 
print (df_asian.loc[df_asian['Percent Minority']>50])['Enterprise Flag'].count()
print (df_asian.loc[df_asian['Percent Minority']>90])['Enterprise Flag'].count()
print df_black['Enterprise Flag'].count() 
print (df_black.loc[df_black['Percent Minority']>50])['Enterprise Flag'].count()
print (df_black.loc[df_black['Percent Minority']>90])['Enterprise Flag'].count()
print df_pacific['Enterprise Flag'].count() 
print (df_pacific.loc[df_pacific['Percent Minority']>50])['Enterprise Flag'].count()
print (df_pacific.loc[df_pacific['Percent Minority']>90])['Enterprise Flag'].count()
print df_white['Enterprise Flag'].count() 
print (df_white.loc[df_white['Percent Minority']>50])['Enterprise Flag'].count()
print (df_white.loc[df_white['Percent Minority']>90])['Enterprise Flag'].count()



