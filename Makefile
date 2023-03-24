#########
# BUILD #
#########
develop:  ## install dependencies and build library
	python -m pip install -e .[develop] .[dependencies]

build:  ## build the python library
	python setup.py build build_ext --inplace

install:  ## install library
	python -m pip install .

#########
# LINTS #
#########
lint:  ## run static analysis with black and flake8

	python -m black --check Resume-Parser setup.py
	python -m flake8 Resume-Parser setup.py --ignore=E501,F401

# Alias
lints: lint

format:  ## run autoformatting with black
	python -m black Resume-Parser/ setup.py

# alias
fix: format

#########
# TESTS #
#########
test: ## clean and run unit tests
	python -m pytest -v Resume-Parser/test_all.py

coverage:  ## clean and run unit tests with coverage
	python -m pytest -v Resume-Parser/test_all.py --cov=Resume-Parser --cov-branch --cov-fail-under=50 --cov-report term-missing

# Alias
tests: test

###########
# VERSION #
###########
show-version:
	bump2version --dry-run --allow-dirty setup.py --list | grep current | awk -F= '{print $2}'

patch:
	bump2version patch

minor:
	bump2version minor

major:
	bump2version major

########
# DIST #
########
dist-build:  # Build python dist
	python setup.py sdist bdist_wheel

dist-check:
	python -m twine check dist/*

dist: clean build dist-build dist-check  ## Build dists

publish:  # Upload python assets
	echo "would usually run python -m twine upload dist/* --skip-existing"

#########
# CLEAN #
#########
deep-clean: ## clean everything from the repository
	git clean -fdx

clean: ## clean the repository
	rm -rf .coverage coverage cover htmlcov logs build dist *.egg-info .pytest_cache