## Запуск проекта

***Чтобы запустить проект, вам необходимо выполнить следующие шаги:***

#### 1 Клонировать репозиторий:
1 Клонировать репозиторий проекта с помощью команды
```bash
git clone git@github.com:p1mcky/kitty_api.git
```
#### 2 Создать виртуальное окружение:
Создать виртуальное окружение с помощью команды
```bash
python -m venv venv
```

#### 3 Активировать виртуальное окружение:
Активировать виртуальное окружение с помощью команды
```bash
source venv/bin/activate #(для Linux/Mac)
```
```bash
source venv\Scripts\activate #(для Windows).
```

#### 4 Установить зависимости:
Установить зависимости проекта с помощью команды
```bash
pip install -r requirements.txt.
```
#### 5 Создать базу данных:
Создать базу данных проекта с помощью команды
```bash
python manage.py migrate.
```
#### 6 Запустить сервер:
Запустить сервер проекта с помощью команды
```bash
python manage.py runserver.
```
***Примечание: Перед запуском сервера убедитесь, что у вас установлены все необходимые зависимости и база данных создана.***

## Запуск с помощью Docker Compose

**Альтернативно, вы можете запустить проект с помощью Docker Compose:**

#### 1 Клонировать репозиторий:
Клонировать репозиторий проекта с помощью команды
```bash
git clone git@github.com:p1mcky/kitty_api.git
```
#### 2 Перейти в папку с репозиторием:
```bash
cd kitty_api/
```
#### 3 Запустить контейнеры:
Запустить контейнеры с помощью команды
```bash
docker-compose up.
```
#### 4 Открыть браузер:
Открыть браузер и перейти по адресу http://localhost:8000.

## Примеры запросов:

***GET /api/breeds/***
```
Response
Content-Type: application/json
HTTP Status Code: 200
Example Value:
json
[
  {
    "id": 1,
    "name": "Breed 1",
    "slug": "breed-1"
  },
  {
    "id": 2,
    "name": "Breed 2",
    "slug": "breed-2"
  }
]
```
***GET /api/kitties/***
```
Response
Content-Type: application/json
HTTP Status Code: 200
Example Value:
json
[
  {
    "id": 1,
    "name": "Kitty 1",
    "age": 2
  },
  {
    "id": 2,
    "name": "Кот 2",
    "age": 3
  }
]
```
***POST /api/kitties/***
```
Request
Content-Type: application/json
Body:
{
  "name": "Kitty Name",
  "color": "#FF00FF",
  "age": 2,
  "breed": 1,
  "description": "Description"
}
```
```
Response
Content-Type: application/json
HTTP Status Code: 201
Example Value:
json
{
  "id": 1,
  "name": "Kitty Name",
  "color": "Color",
  "age": 2,
  "breed": 1,
  "description": "Description",
  "owner": "Owner",
  "ratings": []
}
```

***POST /api/kitties/{kitty_id}/rating***
```
Request
{
    "rating": 5
}
```
```
Response
Content-Type: application/json
HTTP Status Code: 201
Example Value:
json
{
  // No response body
}
```












