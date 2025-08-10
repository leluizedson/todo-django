VISÃO GERAL DO SISTEMA

- App de gerenciamneto de tarefas feito em Django

INTEGRANTES 

- Luis Edson de Oliveira e Gustavo Anthony Costa

INSTRUÇÕES PARA INSTALAÇÃO

Clone este repositorio localmente em sua maquina: 
> git clone https://github.com/leluizedson/todo-django

Crie e ative um ambiente virtual no diretorio raiz do projeto:
> cd todo-django

> python -m venv venv

> venv\Scripts\activate

Instale as dependencias necessarias via requirementes.txt:
> pip install requirement.txt

Aplique as configurações do projeto:
> python manage.py makemigrations

> python manage.py migrate

Rode o servidor:
> python manage.py runserver

> Endereço local: http://127.0.0.1:8000