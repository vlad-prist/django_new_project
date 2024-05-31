from django.shortcuts import render

from new_app.models import Student


def index(request):
    students_list = Student.objects.all()
    context = {
        'object_list': students_list,
        'title': 'Student List',
    }

    return render(request, 'new_app/index.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f'{name} ({email}: {message})')

    context = {
        'title': 'Контакты'
    }

    return render(request, 'new_app/contact.html', context)
