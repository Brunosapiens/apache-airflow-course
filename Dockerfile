FROM astrocrpublic.azurecr.io/runtime:3.0-4

ENV AIRFLOW_VAR_NOME_DA_VARIAVEL = 'minha variável e ambiente'
ENV AIRFLOW_VAR_JSON='{"key":"valor_json","key2":"valor_json2"}'

ENV AIRFLOW_CONN_MY_PROD_DATABASE='{ \
    "conn_type": "my-conn-type", \
    "description": "minha descricao", \
    "host": "localhost", \
    "login": "admin", \
    "port": "0", \
    "schema": "default", \
    "extra": "{\"key\":\"value\"}", \
    "password": "admin" \
}'