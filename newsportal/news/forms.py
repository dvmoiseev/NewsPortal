from django import forms
from django.core.exceptions import ValidationError

from .models import Post


class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'text', 'author']

    def clean(self):
        cleaned_data = super().clean()
        title = cleaned_data.get("title")
        text = cleaned_data.get("text")

        if title == '':
            raise ValidationError(
                "Заголовок новости или статьи не может быть пустым"
            )

        if text == '':
            raise ValidationError(
                "Текст новости или статьи не может быть пустым"
            )

        return cleaned_data