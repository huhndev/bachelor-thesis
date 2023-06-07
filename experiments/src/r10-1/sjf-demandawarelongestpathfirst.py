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
        self.addLink(h1, h9, igp_metric=985, bw=100, delay="5ms")
        self.addLink(h3, h7, igp_metric=985, bw=100, delay="5ms")
        self.addLink(h0, h6, igp_metric=985, bw=100, delay="5ms")
        self.addLink(h5, h8, igp_metric=985, bw=100, delay="5ms")

        # LongestPathFirst
        #self.addLink(h1, h3, igp_metric=985, bw=100, delay="5ms")
        #self.addLink(h0, h4, igp_metric=984, bw=100, delay="5ms")
        #self.addLink(h2, h5, igp_metric=983, bw=100, delay="5ms")
        #self.addLink(h6, h9, igp_metric=982, bw=100, delay="5ms")
        #self.addLink(h7, h8, igp_metric=981, bw=100, delay="5ms")

        # DemandFirst
        #self.addLink(h0, h8, igp_metric=980, bw=100, delay="5ms")
        #self.addLink(h1, h9, igp_metric=979, bw=100, delay="5ms")
        #self.addLink(h4, h7, igp_metric=978, bw=100, delay="5ms")

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

    h1.cmd('iperf3 -s -p 5009 &')
    h0.cmd('iperf3 -s -p 5006 &')
    h7.cmd('iperf3 -s -p 5004 &')
    h2.cmd('iperf3 -s -p 5009 &')
    h2.cmd('iperf3 -s -p 5008 &')
    h9.cmd('iperf3 -s -p 5001 &')
    h4.cmd('iperf3 -s -p 5005 &')
    h5.cmd('iperf3 -s -p 5008 &')
    h6.cmd('iperf3 -s -p 5001 &')
    h0.cmd('iperf3 -s -p 5008 &')
    h7.cmd('iperf3 -s -p 5004 &')
    h8.cmd('iperf3 -s -p 5000 &')
    h3.cmd('iperf3 -s -p 5007 &')
    h1.cmd('iperf3 -s -p 5009 &')
    h7.cmd('iperf3 -s -p 5000 &')
    h0.cmd('iperf3 -s -p 5007 &')
    h4.cmd('iperf3 -s -p 5003 &')
    h5.cmd('iperf3 -s -p 5007 &')
    h1.cmd('iperf3 -s -p 5003 &')
    h6.cmd('iperf3 -s -p 5000 &')

    h9.cmd('iperf3 -c h1 -p 5009 -n 63761K -J --logfile experiments/results/0-h9-h1-1.json &&'
           'iperf3 -c h2 -p 5009 -n 209025K -J --logfile experiments/results/0-h9-h2.json &&' 
           'iperf3 -c h1 -p 5009 -n 367893K -J --logfile experiments/results/0-h9-h1-2.json &')

    h7.cmd('iperf3 -c h3 -p 5007 -n 8342K -J --logfile experiments/results/0-h7-h3.json &&'
           'iperf3 -c h5 -p 5007 -n 47340K -J --logfile experiments/results/0-h7-h5.json &&'
           'iperf3 -c h0 -p 5007 -n 205313K -J --logfile experiments/results/0-h7-h0.json &')

    h6.cmd('iperf3 -c h0 -p 5006 -n 522374K -J --logfile experiments/results/0-h6-h0.json &')

    h4.cmd('iperf3 -c h7 -p 5004 -n 155699K -J --logfile experiments/results/0-h4-h7-2.json &&'
           'iperf3 -c h7 -p 5004 -n 346907K -J --logfile experiments/results/0-h4-h7-1.json &')

    h0.cmd('iperf3 -c h7 -p 5000 -n 120804K -J --logfile experiments/results/0-h0-h7.json &&'
           'iperf3 -c h6 -p 5000 -n 464581K -J --logfile experiments/results/0-h0-h6.json &&'
           'iperf3 -c h8 -p 5000 -n 724249K -J --logfile experiments/results/0-h0-h8.json &')

    h3.cmd('iperf3 -c h4 -p 5003 -n 64159K -J --logfile experiments/results/0-h3-h4.json &&'
           'iperf3 -c h1 -p 5003 -n 206732K -J --logfile experiments/results/0-h3-h1.json &')

    h8.cmd('iperf3 -c h0 -p 5008 -n 40866K -J --logfile experiments/results/0-h8-h0.json &&'
           'iperf3 -c h2 -p 5008 -n 80609K -J --logfile experiments/results/0-h8-h2.json &&'
           'iperf3 -c h5 -p 5008 -n 200853K -J --logfile experiments/results/0-h8-h5.json &')

    h1.cmd('iperf3 -c h6 -p 5001 -n 95747K -J --logfile experiments/results/0-h1-h6.json &&'
           'iperf3 -c h9 -p 5001 -n 177736K -J --logfile experiments/results/0-h1-h9.json &')

    h5.cmd('iperf3 -c h4 -p 5005 -n 950697K -J --logfile experiments/results/0-h5-h4.json &')

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
