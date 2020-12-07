import pandas as pd 
#write to CSV/EXCEL
trump_csv = pd.read_json('trump_results.json')
biden_csv = pd.read_json('biden_results.json')
trump_csv.to_csv('trump.csv')
biden_csv.to_csv('biden.csv')


#Code from Jupyter Notebook
import pandas as pd 
from matplotlib import pyplot as plt
import matplotlib.colors as pltc

#read and remove one collumn
trumpcsv = pd.read_csv("/home/mozes721/Desktop/US_Elections/trump.csv")
bidencsv =pd.read_csv("/home/mozes721/Desktop/US_Elections/biden.csv")
trumpcsv_adjusted = trumpcsv.drop('Unnamed: 0', axis=1)
bidencsv_adjusted = bidencsv.drop('Unnamed: 0', axis=1)

states = []

trump_votes = []
trump_percent = []
#get each column value
for state in trumpcsv_adjusted.iloc[:,0]:
    states.append(state)


for vote in trumpcsv_adjusted.iloc[:,1]:
    trump_votes.append(vote)


for percent in trumpcsv_adjusted.iloc[:,2]:
    trump_percent.append(percent)


biden_votes = []
biden_percent = []

for vote in bidencsv_adjusted.iloc[:,1]:
    biden_votes.append(vote)


for percent in bidencsv_adjusted.iloc[:,2]:
    biden_percent.append(percent)

#adjusting trying to convert to float value
trump_votes.astype(float)
plt.axis("equal")
plt.pie(trump_votes, labels=states, autopct='%0.1f%%')
trump_axis_votes.show()