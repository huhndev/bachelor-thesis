import json
import os
import glob

avg_obj = {}

runs = os.listdir('.')
runs.remove('run-avg')
print(runs)
for run in runs:
    traffics = glob.glob('./' + run + '/*.json')
    for traffic in traffics:
        with open(traffic) as f:
            data = json.load(f)
            traffic_name = traffic.split('/')[2]
            traffic_name = traffic_name.split('.')[0]
            if (traffic_name not in avg_obj):
                avg_obj[traffic_name] = {}
                avg_obj[traffic_name]['end'] = {}
                avg_obj[traffic_name]['end']['sum_sent'] = data['end']['sum_sent']
            else:
                avg_obj[traffic_name]['end']['sum_sent']['seconds'] += data['end']['sum_sent']['seconds']
                avg_obj[traffic_name]['end']['sum_sent']['bytes'] += data['end']['sum_sent']['bytes']
                avg_obj[traffic_name]['end']['sum_sent']['bits_per_second'] += data['end']['sum_sent']['bits_per_second']


for traffic in avg_obj:
    current_traffic = avg_obj[traffic]
    current_traffic['end']['sum_sent']['seconds'] = current_traffic['end']['sum_sent']['seconds'] / len(runs)
    current_traffic['end']['sum_sent']['bytes'] = current_traffic['end']['sum_sent']['bytes'] / len(runs)
    current_traffic['end']['sum_sent']['bits_per_second'] = current_traffic['end']['sum_sent']['bits_per_second'] / len(runs)
    with open('run-avg/' + traffic + '-avg.json', 'w') as outfile:
        json.dump(current_traffic, outfile)
