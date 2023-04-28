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

ipmininet.DEBUG_FLAG = True
lg.setLogLevel("info")

# Start network
net = IPNet(topo=Topo(), use_v6=False)
net.start()
IPCLI(net)
net.stop()
