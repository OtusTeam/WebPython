from django.contrib.auth.forms import UserCreationForm

from myauth.models import OtusUser


class OtusUserCreateForm(UserCreationForm):
    # create_author = BooleanField(label='super post', required=False)

    # class Meta(UserCreationForm.Meta):
    class Meta:
        model = OtusUser
        fields = ('username', 'password1', 'password2', 'email')

    # def save(self, commit=True):
    #     author_inst = ...
