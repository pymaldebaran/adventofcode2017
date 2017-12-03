# author: Pierre-Yves Martin <pym.aldebaran@gmail.com>

.PHONY: docs
# A very good reference makefile https://github.com/requests/requests/blob/master/Makefile

# Launch all inexpensive tests
test:
	# Moving to the mincer module dir allows doctests to run properly
	pipenv run py.test --doctest-modules *.py

# Run all solutions
runall:
	pipenv run python december01.py
	pipenv run python december02.py
