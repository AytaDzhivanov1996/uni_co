# Инструкции по настройке

1. Клонируйте репозиторий:
    ```
    git clone git@github.com:AytaDzhivanov1996/uni_co.git
    ```
2. Установите и активируйте виртуальное окружение:
    ```
    python -m venv env
    source env/Scripts/activate  - для Windows
    source env/bin/activate - для Linux
    ```
3. Установите зависимости:
    ```
    python -m pip install --upgrade pip
    pip install -r requirements.txt
    ```
4. Поменяте переменные окружения в .env файле
5. Выполните миграции:
    ```
    python manage.py migrate
    ```
6. Создайте суперпользователя и заполните БД через административную панель:
    ```
    python manage.py createsuperuser
    ```
7. Запустите проект:
    ```
    python manage.py runserver
    ```