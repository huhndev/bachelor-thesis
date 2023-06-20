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
        self.addLink(h0, h6, igp_metric=984, bw=100, delay="5ms")
        self.addLink(h3, h8, igp_metric=983, bw=100, delay="5ms")
        self.addLink(h2, h4, igp_metric=982, bw=100, delay="5ms")

        # LongestPathFirst
        #self.addLink(h1, h3, igp_metric=985, bw=100, delay="5ms")
        #self.addLink(h0, h4, igp_metric=984, bw=100, delay="5ms")
        #self.addLink(h2, h5, igp_metric=983, bw=100, delay="5ms")
        #self.addLink(h6, h9, igp_metric=982, bw=100, delay="5ms")
        #self.addLink(h7, h8, igp_metric=981, bw=100, delay="5ms")

        # DemandFirst
        #self.addLink(h1, h4, igp_metric=985, bw=100, delay="5ms")
	#self.addLink(h7, h8, igp_metric=984, bw=100, delay="5ms")
        #self.addLink(h2, h9, igp_metric=983, bw=100, delay="5ms")
        #self.addLink(h5, h6, igp_metric=982, bw=100, delay="5ms")

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

    h8.cmd('iperf3 -s -p 5001 &')
    h1.cmd('iperf3 -s -p 5002 &')
    h4.cmd('iperf3 -s -p 5006 &')
    h6.cmd('iperf3 -s -p 5004 &')
    h3.cmd('iperf3 -s -p 5008 &')
    h9.cmd('iperf3 -s -p 5001 &')
    h9.cmd('iperf3 -s -p 5003 &')
    h0.cmd('iperf3 -s -p 5008 &')
    h9.cmd('iperf3 -s -p 5002 &')
    h1.cmd('iperf3 -s -p 5008 &')
    h4.cmd('iperf3 -s -p 5001 &')
    h5.cmd('iperf3 -s -p 5006 &')
    h4.cmd('iperf3 -s -p 5002 &')
    h6.cmd('iperf3 -s -p 5000 &')
    h9.cmd('iperf3 -s -p 5007 &')
    h5.cmd('iperf3 -s -p 5006 &')
    h8.cmd('iperf3 -s -p 5007 &')
    h5.cmd('iperf3 -s -p 5000 &')
    h5.cmd('iperf3 -s -p 5008 &')
    h1.cmd('iperf3 -s -p 5002 &')

    h1.cmd('iperf3 -c h4 -p 5001 -n 592533.1123046875K -J --logfile experiments/results/0-h1-h4.json &&'
           'iperf3 -c h9 -p 5001 -n 286980.8603515625K -J --logfile experiments/results/0-h1-h9.json &&'
           'iperf3 -c h8 -p 5001 -n 32422.283203125K -J --logfile experiments/results/0-h1-h8.json &')

    h2.cmd('iperf3 -c h9 -p 5002 -n 336980.5869140625K -J --logfile experiments/results/0-h2-h9.json &&'
           'iperf3 -c h1 -p 5002 -n 196867.228515625K -J --logfile experiments/results/0-h2-h1-2.json &&'
           'iperf3 -c h1 -p 5002 -n 185067.421875K -J --logfile experiments/results/0-h2-h1-1.json &&'
           'iperf3 -c h4 -p 5002 -n 86290.9765625K -J --logfile experiments/results/0-h2-h4.json &')

    h6.cmd('iperf3 -c h5 -p 5006 -n 99798.6572265625K -J --logfile experiments/results/0-h6-h5-1.json &&'
           'iperf3 -c h5 -p 5006 -n 46221.17578125K -J --logfile experiments/results/0-h6-h5-2.json &&'
           'iperf3 -c h4 -p 5006 -n 2494.3603515625K -J --logfile experiments/results/0-h6-h4.json &')

    h4.cmd('iperf3 -c h6 -p 5004 -n 408371.7958984375K -J --logfile experiments/results/0-h4-h6.json &')

    h8.cmd('iperf3 -c h0 -p 5008 -n 435042.0390625K -J --logfile experiments/results/0-h8-h0.json &&'
           'iperf3 -c h1 -p 5008 -n 378866.173828125K -J --logfile experiments/results/0-h8-h1.json &&'
           'iperf3 -c h5 -p 5008 -n 143795.205078125K -J --logfile experiments/results/0-h8-h5.json &&'
           'iperf3 -c h3 -p 5008 -n 5229.1982421875K -J --logfile experiments/results/0-h8-h3.json &')

    h3.cmd('iperf3 -c h9 -p 5003 -n 102573.5185546875K -J --logfile experiments/results/0-h3-h9.json &')

    h0.cmd('iperf3 -c h5 -p 5000 -n 32718.517578125K -J --logfile experiments/results/0-h0-h5.json &&'
           'iperf3 -c h6 -p 5000 -n 16045.29296875K -J --logfile experiments/results/0-h0-h6.json &')

    h7.cmd('iperf3 -c h8 -p 5007 -n 574270.1748046875K -J --logfile experiments/results/0-h7-h8.json &&'
           'iperf3 -c h9 -p 5007 -n 83558.474609375K -J --logfile experiments/results/0-h7-h9.json &')

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
