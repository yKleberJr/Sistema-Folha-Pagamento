# Sistema de Pagamento (Projeto de Software-UFAL)


## Installation (Venv)

Esta aplicação necessita que Python esteja instalado em sua máquina.

Após clonar o projeto, navegue até a pasta dele, crie uma pasta chamada "venv" (sem aspas), abra a pasta raiz do projeto com o terminal e digite o comando a seguir:
```sh
python -m venv venv
```


## Ativando sua venv

Para ativar sua venv use:
 Windows: cd/venv/Scripts, em seguida basta digitar o comando "./activate" (Sem aspas);
 MacOS: source venv/bin/activate
 
## Instalando o django

Após ativar sua venv, execute o seguinte comando:
```sh
pip install django
```

## Executando o porjeto

Volte para a pasta raiz do projeto pelo terminal e digite:
```sh
python manage.py makemigrations
python manage.py migrate
python manage.py runserver
```
