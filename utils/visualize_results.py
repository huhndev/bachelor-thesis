import json
import matplotlib.pyplot as plt
import os

# get all filenames from results directory
files = os.listdir('experiments/results/')
files.sort()

# initialize empty lists for storing values
values = []
traffic_flows = []

time_zero = 0

# loop through files
for file in files:
    # open file and store values in variables
    with open('experiments/results/' + file) as f:
        data = json.load(f)
        traffic_flow = file.split('-')[1] + '-' + file.split('-')[2]
        traffic_flow = traffic_flow.split('.')[0]
        intervals = data['intervals']
        timestamp = data['start']['timestamp']['timesecs']
        if (time_zero == 0):
            time_zero = timestamp
        xValues = []
        yValues = []
        for interval in intervals:
            sum = interval['sum']
            #print(sum)
            start = timestamp + sum['start']
            end = timestamp + sum['end']
            bps = sum['bits_per_second']
            xValues.append(start-time_zero)
            yValues.append(bps/1000000)
        values.append({'name': traffic_flow, 'val': {'x': xValues, 'y': yValues}})

# generate graph 
for traffic in values:
    plt.plot(traffic['val']['x'], traffic['val']['y'], label = traffic['name'])

plt.xlabel('s')
plt.ylabel('Mbit/s') 
plt.title('Traffic Overview')
plt.legend()

# save graph as a png
plt.savefig('graph.png')
