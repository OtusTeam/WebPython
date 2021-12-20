from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from posting.models import Article


class PostCreateForm(ModelForm):
    mark_it = BooleanField(label='super post', required=False)

    class Meta:
        model = Article
        # fields = ('author', 'title', 'text')
        exclude = ('published_at',)

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for f_name, f_obj in self.fields.items():
            # print(f_name, f_obj)
            f_obj.widget.attrs['class'] = 'form-item'
            # if f_name == 'title':
            #     f_obj.widget = HiddenInput()

    def clean_title(self):
        value = self.cleaned_data['title']
        # if not value or not value[0].isupper():
        if not value[0].isupper():
            raise ValidationError('title is not title')

        return value

    def save(self, commit=True):
        # own logic
        super(PostCreateForm, self).save(commit=commit)
