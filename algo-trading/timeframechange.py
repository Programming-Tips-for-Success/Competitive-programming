import pandas as pd
import numpy as np
import time
import math
def minute_convertion(timeframe,data):
    
    i=0
    value1,value1_index,value2,value2_index =0,0,0,0
    count=0
    new_list =[]
    df = data
    day_change_index = []
    
    for i,x in enumerate(data.date):
        if x[11:] == "00:01:00.000Z":
            day_change_index.append(i)

    for j in day_change_index:
        d=math.ceil((j-i)/timeframe)
        count =0
#         print(j)
        
        for k in range(i,j+1,timeframe):
            count=count+1
#             print(k)
            
            if count!=d: 
                m=df.loc[k,"date"]
                n=df.loc[k+(timeframe)-1,"date"]
#                 print(m,n)
                
                for p,q in enumerate(df.date):
                    if q == m:
                        value1 = df.loc[p]
                        value1_index=p
                        break
                        
                for p,q in enumerate(df.date):
                    if q == n:
                        value2 = df.loc[p]
                        value2_index = p
                        break
                        
                new_list.append([n,df.loc[value1_index,"open"],max(df.loc[value1_index:value2_index,"high"])
                                ,min(df.loc[value1_index:value2_index,"low"]),df.loc[value2_index,"close"],
                                sum(df.loc[value1_index:value2_index,"volume"])])

            else:
                m=df.loc[k,"date"]
                n=df.loc[j-1,"date"]
                
                for p,q in enumerate(df.date):
                    if q == m:
                        value1 = df.loc[p]
                        value1_index=p
#                         print(value1)
                        break
                
                for p,q in enumerate(df.date):
                    if q == n:
                        value2 = df.loc[p]
                        value2_index = p
#                         print(value2)
                        break
                
                new_list.append([n,df.loc[value1_index,"open"],max(df.loc[value1_index:value2_index,"high"])
                                ,min(df.loc[value1_index:value2_index,"low"]),df.loc[value2_index,"close"],
                                sum(df.loc[value1_index:value2_index,"volume"])])
        i=j
    
    new_data = pd.DataFrame(new_list,columns = ["date","open","high","low","close","volume"],index= None)
    return new_data
a = minute_convertion(72,new_df)
a = a.drop_duplicates()
a = a.reset_index(drop=True)
b = HA(new_df)
