#!/usr/bin/env python
# coding: utf-8

# In[10]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd

# Your data
data = {
    'Minerals': ['Magnesium', 'Potassium', 'Calcium', 'Zinc', 'Iron', 'Iodine', 'Selenium'],
    'Gracilaria': [292.2, 5791.8, 175.63, 4.5, 80.13, None, None],
    'Ulva': [806.35, 474.23, 740.05, 2.14, 43.19, None, 1.04],
    'Enteromorpha': [61.7, 325.11, 48.96, 1.16, 13.75, None, None],
    'Padina': [2.16, 81.11, 1571.35, 1.2, 47.84, None, None],
    'Sargassum': [198.98, 3.4, 2.17, 1.51, None, 25.82, None],
    'Hypnea': [411.56, 2.55, None, 1.29, None, 7.34, None],
    'Caulerpa': [257.90, 519.55, 750.96, 2.24, 75.17, None, None]
}

df = pd.DataFrame(data)

# Create a heat map with specified font settings
plt.figure(figsize=(10, 8))
sns.heatmap(df.set_index('Minerals'), cmap='rocket', annot=True, fmt=".2f", linewidths=.5)

# Set title and axis labels with specified font settings
plt.title('Minerals Content in Different Seaweed Species', fontsize=14, fontname='Times New Roman')
plt.xlabel('Seaweed Species', fontsize=12, fontname='Times New Roman')
plt.ylabel('Minerals', fontsize=12, fontname='Times New Roman')

# Set the tick labels' font settings
plt.xticks(fontsize=12, fontname='Times New Roman',rotation=45)
plt.yticks(fontsize=12, fontname='Times New Roman',rotation=45)

# Save the figure as a PNG file
plt.savefig('seaweed_heatmap.png', dpi=300, bbox_inches='tight')

# Show the heatmap
plt.show()


# In[9]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Your data with None values
data = {
    "Fatty Acid": ['MUFA', 'SFA', 'PUFA', 'EPA', 'DHA'],
    'Gracilaria': [None, None, None, None, None],
    'Ulva': [12.69, 60.47, 14.64, 1.1, 0.66],
    'Enteromorpha': [24.8, 60.6, 14.8, 0.3, None],
    'Padina': [12.68, 16.37, 21.89, None, None],
    'Sargassum': [17.71, 61.63, 10.13, None, None],
    'Hypnea': [8.41, 64.12, 4.75, None, None],
    'Caulerpa': [20.02, 41.00, 16.75, None, None]
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Replace None with np.nan to handle missing data
df = df.replace({None: np.nan})

# Create a heatmap, hiding cells with missing data
plt.figure(figsize=(10, 8))
sns.heatmap(df.set_index("Fatty Acid"), cmap='mako', annot=True, fmt=".2f", linewidths=.5, mask=df.set_index("Fatty Acid").isnull())

# Set title and axis labels with specified font settings
plt.title('Fatty Acid Content in Different Seaweed Species', fontsize=14, fontname='Times New Roman')
plt.xlabel('Seaweed Species', fontsize=12, fontname='Times New Roman')
plt.ylabel("Fatty Acid", fontsize=12, fontname='Times New Roman')

# Set the tick labels' font settings
plt.xticks(fontsize=12, fontname='Times New Roman',rotation=45)
plt.yticks(fontsize=12, fontname='Times New Roman',rotation=45)

# Save the figure as a PNG file
plt.savefig('seaweed_Fatty Acid_heatmap.png', dpi=300, bbox_inches='tight')

# Show the heatmap
plt.show()


# In[1]:


import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

# Your data with some missing values
data = {
    "Seaweed Species": ['Caulerpa', 'Ulva', 'Gracilaria', 'Enteromorpha', 'Padina', 'Sargassum', 'Hypnea'],
    'Histidine': [20.22,15.8,5, None,None,None,6.4],
    'Iso-Leucine': [28.96,17.6,10, None, 1.05, None,42.1],
    'Leucine': [48.27, 43.42, 15.1, None, 3.66, None, 45.6],
    'Lysine': [36.75, 27.84, 10.3, None, 2.98, None, 84.8],
    'Methionine': [12.71, 5.97, 6.6, None, None, None, 16.2],
    'Tryptophan': [0.45, None, None, None, None, None, None],
    'Valine': [41.27, 33.8, 10.8, None, 1.15, None, 55.8],
    'Threonine': [35.9, 26.41, 11.6, None, 1.319, None, 62.7],
    'Phenylalanine': [32.61, 27.52, 11.7,None , None, None,32.9],
}

# Convert data to DataFrame
df = pd.DataFrame(data)

# Replace None with np.nan to handle missing data
df = df.replace({None: np.nan})

# Set the 'Seaweed Species' column as the index
df.set_index('Seaweed Species', inplace=True)

# Create a heatmap, hiding cells with missing data
plt.figure(figsize=(12, 8))
sns.heatmap(df, cmap='viridis', annot=True, fmt=".2f", linewidths=.5, mask=df.isnull(), cbar_kws={'label': 'Amino Acid Concentration'})

# Set title and axis labels
plt.title('Amino Acid Content in Different Seaweed Species', fontsize=16, fontname='Times New Roman')
plt.xlabel('Amino Acids', fontsize=14, fontname='Times New Roman')
plt.ylabel('Seaweed Species', fontsize=14, fontname='Times New Roman')

# Set the tick labels' font settings
plt.xticks(fontsize=12, fontname='Times New Roman', rotation=45)
plt.yticks(fontsize=12, fontname='Times New Roman',rotation=45)
# Save the figure as a PNG file
plt.savefig('seaweed_Amino Acid_heatmap.png', dpi=300, bbox_inches='tight')

# Show the heatmap
plt.show()


# In[ ]:




