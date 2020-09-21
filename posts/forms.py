from django import forms
from .models import Post
from django.utils.translation import ugettext as _


class PostForm(forms.ModelForm):

    
    class Meta:
        model = Post
        fields = ("group", "text")
        widgets = {
            "text": forms.Textarea,
        }
        labels = {
            "group": "Группа",
            "text": "Текст",
        }
        help_texts = {
            "group": "Укажите сообщество, в котором хотите опубликовать пост.",
            "text": "Напишите текст поста.",
        }
