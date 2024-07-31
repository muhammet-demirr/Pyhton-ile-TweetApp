from django import forms
from django.forms import ModelForm #3.kullanım formda
from tweetapp.models import Tweet

class AddTweetForm(forms.Form): #2.yöntem 
    nickname_input = forms.CharField(label="Nickname",max_length=50)
    message_input = forms.CharField(label="Message",max_length=100,
                                    widget=forms.Textarea(attrs={"class":"tweetmessage"}))
    
class AddTweetModelForm(ModelForm): #3.yöntem
    class Meta:
        model = Tweet
        fields = ["username","message"]  #modelde koyduğumuz yerler eskinden username yazan yerlerde nickname yazıyodu