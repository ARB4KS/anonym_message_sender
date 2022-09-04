from django import forms
from tweets.models import Tweets_Model

class TweetForm(forms.ModelForm):
    class Meta:
        model = Tweets_Model
        fields = "__all__"


