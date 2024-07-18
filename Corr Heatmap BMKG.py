import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt

dataframe = pd.read_csv('Corr Heatmap BMKG.csv', delimiter = ';')
print(dataframe.head())

dataframe.corr()

plt.figure(figsize=(16, 6))
# Store heatmap object in a variable to easily access it when you want to include more features (such as title).
# Set the range of values to be displayed on the colormap from -1 to 1, and set the annotation to True to display the correlation values on the heatmap.
heatmap = sns.heatmap(dataframe.corr(), vmin = -1, vmax = 1, annot = True)
# Give a title to the heatmap. Pad defines the distance of the title from the top of the heatmap.
heatmap.set_title('Correlation Heatmap', fontdict = {'fontsize':12}, pad = 12)

ctoin = ['T', 'RH', 'R', 'FF', 'RMM']

# Define the phases to analyze
phases_to_analyze = [3, 4, 5, 6]

for phase in phases_to_analyze:
    # Filter the dataset for the specific phase
    dataframe_phase = dataframe[dataframe['Phase'] == phase][ctoin]
    # Create the correlation heatmap for the specific phase
    plt.figure(figsize=(16, 6))
    heatmap = sns.heatmap(dataframe_phase.corr(), vmin=-1, vmax=1, annot=True)
    heatmap.set_title(f'Correlation Heatmap on MJO Phase {phase} (BMKG)', fontdict={'fontsize':12}, pad=12)
    # Save the plot
    plt.savefig(f'Correlation Heatmap Phase{phase} (BMKG).png', bbox_inches='tight')
    plt.close()

plt.show()
