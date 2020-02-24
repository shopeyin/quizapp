from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group, Permission
from django.db import transaction
from django.contrib.auth import authenticate
from account.models import MyUser,Subject,Student



class StudentSignUpForm(UserCreationForm):
    subject = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True,
    
    )

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields =  ['email', 'username','password1', 'password2']
        
    def __init__(self, *args, **kwargs):
        super(StudentSignUpForm,self).__init__(*args, **kwargs)
        self.fields['password1'].help_text=''
        self.fields['password2'].help_text=''

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_student = True
        user.save()
        student = Student.objects.create(user=user)
        student.subject.add(*self.cleaned_data.get('subject'))
        return user




class AnswerForm(forms.Form):
    answer            = forms.CharField(required=True,max_length=100)


     