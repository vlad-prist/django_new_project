from django import forms

from new_app.models import Student, Subject


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'avatar',)
        # exclude = ('is_active')


class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'
