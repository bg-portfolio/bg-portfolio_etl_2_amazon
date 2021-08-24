# Table of Contents:

- [Table of Contents](#table-of-contents)
- [Overview](#overview)
    - [Project Schema](#project-schema)
    - [About](#about)
- [Docs](#docs)
    - [Instalation](#instalation)
    - [Getting Started](#getting-started)
        - [Settings](#settings)
        - [Project Ports](#project-ports)
- [TODO](#todo)
    - [Fix](#fix)
- [Technical Requirements](#technical-requirements)
- [License](#license)


---
# Overview

This is fully implemented [amazon shop](https://www.amazon.com/) ETL pipeline. Extraction is through web scraping program using [selenium](https://github.com/SeleniumHQ/selenium) and [beautiful soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/). Transformation implemented through [pandas](https://pandas.pydata.org/) and pys' dictionaries. Loading data into [MongoDB](https://www.mongodb.com/). ETL is orchestrated in [Airflow](https://airflow.apache.org/) using postgres, selenium is using remote selenium grid server, mongo has GUI in form of [mongo-express](https://github.com/mongo-express/mongo-express). Business graphs are available in a [streamlit](https://streamlit.io/) Dashboard.
Everything is deployed in [Docker](https://www.docker.com/) compose.

## Project Schema

Technological stack: Python 3.8+, Airflow 2+, Docker-compose file 3.8, mongodb 5+

directory schema:
```
.
├── Dockerfile-dashboard
├── LICENSE
├── README.md
├── app
│   ├── main.py
│   ├── requirements.txt
│   └── utils
│       ├── __init__.py
│       ├── graph_controls.py
│       ├── image_export.py
│       ├── layout.py
│       └── processing.py
├── dags
│   ├── __init__.py
│   ├── dummy_dag.py
│   ├── programs
│   │   ├── __init__.py
│   │   └── ws_amazon
│   │       ├── __init__.py
│   │       ├── requirements.txt
│   │       ├── utils
│   │       │   ├── amazon_shop.py
│   │       │   ├── inputs.py
│   │       │   └── processing.py
│   │       ├── ws_amazon.py
│   │       └── ws_amazon.yaml
│   └── ws_amazon_dag.py
├── docker-compose.yml
├── init.sh
├── other
│   └── diagram.png
├── logs
├── plugins
├── requirements.txt
├── scripts
│   └── entrypoint.sh
└── tests
    ├── __init__.py
    ├── database.py
    ├── dummy_test.py
    ├── integration.py
    ├── unit_dashboard.py
    └── unit_scraper.py
```

Project schema:

![Alt Text](../main/other/diagram.png?raw=true "diagram")


## About

This is as fully functional ETL pipeline as work in progress. I wanted to learn docker, had an old script from one of the web scraping jobs and I decided that I'll repurpose it into ETL. 
I wanted to create something bigger with couple of phases, use more advanced technologies than just simple ETL script that downloads the data and writes it into a database. Because I used couple of tools for the first time, there are places where, for example, configurations for docker containers in docker compose file are not following the same schema. How envs are invoked, how commands are run, different ways to set up the neccessary framework, all of that is mixed. I've wanted to explore couple of ways, of possibilities to learn how it can be set up. In future projects I'll follow more standarised way of doing them.
I might even clean this project up to some project management standard. Right now all of the elements that I've envisioned while architecting the ETL structure, are tested, implemented and fully working. Web scraping script, downloading the data from amazon shop, proceeding with basic transformations and loading the data into database. Orchestrating it in Airflow, visualising the data on the dashboard. Everything run in docker, each process having its own container or couple of them when it comes to Airflow.  
While building the project, some new features/implementations seemed natural to use, like mongo-express for GUI or seleniums' grid server. Another thing I've noticed is to set up CI quite early in the process, to leverage testing/deployment and building of the containers to save time and better ease of life.
I hope you like it.


---
# Docs

## Instalation

This is implicitly assumed that newest [docker](https://docs.docker.com/get-docker/) and [docker compose](https://docs.docker.com/compose/install/) are installed and operational. If not, please continue with their respective instalation guides.

Download or clone the repository and in the main repository' folder, where docker-compose.yml is located, open terminal and run:
`docker-compose up`
It will take around 2-5 minutes for all the containers to launch and install dependencies, not counting downloading and building the images.

Once that is done, open new terminal and run init.sh script to set up airflow users.
`./init.sh`
or do it manually by opening CLI inside the container of airflow webserver or scheduler, and run `airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin`

When that is done, open [localhost:8080](https://localhost:8080/) and sign into Airflow Webserver using credentials:
`login:admin password:admin`

In the main Airflow dashboard, turn on the Amazon_ETL, it should start the dag automatically. If not, trigger it manually.

Proceed into dags' log to view the progress (have to refresh the site for updates).

Once the entries are downloaded and saved in db, open [Dashboard](https://localhost:8501/) and use the charts.


## Getting Started

### Settings

Mongo-express: `login:admin password:admin`
Airflow webserver: `login:admin password:admin`

Change web scraping parameters in yaml file at: `./dags/programs/ws_amazon/ws_amazon.yaml`

Amazon scraping dag is set to trigger once a day.


### Project Ports

This project is deployed in local network.
- 8080: [Airflow Webserver](https://localhost:8080/)
- 8793: Airflow Scheduler
- 4444: Selenium grid, 4444/wd/hub for instance access
- ~~7900: Selenium noVNC~~
- 8081: [Mongo-express](https://localhost:8081/)
- 27017: MongoDB
- 8501: [Dashboard](https://localhost:8501/)


---
# TODO

- how to manage dependencies in airflow, venv for each dag?
- clean configs, remove hard coded configs, use ENV_VARS
- add authentication/security/user layer, use ENV_VARS
- split amazon dag into multiple steps
- add tests
- add CI
- write documentation
- trim the images, build custom ones for light weight
- add propper logging with logging module
- add DB operations, backups etc.
- add monitoring tool for docker containers
- update selenium grid into 4.0 for noVNC, container check/run control
- further clean the legacy web scraping script
- add healthchecks for postgres, scheduler, selenium, dashboard
- faulty safe mechanism for lack of scraping items on amazon shop (scrape)
- add more data into scrape (product details)
- add more data validation
- change locators into page object model
- add script to upload some data into the db to work with straight away.


### Fix

- mongodb creating new volume each uptime
- in_stock col in scrape (sometimes missing)
- mongo-express not displaying server stats


---
# Technical Requirements

Processor with at least 2 cores and 4gb of free RAM to spare.


---
# License

This project is under GNU General Public License v3.0
To view the [License](../main/LICENSE), click the link.


---