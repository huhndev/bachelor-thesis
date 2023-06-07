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
        h10 = self.addRouter('h10')
        h11 = self.addRouter('h11')
        h12 = self.addRouter('h12')
        h13 = self.addRouter('h13')
        h14 = self.addRouter('h14')
        h15 = self.addRouter('h15')
        h16 = self.addRouter('h16')
        h17 = self.addRouter('h17')
        h18 = self.addRouter('h18')
        h19 = self.addRouter('h19')

        #Links
        self.addLink(h0, h5, igp_metric=1000, bw=100, delay="5ms")
        self.addLink(h0, h7, igp_metric=999, bw=100, delay="5ms")
        self.addLink(h0, h14, igp_metric=998, bw=100, delay="5ms")

        self.addLink(h1, h12, igp_metric=997, bw=100, delay="5ms")
        self.addLink(h1, h14, igp_metric=996, bw=100, delay="5ms")
        self.addLink(h1, h15, igp_metric=995, bw=100, delay="5ms")

        self.addLink(h2, h3, igp_metric=994, bw=100, delay="5ms")
        self.addLink(h2, h9, igp_metric=993, bw=100, delay="5ms")
        self.addLink(h2, h16, igp_metric=992, bw=100, delay="5ms")

        self.addLink(h3, h10, igp_metric=991, bw=100, delay="5ms")
        self.addLink(h3, h13, igp_metric=990, bw=100, delay="5ms")

        self.addLink(h4, h7, igp_metric=989, bw=100, delay="5ms")
        self.addLink(h4, h8, igp_metric=988, bw=100, delay="5ms")
        self.addLink(h4, h9, igp_metric=987, bw=100, delay="5ms")

        self.addLink(h5, h6, igp_metric=986, bw=100, delay="5ms")
        self.addLink(h5, h7, igp_metric=985, bw=100, delay="5ms")

        self.addLink(h6, h11, igp_metric=984, bw=100, delay="5ms")
        self.addLink(h6, h18, igp_metric=983, bw=100, delay="5ms")

        self.addLink(h8, h16, igp_metric=982, bw=100, delay="5ms")
        self.addLink(h8, h18, igp_metric=981, bw=100, delay="5ms")

        self.addLink(h9, h17, igp_metric=980, bw=100, delay="5ms")

        self.addLink(h10, h12, igp_metric=979, bw=100, delay="5ms")
        self.addLink(h10, h17, igp_metric=978, bw=100, delay="5ms")

        self.addLink(h11, h13, igp_metric=977, bw=100, delay="5ms")
        self.addLink(h11, h15, igp_metric=976, bw=100, delay="5ms")

        self.addLink(h12, h19, igp_metric=975, bw=100, delay="5ms")

        self.addLink(h13, h19, igp_metric=974, bw=100, delay="5ms")

        self.addLink(h14, h16, igp_metric=973, bw=100, delay="5ms")

        self.addLink(h15, h17, igp_metric=972, bw=100, delay="5ms")

        self.addLink(h18, h19, igp_metric=971, bw=100, delay="5ms")

	# DemandAwareLongestPathFirst
        self.addLink(h5, h10, igp_metric=970, bw=100, delay="5ms")
        self.addLink(h2, h6, igp_metric=969, bw=100, delay="5ms")
        self.addLink(h9, h19, igp_metric=968, bw=100, delay="5ms")
        self.addLink(h0, h17, igp_metric=967, bw=100, delay="5ms")
        self.addLink(h1, h13, igp_metric=966, bw=100, delay="5ms")
        self.addLink(h3, h7, igp_metric=965, bw=100, delay="5ms")
        self.addLink(h8, h12, igp_metric=964, bw=100, delay="5ms")
        self.addLink(h9, h11, igp_metric=963, bw=100, delay="5ms")
        self.addLink(h14, h18, igp_metric=962, bw=100, delay="5ms")
        self.addLink(h4, h16, igp_metric=961, bw=100, delay="5ms")

        # LongestPathFirst
        #self.addLink(h5, h10, igp_metric=970, bw=100, delay="5ms") 
        #self.addLink(h0, h13, igp_metric=969, bw=100, delay="5ms")
        #self.addLink(h1, h4, igp_metric=968, bw=100, delay="5ms")
        #self.addLink(h2, h6, igp_metric=967, bw=100, delay="5ms")
        #self.addLink(h9, h19, igp_metric=966, bw=100, delay="5ms")
        #self.addLink(h3, h7, igp_metric=965, bw=100, delay="5ms")
        #self.addLink(h8, h11, igp_metric=964, bw=100, delay="5ms")
        #self.addLink(h12, h16, igp_metric=963, bw=100, delay="5ms")
        #self.addLink(h14, h17, igp_metric=962, bw=100, delay="5ms")
        #self.addLink(h15, h18, igp_metric=961, bw=100, delay="5ms")

        # DemandFirst
        #self.addLink(h9, h10, igp_metric=970, bw=100, delay="5ms")
        #self.addLink(h2, h12, igp_metric=969, bw=100, delay="5ms")
        #self.addLink(h4, h16, igp_metric=968, bw=100, delay="5ms")
        #self.addLink(h13, h18, igp_metric=967, bw=100, delay="5ms")
        #self.addLink(h5, h0, igp_metric=966, bw=100, delay="5ms")
        #self.addLink(h1, h8, igp_metric=965, bw=100, delay="5ms")
        #self.addLink(h3, h15, igp_metric=964, bw=100, delay="5ms")
        #self.addLink(h6, h17, igp_metric=963, bw=100, delay="5ms")

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
    h10 = net.routers[10]
    h11 = net.routers[11]
    h12 = net.routers[12]
    h13 = net.routers[13]
    h14 = net.routers[14]
    h15 = net.routers[15]
    h16 = net.routers[16]
    h17 = net.routers[17]
    h18 = net.routers[18]
    h19 = net.routers[19]

    h18.cmd('iperf3 -s -p 5012 &')
    h5.cmd('iperf3 -s -p 5010 &')
    h2.cmd('iperf3 -s -p 5001 &')
    h9.cmd('iperf3 -s -p 5008 &')
    h3.cmd('iperf3 -s -p 5007 &')
    h14.cmd('iperf3 -s -p 5018 &')
    h19.cmd('iperf3 -s -p 5009 &')
    h2.cmd('iperf3 -s -p 5006 &')
    h10.cmd('iperf3 -s -p 5005 &')
    h16.cmd('iperf3 -s -p 5002 &')
    h5.cmd('iperf3 -s -p 5019 &')
    h3.cmd('iperf3 -s -p 5015 &')
    h13.cmd('iperf3 -s -p 5001 &')
    h13.cmd('iperf3 -s -p 5011 &')
    h1.cmd('iperf3 -s -p 5008 &')
    h8.cmd('iperf3 -s -p 5014 &')
    h15.cmd('iperf3 -s -p 5017 &')
    h17.cmd('iperf3 -s -p 5000 &')
    h0.cmd('iperf3 -s -p 5010 &')
    h12.cmd('iperf3 -s -p 5014 &')
    h18.cmd('iperf3 -s -p 5017 &')
    h12.cmd('iperf3 -s -p 5002 &')
    h4.cmd('iperf3 -s -p 5000 &')
    h19.cmd('iperf3 -s -p 5013 &')
    h10.cmd('iperf3 -s -p 5017 &')
    h4.cmd('iperf3 -s -p 5019 &')
    h9.cmd('iperf3 -s -p 5007 &')
    h7.cmd('iperf3 -s -p 5010 &')
    h6.cmd('iperf3 -s -p 5012 &')
    h9.cmd('iperf3 -s -p 5011 &')
    h4.cmd('iperf3 -s -p 5013 &')
    h13.cmd('iperf3 -s -p 5018 &')
    h10.cmd('iperf3 -s -p 5009 &')
    h17.cmd('iperf3 -s -p 5006 &')
    h12.cmd('iperf3 -s -p 5006 &')
    h12.cmd('iperf3 -s -p 5008 &')
    h10.cmd('iperf3 -s -p 5005 &')
    h0.cmd('iperf3 -s -p 5004 &')
    h0.cmd('iperf3 -s -p 5005 &')
    h16.cmd('iperf3 -s -p 5004 &')

    h12.cmd('iperf3 -c h6 -p 5012 -n 247517.658203125K -J --logfile experiments/results/0-h12-h6.json &&'
            'iperf3 -c h18 -p 5012 -n 104094.708984375K -J --logfile experiments/results/0-h12-h18.json &')

    h10.cmd('iperf3 -c h5 -p 5010 -n 145548.6259765625K -J --logfile experiments/results/0-h10-h5.json &&'
            'iperf3 -c h0 -p 5010 -n 109112.1171875K -J --logfile experiments/results/0-h10-h0.json &&'
            'iperf3 -c h7 -p 5010 -n 34508.13671875K -J --logfile experiments/results/0-h10-h7.json &')

    h1.cmd('iperf3 -c h2 -p 5001 -n 14154.220703125K -J --logfile experiments/results/0-h1-h2.json &&'
           'iperf3 -c h13 -p 5001 -n 11606.609375K -J --logfile experiments/results/0-h1-h13.json &')

    h8.cmd('iperf3 -c h1 -p 5008 -n 175584.7939453125K -J --logfile experiments/results/0-h8-h1.json &&'
           'iperf3 -c h12 -p 5008 -n 143349.6455078125K -J --logfile experiments/results/0-h8-h12.json &&'
           'iperf3 -c h9 -p 5008 -n 91448.19140625K -J --logfile experiments/results/0-h8-h9.json &')

    h7.cmd('iperf3 -c h3 -p 5007 -n 45271.6318359375K -J --logfile experiments/results/0-h7-h3.json &')

    h18.cmd('iperf3 -c h13 -p 5018 -n 379406.66796875K -J --logfile experiments/results/0-h18-h13.json &&'
            'iperf3 -c h14 -p 5018 -n 36478.6923828125K -J --logfile experiments/results/0-h18-h14.json &')

    h9.cmd('iperf3 -c h10 -p 5009 -n 849768.4794921875K -J --logfile experiments/results/0-h9-h10.json &&'
           'iperf3 -c h19 -p 5009 -n 84280.2431640625K -J --logfile experiments/results/0-h9-h19.json &')

    h6.cmd('iperf3 -c h12 -p 5006 -n 140983.2392578125K -J --logfile experiments/results/0-h6-h12.json &&'
           'iperf3 -c h2 -p 5006 -n 120456.796875K -J --logfile experiments/results/0-h6-h2.json &&'
           'iperf3 -c h17 -p 5006 -n 6583.8173828125K -J --logfile experiments/results/0-h6-h17.json &')

    h5.cmd('iperf3 -c h0 -p 5005 -n 269865.0224609375K -J --logfile experiments/results/0-h5-h0.json &&'
           'iperf3 -c h10 -p 5005 -n 56637.541015625K -J --logfile experiments/results/0-h5-h10-2.json &&'
           'iperf3 -c h10 -p 5005 -n 36095.109375K -J --logfile experiments/results/0-h5-h10-1.json &')

    h2.cmd('iperf3 -c h12 -p 5002 -n 522691.72265625K -J --logfile experiments/results/0-h2-h12.json &&'
           'iperf3 -c h16 -p 5002 -n 56263.478515625K -J --logfile experiments/results/0-h2-h16.json &')

    h19.cmd('iperf3 -c h4 -p 5019 -n 24746.3544921875K -J --logfile experiments/results/0-h19-h4.json &&'
            'iperf3 -c h5 -p 5019 -n 22339.6708984375K -J --logfile experiments/results/0-h19-h5.json &')

    h15.cmd('iperf3 -c h3 -p 5015 -n 93375.5908203125K -J --logfile experiments/results/0-h15-h3.json &')

    h11.cmd('iperf3 -c h9 -p 5011 -n 242922.939453125K -J --logfile experiments/results/0-h11-h9.json &&'
            'iperf3 -c h13 -p 5011 -n 95982.341796875K -J --logfile experiments/results/0-h11-h13.json &')

    h14.cmd('iperf3 -c h12 -p 5014 -n 387582.615234375K -J --logfile experiments/results/0-h14-h12.json &&'
            'iperf3 -c h8 -p 5014 -n 127276.6669921875K -J --logfile experiments/results/0-h14-h8.json &')

    h17.cmd('iperf3 -c h10 -p 5017 -n 612767.6298828125K -J --logfile experiments/results/0-h17-h10.json &&'
            'iperf3 -c h15 -p 5017 -n 91837.056640625K -J --logfile experiments/results/0-h17-h15.json &&'
            'iperf3 -c h18 -p 5017 -n 62212.1416015625K -J --logfile experiments/results/0-h17-h18.json &')

    h0.cmd('iperf3 -c h17 -p 5000 -n 142272.03125K -J --logfile experiments/results/0-h0-h17.json &&'
           'iperf3 -c h4 -p 5000 -n 57444.865234375K -J --logfile experiments/results/0-h0-h4.json &')

    h13.cmd('iperf3 -c h19 -p 5013 -n 350867.173828125K -J --logfile experiments/results/0-h13-h19.json &&'
            'iperf3 -c h4 -p 5013 -n 118510.6416015625K -J --logfile experiments/results/0-h13-h4.json &')

    h7.cmd('iperf3 -c h9 -p 5007 -n 292507.5322265625K -J --logfile experiments/results/0-h7-h9.json &')

    h4.cmd('iperf3 -c h16 -p 5004 -n 406852.98046875K -J --logfile experiments/results/0-h4-h16.json &&'
           'iperf3 -c h0 -p 5004 -n 33156.5595703125K -J --logfile experiments/results/0-h4-h0.json &')

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
