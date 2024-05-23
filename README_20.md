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

# 2) Создание Моделей
1. В прилоджении в папке models.py 
прописываем класс, у которого родительский класс будет models.Model
Задаем атрибуты, такие как CharField - хранение тескта и добавляем ImageField - для хранения изображения

Также в models.py прописываем метод str, и class Meta (Информация для вывода удобного отображения текстов нашей модели)

2. Миграция запускается через консоль командой 
python manage.py makemigrates

(поскольку у нас есть атрибут ImageField то нам до миграции нужно установить pillow)
командой pip install pillow - утилита для изображения

3. В settings.py в самом конце прописываем 
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

и создаем папку в корне проекта "media"

4. в Config.urls.py дописываем 
"+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)"
незабываем импортировать static и settings:

from django.conf import settings
from django.conf.urls.static import static

# 3) Админка

Создаем Админа командой:
python manage.py createsuperuser
для данного проекта админ создан:
admin_django_latest
latest123456

Далее переходим на сайт http://localhost:8000/admin/ (чтобы сайт заработал, нужно вначале запустить проект в пайчарме)

в файле admin.py заполнили два примера:
1. легкий:
admin.site.register(Student)
2. Для определенных настроек делаем фикстуру:
@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name',) - то что отображается
    list_filter = ('is_active',) - то по чему можно фильтровать
    search_fields = ('first_name', 'last_name',) - для поиска

# 4) Shell
Устанавливаем пакет ipython
Запускается через консоль командой 
python manage.py shell

Команды shell:
1. from new_app.models import Students
 запрашиваем список студентов
2. Student.objects.all()
получаем всех студентов
3. Student.objects.get(pk=1)
получаем студента по пк
Можно посмотреть его содержимое (словарь)
Student.objects.get(pk=1).__dict__
4. Поиск по фильтру
Student.objects.filter(is_active=True)
и наоборот Student.objects.exclude(is_active=True)
5. Несколько параметров:
Student.objects.filter(is_active=True, last_name='Иванов')
6. Создание нового студента 
первый способ:
Student.objects.create(first_name='Vlad', last_name='Alexandrov')
второй способ:
st = Student(first_name='Artem', last_name='Morozov') (но он не попадает в админку, а пока хранится в памяти)
st.save() - сохраняем нового студента в админке

# 4) Фикстуры
команда в консоли
python manage.py dumpdata new_app > data.json
сохраняет данные в json файл
(для форматирования json-файла Ctrl+Alt+L)





