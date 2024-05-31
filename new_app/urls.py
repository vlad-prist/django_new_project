from django.urls import path
from new_app.apps import NewAppConfig
from new_app.views import index, contact

app_name = NewAppConfig.name

urlpatterns = [
    path('', index, name='index'),
    path('contact/', contact, name='contact'),
]
