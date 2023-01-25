## Inference For Prototype

Airflow 사용을 위한 dags폴더 내 Train 및 Inference 등 airflow내 포함될 파일들 이동

poetry lock환경설정 필

big query key와 steam api key 폴더 내 위치 및 기입 필요

## Airflow 예상안

PostgreSQL >1번> Big query >2번> Train
2번은 매일 utc 기준 22시로 Train되는 것으로 정해져있으나, 1번은 구현 X
