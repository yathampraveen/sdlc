# Prerequsite (for local development)
* Install python3.7, mysql 5.7

# Setting up local environment
## Setup virtualenv
* Install virtualenv and virtualenvwrapper (`pip install virtualenv, virtualenvwrapper`)
* Setup virtualenvwrapper
* * Add environment variable: WORKON_HOME in bashrc file.
* * * `export WORKON_HOME=\<prefered-place-to-store-virtualenvs\>` `ex: ~/.Env`
* * Add below command in bashrc file:
* * * `source /usr/local/bin/virtualenvwrapper.sh`
* * Reload basrc file: `source ~/.bashrc`
* * Execute command: `mkdir -p $WORKON_HOME`
* * Create virtualenv called consolidation_svc with python 3.6
* * * `mkvirtualenv -p <path-to-python3.6> consolidation_svc `
* * Change work environment to consolidation_svc: `workon consolidation_svc`
## Install requirements:
`pip install -r requirements/local.txt`
## Github setup
* * Copy github hooks present in dir: git_hooks into .git/hooks folder
* * run pre-commit install (this will install precommit hook)
## Start server
* runserver in 9000 port (as port 8000 will be used for monolithic)
## Ready to go
## Running tests
* * cd to the project root folder
* * set PYTHONPATH to the <path-to-consolidation-svc>/consolidation_svc/consolidation_svc/
* * run command: `pytest`
* * This will run all the tests and generate coverage report in folder: `htmlcov`
* * open index.html file (in browser) present inside htmlcov to open the coverage report.

# Permission handling
## Steps to upload permissions in monolithic
* Execute below command in consolidation svc to print permissions for app or model
./manage.py monolithic_permissions --app-label <app-label> - Prints permissions for given app
./manage.py monolithic_permissions --model-name warehousetriggertimings - Prints permissions for given model
* Copy lines printed by above command into xls sheet
* Upload this xls in monolithic: /admin/microservices/upload-urls-permissions/
## Steps to associate consolidation svc permissions to group/user
* Create xls sheet with permission name in 1st column that needs to be associated to group
* Execute below command in monolithic to associate permissions to given group
/manage.py group_user_permission_add_update --groupname <group-name>  --filepath <permission-file-path.xls>

# Docker
* Docker build local
Command: docker build -f compose/docker/production/Dockerfile --no-cache --build-arg GITHUB_USERNAME=bbsuper
--build-arg GITHUB_PERSONAL_ACCESS_TOKEN=<> -t 274334742953.dkr.ecr.ap-south-1.amazonaws.com/bb-engg/consolidation:3.7 .

# Release versions
* Production is running in version: v1.6.0 (all services)
