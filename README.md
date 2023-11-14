## Тестовое задание для компании Ecom

## Задание
В базе данных хранятся шаблоны форм, состоящие из названия поля и его типа, всего поддерживаются 4 типа: дата, телефон, емейл и текст, заданные в определенном формате. На endpoint post запросом передаются названия полей со значениями, нужно подобрать подходящую для них схему, хранящуюся в базе, а если такой схемы нет то вернуть типы значений полей.

## Решение
В качестве базы данных используется TinyDB. Для валидации и определения типа данных были написаны классы валидаторов, которые используют для валидации регулярные выражения. Endpoint реализован с помощью Django Rest Framework. Для тестов использован Pytest.

## Запус приложения
Сначала в корне проекта создадим виртуальное окружение и активируем его:
```
python3 -m venv venv
source venv/bin/activate
```
Затем установим все зависимости проекта, отдав следующую команду:
```
pip install -r requirements.txt
```
Затем инициализируем базу данных шаблонами из файла [schemas.json](schemas.json)
```
python3 initialize_db.py
```
Запускаем все тесты, прописанные в файле [test_requests.json](test_requests.json) одной простой командой
```
pytest
```
После этого можно запускать сервер следующей командой:
```
python3 manage.py runserver
```
Приложение запуститься и должно быть доступно по локальному адресу [127.0.0.1:8000](http://127.0.0.1:8000)
Можем посылать запросы по [следующему адресу](http://127.0.0.1:8000/get_form/)

