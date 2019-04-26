from django.shortcuts import render, get_list_or_404,get_object_or_404
from django.utils import timezone
from .models import Challenge,Entries
from .forms import ChallengeForm, EntryForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate

# Create your views here.

def register(request):
    if request.method =="POST":
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request,user)
            #redirect to the login page
            return redirect('date_list')
            #return render(request = request,template_name = "date_battle/date_list.html")

    else: 
            form = UserCreationForm
    return render(request = request,
                template_name = "registration/register.html",
                context = {"form":form})

def date_list(request):
#Challenge is the QuerySet that represents all challenges sorted by date
    
    #Change to proper QuerySet. Probably an order by
    challenge = Challenge.objects.all()
#This requests the page, and sends challenge in named as challenge
    return render(request, 'date_battle/date_list.html',{'challenge':challenge})

def challenge_rules(request, pk):
    #challenge = get_object_or_404(Challenge('creator','prize','rules'), pk=pk)
    challenge = get_list_or_404(Challenge.objects.filter(pk=pk).all())
    #This is where you would query for the data that is being retrieved.
    #In this case the data about the challenge, e.g. The day by day data
    return render(request,'date_battle/challenge_details.html',{'challenge':challenge})

@login_required
def challenge_new(request):
    if request.method =="POST":
        form = ChallengeForm(request.POST)
        if form.is_valid():
            challenge = form.save(commit=False)
            challenge.creator = request.user
            challenge.start_date = timezone.now()
            challenge.save()
            return redirect('challenge_rules', pk = challenge.pk)
    else:
        form = ChallengeForm()
    return render(request, 'date_battle/challenge_new.html',{'form':form})


@login_required
def entry_new(request,pk):
    competitor = request.user
    challenge = get_object_or_404(Challenge,pk=pk)
    if request.method=="POST":
        form = EntryForm(request.POST)
        if form.is_valid():
            today = timezone.now()
            #This will see if the challenge is over or not
            if challenge.end_date.date() < today.date():
                entries = form.save(commit=False)
                #get primary key. Edit over old entry
                
                competitor = request.user
                #entries.streak = calculate_streak(challenge,competitor)
                entries.streak=0
                entries.competitor = competitor
                entries.prev_date = timezone.now()
                entries.today = today

                entries.challenge = challenge

                entries.save()
                return redirect('date_list')
            else:
                #create a resolution page that gives the results.
                results_check(request, pk)
    else:
        form = EntryForm()
    return render(request,'date_battle/add_entry.html',{'form':form})


def results_check(request, pk):
    

"""
def calculate_streak(challenge,competitor):
#prev_entries is the list that contains all the entries from a specific
#competitor and challenge
	dates = Entries.objects.filter(challenge=challenge, competitor=competitor)
	if all(consecutive(dates[i],dates[i+1]) for i in x
"""
