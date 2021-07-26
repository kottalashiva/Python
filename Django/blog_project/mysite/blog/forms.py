from django import forms
from blog.models import Post, Comment


class PostForm(forms.ModelForm):
    class Meta():
        model = Post
        fields = ('author', 'title', 'text')

        # connecting the specic fields to CSS,
        widgets = {
            'title': forms.TextInput(attrs={'class': 'textinputclass'}), # class are the css class
            'text': forms.Textarea(attrs={"class": "editable medium-editor-textarea postcontent"}) #editable and medium-editro-textarea are the builtinclass
        }

class CommentForm(forms.ModelForm):
    class Meta():
        model = Comment
        fields = ("author", "text")

        widgets = {
        'author': forms.TextInput(attrs={'class': 'textinputclass'}),
        'text': forms.Textarea(attrs={"class": "editable medium-editor-textarea postcontent"}) #editable and medium-editro-textarea are the builtinclass
        }
