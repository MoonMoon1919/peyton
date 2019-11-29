SHELL := /bin/bash
CWD := $(shell pwd)
GIT_SHA := `git rev-parse --short HEAD`
REQ_CHECK_CMD := pipenv run pip check
SAFETY_CHECK_CMD := safety check --full-report
BLACK_SET_CMD := black .

sha:
	@echo $(GIT_SHA)

format:
	@$(BLACK_SET_CMD)

check/reqs:
	@$(REQ_CHECK_CMD)

check/safety:
	@$(SAFETY_CHECK_CMD)
