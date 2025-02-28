from secrets import choice
from django import forms
from numpy import require
from idapp import models
import qrcode

class SaveStudent(forms.ModelForm):
    student_code = forms.CharField(max_length=250, label="Company ID")
    first_name = forms.CharField(max_length=250, label="First Name")
    middle_name = forms.CharField(max_length=250, label="Middle Name", required=False)
    last_name = forms.CharField(max_length=250, label="Last Name")
    dob = forms.DateField(label="Birthday")
    gender = forms.ChoiceField(choices=[("Male","Male"), ("Female","Female")], label="Gender")
    contact = forms.CharField(max_length=250, label="Contact #")
    email = forms.CharField(max_length=250, label="Email")
    address = forms.Textarea()
    department = forms.CharField(max_length=250, label="Department")
    position = forms.CharField(max_length=250, label="Position")
    avatar = forms.ImageField(label="Avatar")

    class Meta():
        model = models.Student
        fields = ('student_code',
                  'first_name',
                  'middle_name',
                  'last_name',
                  'dob',
                  'gender',
                  'contact',
                  'email',
                  'address',
                  'department',
                  'position',
                  'avatar', )

    def clean_student_code(self):
        id = self.data['id'] if self.data['id'] != '' else 0
        student_code = self.cleaned_data['student_code']
        try:
            if id > 0:
                student = models.Student.exclude(id=id).get(student_code = student_code)
            else:
                student = models.Student.get(student_code = student_code)
        except:
            return student_code
        return forms.ValidationError(f"{student_code} already exists.")

