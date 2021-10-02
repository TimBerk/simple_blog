# simple_blog

<p align="left">
    <a href="https://www.python.org/" target="blank">
        <img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white" />
    </a>
    <a href="https://www.django-rest-framework.org/" target="blank">
        <img src="https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray"/>
    </a>
    <a href="https://www.sqlite.org/index.html" target="blank">
        <img src="https://img.shields.io/badge/SQLite-07405E?style=for-the-badge&logo=sqlite&logoColor=white"/>
    </a>
    <a href="https://drf-yasg.readthedocs.io/en/stable/index.html" target="blank">
        <img src="https://img.shields.io/badge/Swagger-85EA2D?style=for-the-badge&logo=Swagger&logoColor=white"/>
    </a>
</p>

Требования
===

- Poetry 1.1+
- Python 3.8+
- Django 3.2+

Установка
===

- Установка зависимостей `@poetry install`
- Установка переменных окружения `cp .env.dist .env`
- Запуск сервера `make run`. API доступно по адресу `127.0.0.1:8000`

## Built With

* [Django](https://www.djangoproject.com/) -  web framework written in Python.
* [Django REST](https://www.django-rest-framework.org/) - a powerful and flexible toolkit for building Web APIs.
* [Django Filter](https://django-filter.readthedocs.io/en/master/) - a generic, reusable application to alleviate writing some of the more mundane bits of view code.
* [Django environ’s](https://django-environ.readthedocs.io/en/latest/) - Django-environ allows to utilize 12factor inspired environment variables to configure Django application.
* [Django CORS](https://pypi.org/project/django-cors-headers/) - A Django App that adds Cross-Origin Resource Sharing (CORS) headers to responses.
* [Simple JWT](https://github.com/SimpleJWT/django-rest-framework-simplejwt) - Simple JWT is a JSON Web Token authentication plugin for the Django REST Framework.
* [DRF YASG](https://drf-yasg.readthedocs.io/en/stable/readme.html) - Generate real Swagger/OpenAPI 2.0 specifications from a Django Rest Framework API.
* [Djoser](https://djoser.readthedocs.io/en/latest/getting_started.html) - Token based authentication from DRF.
* [Django MPTT](https://django-mptt.readthedocs.io/en/latest/) - MPTT is a technique for storing hierarchical data in a database.
* [django-cors-headers](https://github.com/adamchainz/django-cors-headers) - A Django application for handling the server headers required for Cross-Origin Resource Sharing (CORS).

## Poetry commands

* **poetry install** - use the lock file to install all dependencies
* **poetry add [package-name]** - add a new dependency and install it in the current virtual environment
* **poetry add -D [package-name]** - add a new dependency and install it in the current virtual environment
* **poetry remove [package-name]** - remove a package from a Virtual Environment.
* **poetry remove -D [package-name]** - remove a dev package from a Virtual Environment.

## Make команды

* **run** - запуск сервера разработки.
* **migrate** - синхронизация состояние базы данных с текущим состоянием моделей и миграций.
* **superuser** - создание администратора.
* **lint** - проверка правильности кода.
* **files** - инициализация статических файлов.
