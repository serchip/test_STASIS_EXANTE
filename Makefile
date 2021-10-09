CURRENT_DIRECTORY := $(shell pwd)

SERVICE = test-web
TEST_SERVICE = test-web

ifndef DC_FILE
	DC_FILE := docker-compose.yml
endif

DC_CMD = docker-compose -f ${DC_FILE}

ifndef DC_FILE_TEST
	DC_FILE_TEST := docker-compose.test.yml
endif

DC_CMD_TEST = docker-compose -f ${DC_FILE_TEST}


.PHONY: start stop status restart cli tail build pip-compile


help:
	@echo ""
	@echo "Please use \`make <target>' where <target> is one of"
	@echo ""
	@echo "  build              to make all docker assembly images"
	@echo "  test               to run tests"
	@echo "  migrate            to migrate"
	@echo "  pip-compile        to make pip-compile"
	@echo ""
	@echo "See contents of Makefile for more targets."

start:
	$(DC_CMD) up -d

start-up:
	$(DC_CMD) up

stop:
	$(DC_CMD) down

status:
	$(DC_CMD) ps

restart: stop start

cli:
	$(DC_CMD) exec $(SERVICE) bash

tail:
	$(DC_CMD) logs -f $(SERVICE)

build-nw:
	docker network create test_exante_default
build:
	$(DC_CMD) build

pip-compile:
	$(DC_CMD) run --rm --no-deps $(SERVICE) pip-compile
