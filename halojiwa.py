import pandas as pd
import numpy as np
import seaborn as sb
import matplotlib.pyplot as plt
from matplotlib import style

# setting style for graphs
style.use('ggplot')
plt.rcParams['figure.figsize'] = (20,10)

# read data from excel
df = pd.read_excel('Canada.xlsx',1, skiprows = range(20), skipfooter = 2)

df.drop(['AREA','REG','DEV','Type','Coverage','DevName'], axis=1, inplace=True)
df.rename(columns = {'OdName':'country','AreaName':'continent','RegName':'region'}, inplace = True)
df['total'] = df.sum(axis = 1)
df = df.set_index('country')
df.rename(index = {'United Kingdom of Great Britain and Northern Ireland':'UK & Ireland'}, inplace = True)
df.columns = df.columns.astype(str)

# Useful for upcoming visualizations
years = list(map(str, range(1980,2013)))


# Single line chart
fig1 = df.loc['Haiti', years].plot(kind = 'line', color = 'r')
plt.title('Immigration from Haiti to Canada from 1980-2013',color = 'black')
plt.xlabel('Years',color = 'black')
plt.ylabel('Number of Immigrants',color = 'black')
plt.xticks(color = 'black')
plt.yticks(color = 'black')
plt.savefig('linechart_single.png')
plt.show()



# # Multiple lines

# fig2 = plt.plot(df.loc['India',years], label = 'India')
# plt.plot(df.loc['China',years], label = 'China')
# plt.plot(df.loc['Philippines',years], label = 'Sri Lanka')
# plt.legend(loc = 'upper left', fontsize = 12)
# plt.xticks(rotation = 90, color = 'black')
# plt.yticks(color = 'black')
# plt.title('Immigration to Canada from 1980-2013',color = 'black')
# plt.xlabel('Year',color = 'black')
# plt.ylabel('Number of Immigrants',color = 'black')
# plt.savefig('linechart_multiple.png')

# plt.show()

# # Cyberpunk Multiple Line Chart

# import mplcyberpunk
# style.use('cyberpunk')

# plt.plot(df.loc['India',years], label = 'India')
# plt.plot(df.loc['China',years], label = 'China')
# plt.plot(df.loc['Philippines',years], label = 'Sri Lanka')
# plt.legend(loc = 'upper left', fontsize = 14)
# plt.xticks(rotation = 90, color = 'white', fontsize = 14, fontweight = 'bold')
# plt.yticks(color = 'white', fontsize = 14, fontweight = 'bold')
# plt.title('Immigration to Canada from 1980-2013',color = 'white', fontsize = 20, fontweight = 'bold')
# plt.xlabel('Year',color = 'white', fontsize = 16, fontweight = 'bold')
# plt.ylabel('Number of Immigrants',color = 'white',fontsize = 16, fontweight = 'bold')
# plt.savefig('cyber_line.png')

# plt.show()

# # Vertical
# style.use('ggplot')

# df_tot = pd.DataFrame(df.loc[:,years].sum())
# df_tot.rename(columns = {0:'total'}, inplace = True)

# df_tot.plot(kind = 'bar', legend = False)
# plt.title('Total Immigrants to Canada from 1980-2013',color = 'black')
# plt.xticks(color = 'black')
# plt.yticks(color = 'black')
# plt.xlabel('Year',color = 'black')
# plt.ylabel('Number of Immigrants',color = 'black')
# plt.savefig('bar_vertical.png')

# plt.show()



# # Grouped

# year_int10 = list(map(str, (1980,1990,2000,2010, 2013)))
# df_group = pd.DataFrame(df.loc[['India','China','Philippines','Pakistan'],year_int10].T)

# df_group.plot.bar(edgecolor = 'white')
# plt.title('Total Immigrants to Canada from 1980-2013',color = 'black')
# plt.xticks(color = 'black')
# plt.yticks(color = 'black')
# plt.xlabel('Year',color = 'black')
# plt.ylabel('Number of Immigrants',color = 'black')
# plt.legend(title = 'Country', fontsize = 12)
# plt.savefig('bar_grouped.png')

# plt.show()