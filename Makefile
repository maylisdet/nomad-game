.DEFAULT_GOAL := help
SHELL := /bin/bash

bold := $(shell tput bold)
end := $(shell tput sgr0)\033[0m
green := \033[0;32m
red := \033[0;31m
bold_red := $(red)$(bold)
bold_green := $(green)$(bold)


.PHONY: create_venv
create_venv:
	@if [ ! -d env ]; then \
		python3 -m venv env; \
	fi;


.PHONY: help
help:
	@printf "$(bold_green)make$(end): prints this help. Equivalent to $(bold_green)make help$(end).\n"
	@printf "$(bold_green)make format$(end): Formats the code using black.\n"
	@printf "$(bold_green)make check_format$(end): Returns 0 if everything is formatted properly, 1 otherwise.\n"
	@printf "$(bold_green)make mypy$(end): Executes mypy'static analysis.\n"
	@printf "$(bold_green)make test$(end): Executes unit tests.\n"
	@printf "$(bold_green)make coverage$(end): Executes unit tests and prints the current coverage.\n"
	@printf "$(bold_green)make install$(end): Forces the pip install of the project.\n"
	@printf "$(bold_red)make clean$(end): Deletes the venv and dependencies.\n"

.PHONY: update
update: create_venv
	@if [ ! -f env/update ]; \
	then \
		source ./env/bin/activate && \
		./env/bin/pip install -q --upgrade pip && \
		./env/bin/pip install -q -e . && \
		touch ./env/update; \
	elif [ `stat -c %Y requirements.txt` -gt `stat -c %Y ./env/update` ]; \
	then \
		source ./env/bin/activate && \
		./env/bin/pip install -q --upgrade pip && \
		./env/bin/pip install -q -e . && \
		touch ./env/update; \
	fi;


.PHONY: install
install: create_venv
	@source ./env/bin/activate && \
	./env/bin/pip install -q --upgrade pip && \
	./env/bin/pip install -q -e . && \
	touch ./env/update && \
	./env/bin/pre-commit install


.PHONY: test
test: update
	@source ./env/bin/activate && \
	./env/bin/pytest

.PHONY: coverage
coverage: update
	@source ./env/bin/activate && \
	./env/bin/coverage run -m pytest && \
	./env/bin/coverage report

.PHONY: format
format: update
	@source ./env/bin/activate && \
	./env/bin/python -m black src


.PHONY: mypy
mypy: update
	@source ./env/bin/activate && \
	./env/bin/mypy --ignore-missing-imports --install-types --non-interactive src/algorithms && \
	./env/bin/mypy --ignore-missing-imports --install-types --non-interactive src/client && \
	./env/bin/mypy --ignore-missing-imports --install-types --non-interactive src/common && \
	./env/bin/mypy --ignore-missing-imports --install-types --non-interactive src/config && \
	./env/bin/mypy --ignore-missing-imports --install-types --non-interactive src/server;

.PHONY: clean
clean:
	@find src/ -type d -name __pycache__ -prune -exec rm -r {} \;
	@find src/ -type d -name *.egg-info -prune -exec rm -r {} \;
	@rm -rf ./build ./env ./stubs

.PHONY: check_format
check_format:
	@source ./env/bin/activate && \
	./env/bin/python -m black --check src
