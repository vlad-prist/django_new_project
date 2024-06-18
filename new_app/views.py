from django.forms import inlineformset_factory
from django.shortcuts import render, get_object_or_404, redirect
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

from new_app.forms import StudentForm, SubjectForm
from new_app.models import Student, Subject
from django.urls import reverse_lazy, reverse


class StudentListView(ListView):
    model = Student
    # template_name = 'new_app/index.html'


class StudentDetailView(DetailView):
    model = Student
    # template_name = 'new_app/student_detail.html'


class StudentCreateView(CreateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy("new_app:index")


class StudentUpdateView(UpdateView):
    model = Student
    form_class = StudentForm
    success_url = reverse_lazy("new_app:index")

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        SubjectFormset = inlineformset_factory(Student, Subject, form=SubjectForm, extra=1)
        if self.request.method == 'POST':
            context_data['formset'] = SubjectFormset(self.request.POST, instance=self.object)
        else:
            context_data['formset'] = SubjectFormset(instance=self.object) #instance=self.object
        return context_data

    def form_valid(self, form):
        formset = self.get_context_data()['formset']
        self.object = form.save()
        if formset.is_valid():
            formset.instance = self.object
            formset.save()

        return super().form_valid(form)

class StudentDeleteView(DeleteView):
    model = Student
    success_url = reverse_lazy("new_app:index")


def toggle_activity(request, pk):
    student_item = get_object_or_404(Student, pk=pk)
    if student_item.is_active:
        student_item.is_active = False
    else:
        student_item.is_active = True

    student_item.save()

    return redirect(reverse("new_app:index"))



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
