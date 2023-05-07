import json
import time
import sys

def generate_traffic():
    with open('traffic.json', 'r') as f:
        traffic_data = json.load(f)

    traffic_sorted = sorted(traffic_data, key=lambda x: x.get('start_time', 0), reverse=False)

    time = 0

    listen_commands = []
    commands = []
    for traffic in traffic_sorted:
        src = 'h' + str(traffic['src'])
        dst = 'h' + str(traffic['dst'])
        port = 5000 + traffic['src']
        log_file = 'experiments/results/{}-{}-{}.json'.format(traffic['start_time'], src, dst)
        start_time = traffic['start_time'] - time
        time = traffic['start_time']
        commands.append('time.sleep({})\n'.format(start_time))
        commands.append("{}"
                        ".cmd('iperf3 -c {} -p {} -J --logfile {} &')".format(src, dst, port, log_file))
        listen_commands.append("{}.cmd('iperf3 -s -p {} &')".format(dst, port))
    print('\n'.join(map(str, listen_commands)) + '\n')
    print('\n'.join(map(str, commands)))

generate_traffic()
