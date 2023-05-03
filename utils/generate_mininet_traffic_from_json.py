import json
import time
import sys

def generate_traffic():
    with open('traffic.json', 'r') as f:
        traffic_data = json.load(f)
    
    commands = []
    for traffic in traffic_data:
        src = 'h' + str(traffic['src'])
        dst = 'h' + str(traffic['dst'])
        port = 5000 + traffic['src']
        log_file = 'experiments/results/{}-{}.json'.format(src, dst)
        start_time = traffic['start_time']
        commands.append('time.sleep({})\n'.format(start_time))
        commands.append("{}"
                        ".cmd('iperf3 -c {} -p {} -J --logfile {} &')\n".format(src, dst, port, log_file))
        if src != dst:
            commands.append('time.sleep(2)\n')
            commands.append("{}"
                            ".cmd('iperf3 -c {} -p {} -J --logfile {} &')\n".format(dst, src, port+1, log_file))
    
    sys.stdout.write(''.join(commands))

generate_traffic() 
