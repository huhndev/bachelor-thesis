import time

from mininet.log import lg

import ipmininet
from ipmininet.cli import IPCLI
from ipmininet.ipnet import IPNet
from ipmininet.iptopo import IPTopo

class Topo(IPTopo):

    def build(self, *args, **kwargs):

        #Hosts
        h0 = self.addRouter('h0')
        h1 = self.addRouter('h1')
        h2 = self.addRouter('h2')
        h3 = self.addRouter('h3')

        #Links
        self.addLink(h0, h2, igp_metric=1000, delay="5ms")
        self.addLink(h1, h2, igp_metric=1000, delay="5ms")
        self.addLink(h2, h3, igp_metric=1000, delay="5ms")

        super(Topo, self).build(*args, **kwargs)

def perfTest():

    print("*** Waiting for network to start")
    for i in range(60,0,-1):
        print(f"{i}  ", end="\r", flush=True)
        time.sleep(1) 

    print("*** Testing bandwidth between hosts")
    
    h0 = net.routers[0]
    h1 = net.routers[1]
    h3 = net.routers[3]

    h3.cmd('iperf3 -s -p 5000 &')
    h3.cmd('iperf3 -s -p 5001 &')
    h0.cmd('iperf3 -c h3 -p 5000 -t 30 --logfile experiments/results/limitation-h0-h3.json &')
    h1.cmd('iperf3 -c h3 -p 5001 -t 30 --logfile experiments/results/limitation-h1-h3.json &')
    
    for i in range(40,0,-1):
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
