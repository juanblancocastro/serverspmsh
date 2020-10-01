#!/usr/bin/env bash

clear

ENVIRONMENT=".venv"
PROJECT_PATH=$(dirname "$(realpath "$0")")
ENVIRONMENT_PATH=${PROJECT_PATH}/${ENVIRONMENT}

git -C "${PROJECT_PATH}" pull

export PIPENV_VENV_IN_PROJECT=1 PIPENV_IGNORE_VIRTUALENVS=1 && python3 -m pipenv sync