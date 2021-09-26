Запуск проекта.

1. Скопировать `.env.template` в `.env` и настроить параметры подключения к БД
2. Создать виртуальное окружение Python 3.9 и установить зависимости `pip install -r requirements/requirements.txt`
3. `cd ./source`
4. Применить миграции `python manage.py migrate`
5. Создать пользователя `python manage.py createsuperuser`
6. Запустить тестовый сервер `python manage.py runserver`

