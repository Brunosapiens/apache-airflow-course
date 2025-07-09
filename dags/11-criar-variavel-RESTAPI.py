import requests
from requests.exceptions import RequestException

try:
    url = "http://localhost:8080/api/v2/variables"  

    payload = {
        "key": "minha_variavel_py",
        "value": "meu_dado"
    }

    response = requests.post(
        url=url,
        json=payload,
        headers={
            'accept': 'application/json',
            'Content-Type': 'application/json'
        },
        auth=('admin', 'admin')  # Altere se tiver outro usuário/senha
    )

    response.raise_for_status()
    print("Variável criada com sucesso:", response.json())

except RequestException as e:
    print("Erro na requisição:", e)


    response.raise_for_status()  # Levanta exceção para códigos 4xx/5xx
    print("Variável criada com sucesso!")
    print("Resposta:", response.json())

except RequestException as e:
    print("Erro na requisição:", e)
    if hasattr(e, 'response') and e.response:
        print("Detalhes do erro:", e.response.json())