## Установка зависимостей

```bash
pip install pytest httpx fastapi uvicorn[standard] pytest-asyncio
```

## Запуск сервера

```bash
uvicorn main:app --reload
```

## Запуск тестов

```bash
pytest
```
