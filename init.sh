#!/usr/bin/env bash

docker exec -it airflow_webserver bash -c "airflow users create --role Admin --username admin --email admin --firstname admin --lastname admin --password admin"