import argparse
import json
import random

# Festlegen der Argumente für die Kommandozeile
parser = argparse.ArgumentParser(description='Generates traffic for a virtual network.')
parser.add_argument('--max-point', '-p', type=int, default=100, help='Maximum value for start and destination points.')
parser.add_argument('--max-start-time', '-t', type=int, default=1000, help='Maximum value for start time.')
parser.add_argument('--avg-flow-size', '-s', type=int, default=1, help='Average flow size in megabytes.')
parser.add_argument('--num-flows', '-n', type=int, default=10, help='Number of flows to generate.')
parser.add_argument('--output', '-o', type=str, default='-', help='Output file path. Use - for stdout.')
args = parser.parse_args()

# Generieren des Traffics für jedes Flow
flows = []
for i in range(args.num_flows):
    # Generieren von zufälligen Start- und Zielpunkten
    src = random.randint(0, args.max_point)
    dst = random.randint(0, args.max_point)
    while dst == src:
        dst = random.randint(0, args.max_point)
    # Generieren einer zufälligen Größe für den Traffic (Exponentialverteilung)
    size = int(random.expovariate(1/(args.avg_flow_size*1024)) * 1024)
    # Generieren eines zufälligen Startzeitpunkts
    start_time = random.randint(0, args.max_start_time)
    # Hinzufügen des Flows zur Liste
    flows.append({'src': src, 'dst': dst, 'size': size, 'start_time': start_time})

# Ausgabe als JSON
if args.output == '-':
    print(json.dumps(flows))
else:
    with open(args.output, 'w') as f:
        json.dump(flows, f) 
