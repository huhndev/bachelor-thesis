#!/bin/bash
set -e

if [[ $# -ne 2 ]];
then
	echo "usage: $0 <EXPERIMENT> <SCHEDULING-ALGO>"
	exit 1
fi

EXPERIMENT=$1
SCHEDULING_ALGO=$2
LINK_ALGO=static

for i in {1..10};
do
	source ../venv/ipmininet/bin/activate
	python experiments/src/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO.py
	deactivate

	mkdir experiments/results/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO/run$i

	#source ../venv/networkx/bin/activate
	#python utils/visualize_results.py
	#python utils/visualize_results_table.py
	#python utils/visualize_results_table_per_node.py
	#deactivate

	#mv results_* experiments/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO/run$i/
	mv experiments/results/0-* experiments/results/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO/run$i/
done

LINK_ALGO=demandfirst

for i in {1..10};
do
        source ../venv/ipmininet/bin/activate
        python experiments/src/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO.py
        deactivate

        mkdir experiments/results/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO/run$i

        #source ../venv/networkx/bin/activate
        #python utils/visualize_results.py
        #python utils/visualize_results_table.py
        #python utils/visualize_results_table_per_node.py
        #deactivate

        #mv results_* experiments/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO/run$i/
        mv experiments/results/0-* experiments/results/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO/run$i/
done

LINK_ALGO=longestpathfirst

for i in {1..10};
do
        source ../venv/ipmininet/bin/activate
        python experiments/src/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO.py
        deactivate

        mkdir experiments/results/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO/run$i

        #source ../venv/networkx/bin/activate
        #python utils/visualize_results.py
        #python utils/visualize_results_table.py
        #python utils/visualize_results_table_per_node.py
        #deactivate

        #mv results_* experiments/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO/run$i/
        mv experiments/results/0-* experiments/results/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO/run$i/
done

LINK_ALGO=demandawarelongestpathfirst

for i in {1..10};
do
        source ../venv/ipmininet/bin/activate
        python experiments/src/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO.py
        deactivate

        mkdir experiments/results/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO/run$i

        #source ../venv/networkx/bin/activate
        #python utils/visualize_results.py
        #python utils/visualize_results_table.py
        #python utils/visualize_results_table_per_node.py
        #deactivate

        #mv results_* experiments/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO/run$i/
        mv experiments/results/0-* experiments/results/$EXPERIMENT/$SCHEDULING_ALGO-$LINK_ALGO/run$i/
done
