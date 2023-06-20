#!/bin/bash
set -e

for experiment in experiments/results/*/
do
	for variation in $experiment*/
        do
		echo +++ $experiment +++
                echo + ${variation#*/*} +
		echo avg speed
		tail -n 1 $variation/results_avg.csv
		echo avg longest completion time
		tail -n 1 $variation/results_average_longest_completion_time.csv
		echo avg transfer completion time
		tail -n 1 $variation/results_average_transfer_completion_time.csv
	done
done
