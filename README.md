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

here be tree of dictionaries

here be image of project schema

## About

here be about section, detailed overview and in detail information about the project from more personal point of view.

---
# Docs

## Instalation

This is implicitly assumed that newest [docker](https://docs.docker.com/get-docker/) and [docker compose](https://docs.docker.com/compose/install/) are installed and operational. If not, please continue with their respective instalation guides.

Download or clone the repository and in the main repository' folder, where docker-compose.yml is located, open terminal and run:
```docker-compose up```
It will take around 2-5 minutes for all the containers to launch and install dependencies, not counting downloading and building the images.

Once that is done, open new terminal and run init.sh script to set up airflow users, meta database and mongo database.
```./init.sh```

When that is done, open [localhost:8080](localhost:8080) and sign into Airflow Webserver using credentials;
```login:admin
password:admin```

In the main Airflow dashboard, turn on the Amazon_ETL, it should start the dag automatically. If not, trigger it manually.

Proceed into dags' log to view the progress.

HERE BE FURTHER INSTRUCTIONS (like click on amazon_etl button to turn it on etc, ADD SCREENSHOTS)

## Getting Started

### Settings

### Project Ports

This project is deployed in local network.
8080: Airflow Webserver
8793: Airflow Scheduler
4444: Selenium grid, 4444/wd/hub for instance access
~~7900: Selenium noVNC~~
8081: Mongo-express
27017: MongoDB
8501: Dashboard


---
# TODO

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

- postgres creating new, unused volume for each uptime (init db?)
- in_stock col in scrape (sometimes missing)


---
# Technical Requirements

Processor with at least 2 cores and 4gb of free RAM to spare.


---
# License

This project is under GNU General Public License v3.0 \n
To view the [License](../blob/main/LICENSE), click the link.


---