Проект: "Доска объявлений"
- Фичи:
```
Регистрация
Вход по логину
Выход
Изменение профиля
Изменение пароля
Активация логина по емайл
Добавлять объявления могут только авторизованные пользователи
Добавленное объявление привязано к пользователю
Рубрики добавляет только админ
```
- Как создавать такой проект:

```
1. В Pycharm Professional создаешь проект Django:
   автоматически создаются venv и файлы проекта

2. Лочишь зависимости:
   pip install poetry poetry init (all enter) -> result: create pyproject.toml
   poetry add django -> result: create poetry.lock
   poetry add pillow
   poetry add psycopg2
   poetry add django-environ

3. Создаешь .gitignore:
   https://github.com/github/gitignore/blob/master/Python.gitignore
   .idea 
   pg-data

4. Подключаешься к Git:
   в Pycharm: Git -> Github -> Share project on GitHub

5. Делаешь docker-compose.yml -> postgresql:
postg_bboard:
    restart: always
    image: postgres:12
    environment:
      POSTGRES_DB: 'bboard'  # name db в django
      POSTGRES_USER: 'user'
      POSTGRES_PASSWORD: 'user'
    volumes:
      - ./pg-data:/var/lib/postgresql/data
    ports:
      - 5433:5432

settings.py:

DATABASES = {
'default': {
'ENGINE': 'django.db.backends.postgresql',
'NAME': 'db',
'USER': 'user',
'PASSWORD': 'user',
'HOST': 'localhost',
'PORT': '5433', }
}

6. Кодишь в ветках, мержишь в мастер.

7. Важное о GitAction:
   В workflow надо запустить весь проект! Это значит, нужно установить Python, Postgreqsl и все зависимости. Передать
   данные из .env в Git , создав в settings -> enviroments и добавив не только Enviroment secrets, но и Perository
   Secrets! https://github.com/NankuF/djangoProject1_BulletinBoard/settings/environments ;
   Repository secrets нужен, чтобы Питон мог запустить тесты, а Enviroment secrets нужны чтобы запустился Django (ну я так понял)

Сделано:

1. User:
   Вход по логину, Выход, Регистрация, Изменение профиля, Изменение пароля, Активация логина по емайл.

2. Bboard:
   Рубрики, Добавление объявлений с привязкой к юзеру.
   (Рубрики можно создать через админ панель. Объявления могут создавать все через форму на странице)

3. Tests:
   Автотесты через GitAction на базе unittest. Проверено только users.models.py

Сделать:
 - Отправка email через celery 
 - Логин по соц.сети (работает сомнительно)


######################
Установка celery и redis локально: https://webdevblog.ru/asinhronnye-zadachi-v-django-s-redis-i-celery/
poetry add celery
poetry add redis
В djangoProject1 создаем файл celery.py
В djangoProject1 заполняем  __init__.py
В djangoProject1 заполняем settings.py В users создаем tasks.ru (асинхронная отправка email)

# celery in settings.py  (redis in docker-compose)

CELERY_BROKER_URL = 'redis://localhost:6379'  
CELERY_RESULT_BACKEND = 'redis://localhost:6379'  
CELERY_ACCEPT_CONTENT = ['application/json']  
CELERY_RESULT_SERIALIZER = 'json'  
CELERY_TASK_SERIALIZER = 'json'

Чтобы celery установленный в venv запускался с Redis(установленным в docker-compose), необходимо прописать ports:
- 6379:6379 # (HOST_PORT:CONTAINER_PORT)
для сервиса redis, потому что по умолчанию redis слушает 6379/tcp, а надо чтобы слушал 6379->6379/tcp
(Важно отметить различие между HOST_PORT и CONTAINER_PORT. В приведенном выше примере, для redis, то HOST_PORT есть 6379
и контейнер порт 6379(Redis по умолчанию). Сетевое взаимодействие между сервисами использует расширение CONTAINER_PORT.
Когда HOST_PORT определено, сервис доступен и за пределами роя.)

Команды:
celery -A djangoProject1 worker -l info   (запускаем наши задачи в celery)

docker-compose up redis (запуск сервера в докере)
docker-compose ps (смотрим список запущенных контейнеров)
docker exec -it djangoproject1_redis_1 redis-cli ping  (ответ в консоли будет PONG если сервер запущен)```

   