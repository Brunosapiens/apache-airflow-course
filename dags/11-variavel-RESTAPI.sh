curl -X 'POST' \
  'http://localhost:8080/api/v1/variables' \
  -H 'accept: application/json' \
  -H 'Content-Type: application/json' \
  -H 'Authorization: Bearer YOUR_ACCESS_TOKEN' \
  --user admin:admin\
  -d '{
    "key": "minha_variavel_rest_api",
    "value": "valor_via_rest_api",
    "description": "Variável criada via REST API"
  }'