<!-- PROJECT SHIELDS -->
[![Python][Python-shield]][Python-url]
[![Django][Django-shield]][Django-url]
[![PostgreSQL][PostgreSQL-shield]][PostgreSQL-url]

<!-- PROJECT LOGO -->
<br />
<div align="center">
  <a href="https://github.com/meteopavel/legacy_django_mailer">
    <img src="images/logo-big.png" alt="Logo" width="400" height="316">
  </a>

  <h3 align="center">Legacy Django Mailer</h3>

  <p align="center">
    Удобный сервис рассылки email!
    <br />
    <a href="https://legacymailer.meteopavel.space/newsletters/create-newsletter">Демо-версия</a>
    ·
    <a href="https://github.com/meteopavel/legacy_django_mailer/issues/new?labels=bug">Сообщить об ошибке</a>
    ·
    <a href="https://github.com/meteopavel/legacy_django_mailer/issues/new?labels=enhancement">Предложить улучшение</a>
  </p>
</div>

## Основной функционал
1. Отправка рассылок с использованием HTML-макета и списка подписчиков.
2. Для создания рассылки используется AJAX запрос. Форма для создания рассылки заполняется в модальном окне.
3. Отправка отложенных рассылок.
4. Использование переменных в макете рассылки.
5. Отслеживание открытий писем.

## Основные используемые инструменты
* Python 2.7
* Django
* Redis
* Celery
* Python-dotenv
* PostgreSQL
* Gunicorn
* Requests

## Как развернуть проект локально
* Поднять HTTPS-тоннель (рекомендую [xTunnel](https://xtunnel.ru/))
* Для рассылок необходим SMTP-сервер. Можно воспользоваться любым из доступных (я использовал [smtp.bz](https://smtp.bz/)) 
* Клонировать репозиторий с проектом:
```
git@github.com:meteopavel/legacy_django_mailer.git
```
* Создать файл .env и заполнить его переменными по примеру из файла .env.example
* Установить и запустить Docker
* Выполнить команды:
```
docker compose up -d --build
docker compose exec mailer python manage.py migrate
docker compose exec mailer python manage.py collectstatic --no-input
docker compose exec mailer python manage.py createsuperuser
```
* Зайти в админ-панель по адресу http://localhost:8111/admin/ и заполнить дво-три подписчика для тестирования рассылки
* Пройти на эндпоинт http://127.0.0.1:8111/newsletters/create-newsletter/ и заполнить модальное окно создания рассылки *(тему заполнять латинскими символами - там пока нерешённый баг админки)*
* После отправки на указанные почты поступит письмо с HTML-макетом и встроенным пикселем открытия. Подробно об этом можно узнать в статье от [Mailganer](https://mailganer.com/ru/explanation/kak-rabotaet-piksel-otkrytij-v-pismah)
* После открытия писем в админ панели в разделе Email opens появится информация об открытых письмах

## Автор
[Павел Найденов](https://github.com/meteopavel)

<!-- MARKDOWN LINKS & IMAGES -->
<!-- https://www.markdownguide.org/basic-syntax/#reference-style-links -->
[Python-shield]: https://img.shields.io/badge/Python-v2.7-blue?style=flat&logo=python&labelColor=FDEBD0&logoColor=blue
[Python-url]: https://www.python.org/downloads/release/python-2718/
[Django-shield]: https://img.shields.io/badge/Django-v1.9-green?style=flat&logo=django&labelColor=FDEBD0&logoColor=blue
[Django-url]: https://docs.djangoproject.com/en/5.0/releases/1.9/
[PostgreSQL-shield]: https://img.shields.io/badge/PostgreSQL-v11.7-blue?style=flat&logo=PostgreSQL&labelColor=FDEBD0&logoColor=blue
[PostgreSQL-url]: https://www.postgresql.org/docs/13/release-11-7.html 