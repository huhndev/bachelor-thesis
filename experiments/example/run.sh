#!/bin/bash

echo +++ Clean up workspace +++
rm /root/results/example*
rm /root/results/visualization.png

echo +++ Starting Network Test +++
python3 /root/ipmininet/example/example.py
echo done.
echo

echo +++ Visualize results +++
python3 /root/iperf3Vis/src/run.py --data-directory /root/results --output /root/results/visualization.png --time-interval 30s
echo Results can be found in: /root/results/
echo
