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

	rm -f results_*.csv

	source ~/venv/networkx/bin/activate
	python ~/bachelor-thesis/utils/get_results_avg.py
        python ~/bachelor-thesis/utils/get_average_longest_completion_time.py
        python ~/bachelor-thesis/utils/get_average_transfer_completion_time.py
	deactivate	

	pwd
	cat results_*.csv

	cd ~/bachelor-thesis/
done

exit 0
