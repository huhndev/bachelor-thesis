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

        #Links
        self.addLink(h0, h1, igp_metric=1000, delay="5ms")

        super(Topo, self).build(*args, **kwargs)

def perfTest():

    print("*** Waiting for network to start")
    for i in range(60,0,-1):
        print(f"{i}  ", end="\r", flush=True)
        time.sleep(1) 

    print("*** Testing bandwidth between hosts")
    
    h0 = net.routers[0]
    h1 = net.routers[1]

    h1.cmd('iperf3 -s -p 5000 &')
    h0.cmd('iperf3 -c h1 -p 5000 -t 20 --logfile experiments/results/limitation-h0-h1-1.json &')
    
    for i in range(30,0,-1):
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
