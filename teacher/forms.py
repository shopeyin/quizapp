from django import forms
from django.contrib.auth.forms import UserCreationForm
from account.models import MyUser, Teacher,Subject,Quiz



class TeacherSignUpForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields =  ['email', 'username','password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
            teacher = Teacher.objects.create(user=user)
            teacher.save()
        return user



class SubjectForm(forms.ModelForm):

    class Meta:
        model = Subject
        fields = '__all__'
        exclude = ['teacher','slug']




class AddquizForm(forms.ModelForm):

    class Meta:
        model = Quiz
        fields = '__all__'
        exclude = ['subject','slug']


    
    # class StudentSignUpForm(UserCreationForm):
    # subject = forms.ModelMultipleChoiceField(
    #     queryset=Subject.objects.all(),
    #     widget=forms.CheckboxSelectMultiple,
    #     required=True
    # )

    # class Meta(UserCreationForm.Meta):
    #     model = MyUser
    #     fields =  ['email', 'username','password1', 'password2']

    # @transaction.atomic
    # def save(self):
    #     user = super().save(commit=False)
    #     user.is_student = True
    #     user.save()
    #     student = Student.objects.create(user=user)
    #     student.subject.add(*self.cleaned_data.get('subject'))
    #     return user