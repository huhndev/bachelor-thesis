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
        self.addLink(h0, h2, igp_metric=1000, bw=100, delay="5ms")
        self.addLink(h0, h3, igp_metric=999, bw=100, delay="5ms")
        self.addLink(h0, h9, igp_metric=998, bw=100, delay="5ms")

        self.addLink(h1, h6, igp_metric=997, bw=100, delay="5ms")
        self.addLink(h1, h7, igp_metric=996, bw=100, delay="5ms")
        self.addLink(h1, h8, igp_metric=995, bw=100, delay="5ms")

        self.addLink(h2, h7, igp_metric=994, bw=100, delay="5ms")
        self.addLink(h2, h8, igp_metric=993, bw=100, delay="5ms")

        self.addLink(h3, h5, igp_metric=992, bw=100, delay="5ms")
        self.addLink(h3, h9, igp_metric=991, bw=100, delay="5ms")

        self.addLink(h4, h5, igp_metric=990, bw=100, delay="5ms")
        self.addLink(h4, h6, igp_metric=989, bw=100, delay="5ms")
        self.addLink(h4, h8, igp_metric=988, bw=100, delay="5ms")

        self.addLink(h5, h9, igp_metric=987, bw=100, delay="5ms")

        self.addLink(h6, h7, igp_metric=986, bw=100, delay="5ms")

	# DemandAwareLongestPathFirst
        #self.addLink(h1, h3, igp_metric=985, bw=100, delay="5ms")
        #self.addLink(h0, h6, igp_metric=984, bw=100, delay="5ms")
        #self.addLink(h2, h5, igp_metric=983, bw=100, delay="5ms")
        #self.addLink(h7, h9, igp_metric=982, bw=100, delay="5ms")

        # LongestPathFirst
        #self.addLink(h1, h3, igp_metric=985, bw=100, delay="5ms")
        #self.addLink(h0, h4, igp_metric=984, bw=100, delay="5ms")
        #self.addLink(h2, h5, igp_metric=983, bw=100, delay="5ms")
        #self.addLink(h6, h9, igp_metric=982, bw=100, delay="5ms")
        #self.addLink(h7, h8, igp_metric=981, bw=100, delay="5ms")

        # DemandFirst
        self.addLink(h3, h8, igp_metric=985, bw=100, delay="5ms")
        self.addLink(h6, h9, igp_metric=984, bw=100, delay="5ms")
        self.addLink(h5, h1, igp_metric=983, bw=100, delay="5ms")

        super(Topo, self).build(*args, **kwargs)

def perfTest():

    print("*** Waiting for network to start")
    for i in range(180,0,-1):
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

    h9.cmd('iperf3 -s -p 5004 &')
    h8.cmd('iperf3 -s -p 5000 &')
    h0.cmd('iperf3 -s -p 5008 &')
    h0.cmd('iperf3 -s -p 5006 &')
    h8.cmd('iperf3 -s -p 5005 &')
    h6.cmd('iperf3 -s -p 5009 &')
    h8.cmd('iperf3 -s -p 5006 &')
    h8.cmd('iperf3 -s -p 5003 &')
    h1.cmd('iperf3 -s -p 5003 &')
    h3.cmd('iperf3 -s -p 5000 &')
    h6.cmd('iperf3 -s -p 5008 &')
    h2.cmd('iperf3 -s -p 5003 &')
    h6.cmd('iperf3 -s -p 5008 &')
    h1.cmd('iperf3 -s -p 5005 &')
    h6.cmd('iperf3 -s -p 5007 &')
    h7.cmd('iperf3 -s -p 5006 &')
    h9.cmd('iperf3 -s -p 5007 &')
    h3.cmd('iperf3 -s -p 5001 &')
    h7.cmd('iperf3 -s -p 5005 &')
    h2.cmd('iperf3 -s -p 5005 &')

    h4.cmd('iperf3 -c h9 -p 5004 -n 59411.599609375K -J --logfile experiments/results/0-h4-h9.json &')

    h0.cmd('iperf3 -c h8 -p 5000 -n 65028.3095703125K -J --logfile experiments/results/0-h0-h8.json &&'
           'iperf3 -c h3 -p 5000 -n 81740.4833984375K -J --logfile experiments/results/0-h0-h3.json &')

    h8.cmd('iperf3 -c h6 -p 5008 -n 38879.85546875K -J --logfile experiments/results/0-h8-h6-1.json &&' 
           'iperf3 -c h0 -p 5008 -n 55369.248046875K -J --logfile experiments/results/0-h8-h0.json &&'
           'iperf3 -c h6 -p 5008 -n 515274.3154296875K -J --logfile experiments/results/0-h8-h6-2.json &')

    h6.cmd('iperf3 -c h0 -p 5006 -n 26633.32421875K -J --logfile experiments/results/0-h6-h0.json &&'
           'iperf3 -c h8 -p 5006 -n 251047.2119140625K -J --logfile experiments/results/0-h6-h8.json &&'
           'iperf3 -c h7 -p 5006 -n 368781.3291015625K -J --logfile experiments/results/0-h6-h7.json &')

    h5.cmd('iperf3 -c h7 -p 5005 -n 1334.365234375K -J --logfile experiments/results/0-h5-h7.json &&'
           'iperf3 -c h2 -p 5005 -n 42349.837890625K -J --logfile experiments/results/0-h5-h2.json &&'
           'iperf3 -c h8 -p 5005 -n 175363.046875K -J --logfile experiments/results/0-h5-h8.json &&'
           'iperf3 -c h1 -p 5005 -n 423625.2958984375K -J --logfile experiments/results/0-h5-h1.json &')

    h9.cmd('iperf3 -c h6 -p 5009 -n 482361.2451171875K -J --logfile experiments/results/0-h9-h6.json &')

    h3.cmd('iperf3 -c h1 -p 5003 -n 196211.390625K -J --logfile experiments/results/0-h3-h1.json &&'
           'iperf3 -c h2 -p 5003 -n 279417.1669921875K -J --logfile experiments/results/0-h3-h2.json &&'
           'iperf3 -c h8 -p 5003 -n 578916.17578125K -J --logfile experiments/results/0-h3-h8.json &')

    h7.cmd('iperf3 -c h6 -p 5007 -n 3289.5634765625K -J --logfile experiments/results/0-h7-h6.json &&'
           'iperf3 -c h9 -p 5007 -n 394213.576171875K -J --logfile experiments/results/0-h7-h9.json &')

    h1.cmd('iperf3 -c h3 -p 5001 -n 178071.1484375K -J --logfile experiments/results/0-h1-h3.json &')

    for i in range(300,0,-1):
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
