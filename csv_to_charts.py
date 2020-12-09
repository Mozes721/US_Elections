import pandas
#write to CSV/EXCEL
pandas.read_json('trump_results.json').to_excel('trump.xlsx')
pandas.read_json('biden_results.json').to_excel('biden.xlsx')


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
#convert to float
x = ','.join(trump_votes)
votes = np.fromstring(x, dtype)

plt.pie(votes, labels=states)
plt.title("Trump Election chart by votes")
plt.show()