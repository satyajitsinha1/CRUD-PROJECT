from django import forms 
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = '__all__'
        labels = {
            'name':'Enter your Name:',
            'roll':'Enter Roll Number:',
            'email':'Enter your Email ID:'
            }
        widgets = {
            'name':forms.TextInput(attrs=({'class':'form-control','id':'floatingInput'})),
            'roll':forms.NumberInput(attrs=({'class':'form-control','id':'floatingInput'})),
            'email':forms.EmailInput(attrs=({'class':'form-control','id':'floatingInput'})),
            }
        error_messages = {
            'name':{'required':'Please enter a Name'},
            'roll':{
                'required':'Please Enter a Roll No',
                'unique':'This Roll No Already Exists Choose Different Roll No'
                    },
            'email':{
                'required':'Please Enter a Email',
                'invalid':'Add @ at the End'
                     }
        }