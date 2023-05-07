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
        h4 = self.addRouter('h4')
        h5 = self.addRouter('h5')
        h6 = self.addRouter('h6')
        h7 = self.addRouter('h7')
        h8 = self.addRouter('h8')
        h9 = self.addRouter('h9')

        #Links
        self.addLink(h0, h4, igp_metric=100, bw=1000, delay="5ms")
        self.addLink(h0, h6, igp_metric=100, bw=1000, delay="5ms")
        self.addLink(h0, h8, igp_metric=100, bw=1000, delay="5ms")

        self.addLink(h1, h6, igp_metric=100, bw=1000, delay="5ms")
        self.addLink(h1, h8, igp_metric=100, bw=1000, delay="5ms")
        self.addLink(h1, h9, igp_metric=100, bw=1000, delay="5ms")

        self.addLink(h2, h4, igp_metric=100, bw=1000, delay="5ms")
        self.addLink(h2, h5, igp_metric=100, bw=1000, delay="5ms")
        self.addLink(h2, h7, igp_metric=100, bw=1000, delay="5ms")

        self.addLink(h3, h5, igp_metric=100, bw=1000, delay="5ms")
        self.addLink(h3, h6, igp_metric=100, bw=1000, delay="5ms")
        self.addLink(h3, h9, igp_metric=100, bw=1000, delay="5ms")

        self.addLink(h4, h7, igp_metric=100, bw=1000, delay="5ms")
	
        self.addLink(h5, h9, igp_metric=100, bw=1000, delay="5ms")

        self.addLink(h7, h8, igp_metric=100, bw=1000, delay="5ms")

        super(Topo, self).build(*args, **kwargs)

def perfTest():

    print("*** Waiting for network to start")
    for i in range(30,0,-1):
        print(f"{i}  ", end="\r", flush=True)
        time.sleep(1) 

    print("*** Testing bandwidth between hosts")
    
    h0 = net.routers[0]
    h1 = net.routers[1]
    h2 = net.routers[2]
    h3 = net.routers[3]
    h4 = net.routers[4]
    h5 = net.routers[5]
    h6 = net.routers[6]
    h7 = net.routers[7]
    h8 = net.routers[8]
    h9 = net.routers[9]

    h1.cmd('iperf3 -s -p 5002 &')
    h2.cmd('iperf3 -s -p 5003 &')
    h2.cmd('iperf3 -s -p 5006 &')
    h6.cmd('iperf3 -s -p 5008 &')
    h9.cmd('iperf3 -s -p 5002 &')
   
    time.sleep(2)
    h8.cmd('iperf3 -c h6 -p 5008 -J --logfile experiments/results/2-h8-h6.json &')
    time.sleep(3)
    h6.cmd('iperf3 -c h2 -p 5006 -J --logfile experiments/results/5-h6-h2.json &')
    time.sleep(1)
    h3.cmd('iperf3 -c h2 -p 5003 -J --logfile experiments/results/6-h3-h2.json &')
    time.sleep(1)
    h2.cmd('iperf3 -c h9 -p 5002 -J --logfile experiments/results/7-h2-h9.json &')
    time.sleep(2)
    h2.cmd('iperf3 -c h1 -p 5002 -J --logfile experiments/results/9-h2-h1.json &')

    for i in range(20,0,-1):
        print(f"{i}  ", end="\r", flush=True)
        time.sleep(1)


ipmininet.DEBUG_FLAG = True
lg.setLogLevel("info")

# Start network
net = IPNet(topo=Topo(), use_v6=False)
net.start()
perfTest()
#IPCLI(net)
net.stop()
