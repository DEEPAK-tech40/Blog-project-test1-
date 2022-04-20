from django import forms
from blog.models import Post,Comment

class PostForm(forms.ModelForm):

    class Meta():
        model = Post
        fields = ('Author','Title','Text')
        widgets = {
                'Title':forms.TextInput(attrs={'class':'textinputclass'}),
                'Text':forms.Textarea(attrs={'class':'editable medium-editor-textarea postcontent'})
                    }


class CommentForm(forms.ModelForm):

    class Meta():
        model = Comment
        fields = ('Author','Text')
        widgets = {
                'Author':forms.TextInput(attrs={'class':'textinputclass'}),
                'Text':forms.Textarea(attrs={'class':'editable medium-editor-textarea'})
                    }
