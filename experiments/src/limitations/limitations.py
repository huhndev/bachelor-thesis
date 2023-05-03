import time

from mininet.log import lg

import ipmininet
from ipmininet.cli import IPCLI
from ipmininet.ipnet import IPNet
from ipmininet.iptopo import IPTopo

class Topo(IPTopo):

    def build(self, *args, **kwargs):

        #Hosts
        h1 = self.addRouter('h1')
        h2 = self.addRouter('h2')
        h3 = self.addRouter('h3')
        h4 = self.addRouter('h4')

        #Routers
        ra = self.addRouter('ra')

        #Links
        self.addLink(ra, h1, igp_metric=100, bw=1000, delay="5ms")
        self.addLink(ra, h2, igp_metric=100, bw=1000, delay="5ms")
        self.addLink(ra, h3, igp_metric=100, bw=1000, delay="5ms")
        self.addLink(ra, h4, igp_metric=100, bw=1000, delay="5ms")

        super(Topo, self).build(*args, **kwargs)

def perfTest():

    print("*** Waiting for network to start")
    for i in range(30,0,-1):
        print(f"{i}  ", end="\r", flush=True)
        time.sleep(1) 

    print("*** Testing bandwidth between hosts")
    
    h1 = net.routers[0]
    h2 = net.routers[1]
    h3 = net.routers[2]
    h4 = net.routers[3]

    h1.cmd('iperf3 -s -p 5002 &')
    h1.cmd('iperf3 -s -p 5003 &')
    h1.cmd('iperf3 -s -p 5004 &')
    h1.cmd('iperf3 -s -p 5012 &')
    h1.cmd('iperf3 -s -p 5013 &')
    h1.cmd('iperf3 -s -p 5014 &')
    h2.cmd('iperf3 -c h1 -p 5002 -t 30 -O 10 -J --logfile experiments/results/limitation-h2-h1-1.json &')
    h3.cmd('iperf3 -c h1 -p 5003 -t 30 -O 10 -J --logfile experiments/results/limitation-h3-h1-1.json &')
    h4.cmd('iperf3 -c h1 -p 5004 -t 30 -O 10 -J --logfile experiments/results/limitation-h4-h1-1.json &')  
    h2.cmd('iperf3 -c h1 -p 5012 -t 30 -O 10 -J --logfile experiments/results/limitation-h2-h1-2.json &')
    h3.cmd('iperf3 -c h1 -p 5013 -t 30 -O 10 -J --logfile experiments/results/limitation-h3-h1-2.json &')
    h4.cmd('iperf3 -c h1 -p 5014 -t 30 -O 10 -J --logfile experiments/results/limitation-h4-h1-2.json &')
    for i in range(50,0,-1):
        print(f"{i}  ", end="\r", flush=True)
        time.sleep(1)

ipmininet.DEBUG_FLAG = True
lg.setLogLevel("info")

# Start network
net = IPNet(topo=Topo(), use_v6=False)
net.start()
#IPCLI(net)
perfTest()
net.stop()
