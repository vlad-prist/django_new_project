# 1) подключение к БД PostgresQL

В файле config/settings.py вносим изменения в раздел DATABASES:
{
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'django_db',
        'USER': 'postgres',
        'PASSWORD': '676889',
        'HOST': 'localhost',
        'PORT': 5432,
    }
}

Обязательно меняем ENGINE на postgresql_psycopg2 и прописываем имя БД, юсера, пароль, хост и порт.
Если с одного и того же компа подключаешься к БД, то хост и порт прописывать не обязательно. 
Если с другого компа, то хост будет 127.0.0.1

БД в Постгресе создаем в ручную.
команда psql -U postgres не сработала в консоле пайчарма.

Далее устанавливаем утилиту pip install psycopg2-binary