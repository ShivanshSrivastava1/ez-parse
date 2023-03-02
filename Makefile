#########
# BUILD #
#########
develop:  ## install dependencies
	pip install -r requirements.txt

#########
# LINTS #
#########
lint:  ## run static analysis with black and flake8
	python -m black --check parser.py test_all.py
	python -m flake8 parser.py test_all.py

# Alias
lints: lint

format:  ## run autoformatting with black
	python -m black parser.py test_all.py

# alias
fix: format

#########
# TESTS #
#########
test: ## clean and run unit tests
	python -m pytest -v test_all.py

coverage:  ## clean and run unit tests with coverage
	python -m pytest -v test_all.py --cov=parser --cov-branch --cov-fail-under=50 --cov-report term-missing

# Alias
tests: test
