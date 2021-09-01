import pandas as pd
import csv

df = pd.read_csv('total_stars.csv')


#del df["Luminosity"]


df.drop(['Unnamed: 0','Unnamed: 6', 'Star_name.1', 'Distance.1', 'Mass.1', 'Radius.1','Luminosity','NAN'],axis=1,inplace=True)

#print(df.shape)
#print(list(df))

df = df.rename({

    'Star_name': "Scientific_star_name", 
    'Mass':"Weight"
    

} , axis='columns')


#print(list(df))




df.to_csv("final.csv")





# Check final csv containing data (final.csv)

