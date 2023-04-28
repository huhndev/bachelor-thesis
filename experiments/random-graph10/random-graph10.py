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

        #Routers
        ra = self.addRouter('ra')

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

    print("*** Waiting for network to start ***")
    for i in range(30,0,-1):
        print(f"{i}  ", end="\r", flush=True)
        time.sleep(1) 

    #print("*** Dumping switch connections")
    #dumpNodeConnections(net.switches)

    #print("*** Dumping host connections")
    #dumpNodeConnections(net.hosts)

    #print("*** Testing network connectivity")
    net.pingAll()

    print("*** Testing bandwidth between hosts")
    
    h1 = net.routers[0]
    h2 = net.routers[1]
    h3 = net.routers[2]
    h4 = net.routers[3]

    h1.cmd('iperf3 -s -p 5001 &')
    h1.cmd('iperf3 -s -p 5002 &')
    h1.cmd('iperf3 -s -p 5003 &')
    h2.cmd('iperf3 -c h1 -p 5001 -t 30 -O 10 > /root/results/example-h2.out &') #-J --logfile /root/results/example-h2.json &')
    h3.cmd('iperf3 -c h1 -p 5003 -t 30 -O 10 > /root/results/example-h3.out &') #-J --logfile /root/results/example-h3.json &')
    h4.cmd('iperf3 -c h1 -p 5002 -t 30 -O 10 > /root/results/example-h4.out &') #-J --logfile /root/results/example-h4.json &')  
    for i in range(50,0,-1):
        print(f"{i}  ", end="\r", flush=True)
        time.sleep(1)

ipmininet.DEBUG_FLAG = True
lg.setLogLevel("info")

# Start network
net = IPNet(topo=Topo(), use_v6=False)
net.start()
IPCLI(net)
#perfTest()
net.stop()
