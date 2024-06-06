from django.urls import path
from new_app.apps import NewAppConfig
from new_app.views import contact, StudentListView, StudentDetailView

app_name = NewAppConfig.name

urlpatterns = [
    #path('', index, name='index'),
    path('', StudentListView.as_view(), name='index'),
    path('contact/', contact, name='contact'),
    path('view/<int:pk>/', StudentDetailView.as_view(), name='student_detail'),
]
