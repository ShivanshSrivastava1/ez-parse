# Resume-Parser
A Python library that scrapes essential information from PDFs of LinkedIn profiles.

[![License: MIT](https://img.shields.io/badge/License-MIT-brightgreen.svg)](https://opensource.org/licenses/MIT)

![](https://img.shields.io/github/issues/ShivanshSrivastava1/Resume-Parser)

![](https://github.com/ShivanshSrivastava1/Resume-Parser/actions/workflows/build.yml/badge.svg)

[![codecov](https://codecov.io/github/ShivanshSrivastava1/Resume-Parser/branch/main/graph/badge.svg?token=V4IKQ490DY)](https://codecov.io/github/ShivanshSrivastava1/Resume-Parser)

[Project Board](https://github.com/users/ShivanshSrivastava1/projects/2/views/1)

## Overview
This is a parser that extracts important information from a LinkedIn profile PDF. It converts the PDF to a list of strings, and then uses LinkedIn's headers to create a dictionary that maps said headers to string values that contain the most relevant parts of a candidate's profile.

## Details
The following are commands included in the Makefile:
- `make develop`: install the library's dependencies using `pip`
- `make build`: perform static analysis of this library using `setuptools`
- `make lint`: perform static analysis of this library with `black` and `flake8`
- `make format`: autoformat this library with `black`
- `make test`: run automated tests with `pytest`
- `make coverage`: run automated tests with `pytest` and collect coverage information (passes with coverage >50%)
