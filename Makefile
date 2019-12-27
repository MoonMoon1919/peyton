SHELL := /bin/bash
CWD := $(shell pwd)
GIT_SHA := `git rev-parse --short HEAD`
REQ_CHECK_CMD := pipenv run pip check
SAFETY_CHECK_CMD := safety check --full-report
BLACK_SET_CMD := black .
TEST_CMD := pytest tests/
DOCKER_BUILD_CMD := docker build
DOCKER_RUN_CMD := docker run
IMAGE_NAME := peyton_test

sha:
	@echo $(GIT_SHA)

format:
	@$(BLACK_SET_CMD)

check/reqs:
	@$(REQ_CHECK_CMD)

check/safety:
	@$(SAFETY_CHECK_CMD)

test:
	@$(TEST_CMD)

build/test/image:
	@$(DOCKER_BUILD_CMD) . -t $(IMAGE_NAME):$(GIT_SHA)

run/test/image: build/test/image
	@$(DOCKER_RUN_CMD) $(IMAGE_NAME):$(GIT_SHA) $(TEST_CMD)
