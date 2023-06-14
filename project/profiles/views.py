from django.shortcuts import render
from profiles.models import Profile


# Create your views here.


def show_profiles(request):
    context = {"profiles": Profile.objects.all()}
    return render(request, "index.html", context=context)


def show_profile(request, profile_id):
    context = {"profile": Profile.objects.get(pk=profile_id)}
    return render(request, "profile.html", context=context)
