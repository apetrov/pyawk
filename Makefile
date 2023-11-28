

test/awk:
	cat test/input.txt | awk -f test/wc.awk

test/python:
	cat test/input.txt | python test/wc.py

test/pyawk:
	cat test/input.txt | PYTHONPATH=$$(pwd) python -m pyawk test/wc_pyawk.py

test/all: test/awk test/python test/pyawk
	echo $@

test/sum:
	seq 1 10000 | PYTHONPATH=$$(pwd) python -m pyawk test/sum.py

install:
	pip install .
