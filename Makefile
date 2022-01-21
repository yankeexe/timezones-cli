SHELL :=/bin/bash
CWD := $(PWD)
TMP_PATH := $(CWD)/.tmp
VENV_PATH := $(CWD)/venv
docker_image := timezones-cli

.PHONY: test clean build
.DEFAULT_GOAL=help

build:
	@docker build -t $(docker_image) .

build.if:
	@if [ "$$(docker images -q $(docker_image) 2> /dev/null)" = "" ]; then \
		$(MAKE) -s build; \
	fi

run: build.if
	@docker run --rm -it -v ${HOME}/.tz-cli:/home/tz/.tz-cli timezones-cli $(cmd)

clean: # Clean temporary files
	@rm -rf $(TMP_PATH) __pycache__ .pytest_cache
	@find . -name '*.pyc' -delete
	@find . -name '__pycache__' -delete
	@rm -rf build dist

test: # Run pytest
	@pytest -vvv

venv: # Create a virtual environment
	@python3 -m venv venv

format: # Format using black
	@black .

check: # Check for formatting issues using black
	@black --check --diff .

setup: # Setup local development
	@pip install -e .[dev]

help: # Show this help
	@egrep -h '\s#\s' $(MAKEFILE_LIST) | sort | awk 'BEGIN {FS = ":.*?# "}; {printf "\033[36m%-20s\033[0m %s\n", $$1, $$2}'
