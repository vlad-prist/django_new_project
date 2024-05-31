# import datetime
# from django import template  # Импортируем библиотеку для работы с тегами
#
# register = template.Library()
#
# # Создание тега
# @register.simple_tag
# def current_time(format_string):
#     return datetime.datetime.now().strftime(format_string)
#
# # название тега = названию функции
