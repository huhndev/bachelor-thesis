#!/bin/bash

apt update && apt install -y python-pip python3-pip virtualenv git quagga bridge-utils iperf3
pip3 install --upgrade git+https://github.com/cnp3/ipmininet.git@v1.1
usermod -a -G quaggavty root
virtualenv -p python3 venv/ipmininet
source venv/ipmininet/bin/activate
pip3 install --upgrade mininet
pip3 install --upgrade git+https://github.com/cnp3/ipmininet.git@v1.1
deactivate
virtualenv -p python3 venv/networkx
source venv/networkx/bin/activate
pip3 install --upgrade networkx
pip3 install --upgrade matplotlib
deactivate
