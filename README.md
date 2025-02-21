# Legacy Django Mailer
Сервис рассылки электронной почты на Python 2.7 и Django 1.9.9

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

## Как развернуть проект локально (эта инструкция для Windows)
* Установить и запустить Redis (для Windows рекомендую воспользоваться [инструкцией](https://skillbox.ru/media/base/kak_ustanovit_redis_v_os_windows_bez_ispolzovaniya_docker/))
* Поднять HTTPS-тоннель (рекомендую [xTunnel](https://xtunnel.ru/))
* Для рассылок необходим SMTP-сервер. Можно воспользоваться любым из доступных (я использовал [smtp.bz](https://smtp.bz/)) 
* Клонировать репозиторий с проектом:
```
git@github.com:meteopavel/legacy_django_mailer.git
```
* Создать и активировать виртуальное окружение (Python 2.7) и установить зависимости из файла requiremnets.txt:
```
pip install virtualenv
virtualenv -p python2 venv

source venv/Scripts/activate
cd ./mailer
```
* Создать файл .env и заполнить его переменными по примеру из файла .env.example
* Выполнить миграции:
```
python manage.py migrate
```
* Создать суперпользователя для админ-панели:
```
python manage.py createsuperuser
```
* Создать сервер Django:
```
python manage.py runserver
```
* В отдельной консоли запустить Celery:
```
celery -A mailer worker --loglevel=info
```
* Зайти в админ-панель по адресу http://localhost:8000/admin/ и заполнить дво-три подписчика для тестирования рассылки
* Пройти на эндпоинт http://127.0.0.1:8000/newsletters/create-newsletter/ и заполнить модальное окно создания рассылки *(тему заполнять латинскими символами - там пока нерешённый баг админки)*
* После отправки на указанные почты поступит письмо с HTML-макетом и встроенным пикселем открытия. Подробно об этом можно узнать в статье от [Mailganer](https://mailganer.com/ru/explanation/kak-rabotaet-piksel-otkrytij-v-pismah)
* После открытия писем в админ панели в разделе Email opens появится информация об открытых письмах

## Автор
[Павел Найденов](https://github.com/meteopavel)