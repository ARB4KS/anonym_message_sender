from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import CreateView
from tweets.models import Tweets_Model
from tweets.forms import TweetForm
from tweets.send_tweets import Vamonos

# Create your views here.

truc = Vamonos

def type_tweet(request):
    form = TweetForm()
    if request.method == 'POST':  # If the form has been submitted...
        form = TweetForm(request.POST)  # A form bound to the POST data
        if form.is_valid():
            tweet = form.cleaned_data["tweet"]
            destinataire = form.cleaned_data["username"]
            destinataire = "@"+destinataire
            print(tweet, destinataire)
            truc.tweet(tweet,destinataire)
            # All validation rules pass
            # Process the data in form.cleaned_data
            # ...
            return render(request, "tweets_forms.html", {"form": form})





    return render(request,"tweets_forms.html",{"form":form})
