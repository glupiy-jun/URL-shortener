# URL-shortener
Простой сервис для сокращения ссылок. Позволяет создавать короткие ссылки, делать редирект на оригинальные URL и отслеживать количество переходов.

## Возможности
- POST / shorten: создание короткой ссылки
- GET / {short_id}: редирект на оригинальный URL и увеличение счётчика переходов
- GET / stats/{short_id}: получение количества переходов по короткой ссылке

## Технологии
- Python 3
- FastAPI
- SQLAlchemy
- SQLite
- Pytest
- python-dotenv

## Структура проекта
RL-shortener
### App
- Main.py
- Database.py
- Modes.py
- Crud.py 
### Tests
- Test-API.py
