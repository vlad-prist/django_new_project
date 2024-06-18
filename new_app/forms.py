from django import forms

from new_app.models import Student


class StudentForm(forms.ModelForm):

    class Meta:
        model = Student
        # fields = '__all__'
        fields = ('first_name', 'last_name', 'avatar', )
        # exclude = ('is_active')
