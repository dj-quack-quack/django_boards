from django import forms
from .models import Topic
from .models import Post

##below is the model form for new topics
class NewTopicForm(forms.ModelForm):
    message = forms.CharField(
        widget=forms.Textarea(
            attrs={'rows': 5, 'placeholder': 'What is on your mind?'}
        ),
        max_length=4000,
        help_text='The max length of the text is 4000.'
    )
    ##the meta class is a Django thing. Iin the Meta class you're defining the model you want to base the form on
    ##as well as the models fields that you want to use in the form.
    ##The extra message field outside of the Meta class is overriding whatever is created by default in the Meta class.
    class Meta:
        model = Topic
        fields = ['subject', 'message']

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['message']