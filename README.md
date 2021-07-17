Как создавать такой проект:
1. В Pycharm Professional создаешь проект Django:
   автоматически создаются venv и файлы проекта
   
2. Лочишь зависимости:
   pip install poetry
   poetry init (all enter) -> result: create pyproject.toml
   poetry add django -> result: create poetry.lock
   poetry add pillow
   poetry add psycopg2
   
3. Создаешь .gitignore:
https://github.com/github/gitignore/blob/master/Python.gitignore
   .idea
   pg-data

4. Подключаешься к Git:
   в Pycharm: Git -> Github -> Share project on GitHub
   
5. Делаешь docker-compose.yml -> postgresql:
  postg:   # host/service в django
    restart: always
    image: postgres:12
    environment:
      POSTGRES_DB: 'db'  # 'name' в django
      POSTGRES_USER: 'user'
      POSTGRES_PASSWORD: 'user'
    volumes:
    - ./pg-data:/var/lib/postgresql/data
    ports:
    - 5433:5432  (1й порт прописываешь в settings.py, через второй БД слушает внутри docker)

settings.py:
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'db',
        'USER': 'user',
        'PASSWORD': 'user',
        'HOST': 'localhost',
        'PORT': '5433',
    }
}
   
6. Кодишь в ветках, мержишь в мастер.
