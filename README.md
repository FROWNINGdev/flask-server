# SmartCam Surveillance API

## Запуск проекта
1. Установите зависимости:
```bash
pip install -r requirements.txt
```

2. Создайте базу данных и укажите строку подключения в `app.py`.

3. Инициализируйте миграции:
```bash
flask db init
flask db migrate
flask db upgrade
```

4. Запустите сервер:
```bash
python run.py
```

5. Откройте документацию:
[http://localhost:5000/docs](http://localhost:5000/docs)
