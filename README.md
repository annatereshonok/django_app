# django_app

- Настроен Django-проект с виртуальным окружением.
- Создано приложение catalog, зарегистрировано в settings.py.
- Добавлена маршрутизация для страниц:
  - // — главная
  - /contacts/ — контакты
- Используются шаблоны home.html и contacts.html с Bootstrap-оформлением.
- Подключены собственные статические файлы (CSS и JS) из папки static/.
- Оформлены контроллеры (views.py) для вывода обеих страниц.
- Используется namespace catalog для URL'ов.

## Структура проекта
```plaintext
django_app/
│
├── catalog/
│   ├── __init__.py
│   ├── views.py
│   ├── urls.py
│   ├── apps.py
│   ├── models.py
│   ├── tests.py
│   ├── static/
│   │   ├── css/
│   │   │   └── bootstrap.css
│   │   └── js/
│   │       └── bootstrap.bundle.min.js
│   └── templates/
│       └── catalog/
│           ├── home.html
│           └── contacts.html
│
├── config/
│   └── __init__.py
│   └── settings.py
│   └── urls.py
│   └── asgi.py
│   └── wsgi.py
│
├── manage.py
├── requirements.txt
├── README.md
├── .flake8
└── .gitignore
```

## Как запустить проект
1. Клонируйте репозиторий и перейдите в папку проекта:

```bash
git clone <repo_url>
cd catalog_project
```

2. Создайте и активируйте виртуальное окружение:

```bash
python -m venv venv
source venv/bin/activate  # для Linux/macOS
venv\Scripts\activate     # для Windows
```

3. Установите зависимости:

```bash
pip install -r requirements.txt
```

4. Запустите сервер:

```bash
python manage.py runserver
```

5. Перейдите в браузере:

- Главная: http://localhost:8000/
- Контакты: http://localhost:8000/contacts/