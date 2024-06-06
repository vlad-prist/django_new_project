from django.shortcuts import render, get_object_or_404
from django.views.generic import ListView, DetailView
from new_app.models import Student


class StudentListView(ListView):
    model = Student
    template_name = 'new_app/index.html'


class StudentDetailView(DetailView):
    model = Student
    template_name = 'new_app/student_detail.html'


# def view_student(request, pk):
#     student_item = get_object_or_404(Student, pk=pk)
#     context = {
#        'student': student_item,
#     }
#     return render(request, 'new_app/student_detail.html', context)

# def index(request):
#     students_list = Student.objects.all()
#     context = {
#         'object_list': students_list,
#         'title': 'Student List',
#     }
#     return render(request, 'new_app/index.html', context)


def contact(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")
        print(f'{name} ({email}: {message})')
    context = {'title': 'Контакты'}
    return render(request, 'new_app/contact.html', context)
