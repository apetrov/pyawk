

test/awk:
	cat input.txt | awk -f wc.awk


test/python:
	cat input.txt | python wc.py


test/pyawk:
	cat input.txt | PYTHONPATH=$$(pwd) python -m pyawk pyawk.py

all: test/awk test/python test/pyawk
	echo $@
