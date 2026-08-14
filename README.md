# 📝 Todo API (Task Manager)

Асинхронный RESTful API для управления задачами, построенный на современном стеке Python с разделением по слоям архитектуры (Layered Architecture).

---

## 🛠 Стек технологий

* **Язык программирования:** Python 3.10+
* **Фреймворк:** [FastAPI](https://fastapi.tiangolo.com/) (асинхронная обработка запросов)
* **ORM:** [SQLAlchemy 2.0](https://www.sqlalchemy.org/) (Async Engine)
* **Валидация данных:** [Pydantic v2](https://docs.pydantic.dev/)
* **База данных:** PostgreSQL (с драйвером `asyncpg`)
* **ASGI Сервер:** [Uvicorn](https://www.uvicorn.org/)

---

## ✨ Возможности API

- **Полный асинхронный CRUD:** создание, чтение, частичное обновление и удаление задач.
- **Безопасный PATCH:** корректное обновление отдельных полей через `exclude_unset=True` (непереданные поля не затираются).
- **Строгая валидация:** автоматическая проверка входящих типов и длины строк через Pydantic.
- **Автоматическое создание таблиц:** инициализация БД при старте сервера через FastAPI `lifespan`.
- **Интерактивная документация:** автоматически сгенерированные Swagger UI и ReDoc.

---

## 📂 Структура проекта

```text
todo_api/
├── app/
│   ├── routers/
│   │   ├── __init__.py
│   │   └── task.py       # Эндпоинты API
│   ├── __init__.py
│   └── schemas.py        # Pydantic-схемы (TaskCreate, TaskUpdate, Task)
├── database/
│   ├── __init__.py
│   ├── config.py         # Настройки подключения
│   ├── database.py       # Async engine и сессии
│   ├── models.py         # SQLAlchemy модели (Task, Base)
│   └── services.py       # Бизнес-логика и операции с БД
├── main.py               # Точка входа и управление lifespan
