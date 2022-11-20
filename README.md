# Проект Django_stripe_API
## Описание проекта 

Простой сервер с информацией о товаре и с формой оплаты на StripeAPI

### Проект развернут на ![heroku](https://sheltered-journey-95869.herokuapp.com) 

## Как запустить проект локально:
Клонировать репозиторий и перейти в него в командной строке:

```bash
  git clone https://github.com/UchihaIP/Django_stripe_API.git
  cd Django_stripe_API
```
Cоздать и активировать виртуальное окружение:
```bash
  python3 -m venv env source env/bin/activate
```
Установить зависимости из файла requirements.txt:
```bash
  python3 -m pip install --upgrade pip
  pip install -r requirements.txt
```
Выполнить миграции:
```bash
  python3 manage.py migrate
```
(Опционально) Запустить менеджер на добавление данных в БД:
```bash
  python3 manage.py loaditems <количество записей>
```
Запустить проект:
```bash
  python3 manage.py runserver
```
## API Reference

#### Получение информации о товаре

```http
  GET /item/{item_id}
```

| Parameter | Type     | Description                |
| :-------- | :------- | :------------------------- |
| `item_id` | `integer` | **Required** id продукта|


#### Получение Stripe Session Id для оплаты выбранного продукта

```http
  POST /buy/{item_id}
```

| Parameter | Type     | Description                       |
| :-------- | :------- | :-------------------------------- |
| `item_id`      | `integer` | **Required** id продукта|



## Tech Stack

![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
![JavaScript](https://img.shields.io/badge/javascript-%23323330.svg?style=for-the-badge&logo=javascript&logoColor=%23F7DF1E)
![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
![DjangoREST](https://img.shields.io/badge/DJANGO-REST-ff1709?style=for-the-badge&logo=django&logoColor=white&color=ff1709&labelColor=gray)
![Docker](https://img.shields.io/badge/docker-%230db7ed.svg?style=for-the-badge&logo=docker&logoColor=white)
![Stripe](https://img.shields.io/badge/Stripe-626CD9?style=for-the-badge&logo=Stripe&logoColor=white)
![Heroku](https://img.shields.io/badge/heroku-%23430098.svg?style=for-the-badge&logo=heroku&logoColor=white)

## Author

- [Рифат Хасанов](https://github.com/UchihaIP)
![Telegram](https://img.shields.io/badge/Telegram-2CA5E0?style=for-the-badge&logo=telegram&logoColor=white)](https://t.me/lawlietLL)

