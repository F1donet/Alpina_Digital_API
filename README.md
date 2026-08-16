# Alpina_Digital_API
Django-приложение с API для создания и управления ботами

/bots/: CRUD операции для ботов (POST — создание, GET — получение списка, GET /{id} — получение по ID, PUT /{id} — обновление, DELETE /{id} — удаление).

/scenarios/: CRUD операции для сценариев. POST должен принимать данные сценария (например, JSON). GET /{id}/steps — доступ к шагам сценария.

/scenarios/{scenario_id}/steps/: CRUD операции для отдельных шагов сценария.

ВАЖНО!
1. Создание виртуального окружения
python -m venv venv
venv\Scripts\activate     # Windows
2. Установка зависимостей
pip install -r requirements.txt
4. Настройка переменных окружения
Создайте файл .env в корне проекта:

DEBUG=True
SECRET_KEY=your-secret-key-here
OPENAI_API_KEY=your-openai-api-key-here
DATABASE_URL=sqlite:///db.sqlite3

5. Применение миграций
python manage.py migrate

6. Создание суперпользователя
python manage.py createsuperuser

7. Запуск сервера
python manage.py runserver
Приложение будет доступно по адресу: http://localhost:8000
ВАЖНО! Для перехода в режим администратора: http://localhost:8000/admin. При этом необходимо сперва создать суперпользователя для входа в режим админа.
В административном интерфейсе обеспечена возможность редактирования сценариев и добавления новых.

8. Интеграция с OpenAI GPT
Получите API ключ на OpenAI Platform.
Укажите его в переменной окружения OPENAI_API_KEY.

