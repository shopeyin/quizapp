from django.contrib.auth.forms import UserCreationForm
from account.models import MyUser



class TeacherSignUpForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = MyUser
        fields =  ['email', 'username','password1', 'password2']

    def save(self, commit=True):
        user = super().save(commit=False)
        user.is_teacher = True
        if commit:
            user.save()
        return user