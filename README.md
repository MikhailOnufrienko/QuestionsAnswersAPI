# QuestionsAnswersAPI

## API-сервис, запрашивающий данные с сервиса вопросов и ответов для викторины

### Тестовое задание на позицию Python-разработчика


1. Клонируйте репозиторий.

2. Переименуйте файл `.env.example` в `.env`. При необходимости измените значения переменных окружения.

2. Из корневой директории локального репозитория выполните команду:

```
docker compose up
```

3. Описание OpenAPI находится по адресу:

```
http://127.0.0.1:8001/api/openapi
```

4. Пример POST-запроса на URL http://127.0.0.1:8001/api/v1/questions:

```
{
  "questions_num": 1
}
```

Так как БД пока не содержит записей, при первом запросе должен прийти ответ:

```
{'question': 'Нет предыдущего сохранённого вопроса.'}

```

При повторных запросах в качестве ответа будет приходить последний сохранённый в БД вопрос, взятый из стороннего сервиса с вопросами и ответами, либо сообщение с ошибкой.
