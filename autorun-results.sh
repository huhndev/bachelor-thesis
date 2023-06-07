#!/bin/bash
set -e

if [[ $# -ne 1 ]];
then
        echo "usage: $0 <EXPERIMENT>"
        exit 1
fi

EXPERIMENT=$1

for dir in experiments/results/$EXPERIMENT/*/
do
	cd $dir

	rm results_avg.csv

	source ~/venv/networkx/bin/activate
	python ~/bachelor-thesis/utils/get_results_avg.py
	deactivate	

	pwd
	cat results_avg.csv

	cd ~/bachelor-thesis/
done

exit 0
