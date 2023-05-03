import json
import matplotlib.pyplot as plt
import os

# get all filenames from results directory
files = os.listdir('experiments/results/')

# initialize empty lists for storing values
rx_values = []
tx_values = []

# loop through files
for file in files:
    # open file and store values in variables
    with open('experiments/results/' + file) as f:
        data = json.load(f)
        rx_values.append(data['intervals'][0]['streams'][0]['bits_per_second'])
        try:
            tx_values.append(data['intervals'][0]['streams'][1]['bits_per_second'])
        except IndexError:
            tx_values.append(data['intervals'][0]['streams'][0]['bits_per_second'])

# generate boxplots
fig, axes = plt.subplots(1, 2)
axes[0].boxplot(rx_values)
axes[0].set_title('Receive values')
axes[1].boxplot(tx_values)
axes[1].set_title('Transmit values')

# display boxplots
plt.show()

# save boxplots as a png
fig.savefig('boxplots.png')
