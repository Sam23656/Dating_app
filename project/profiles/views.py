from django.shortcuts import render
from profiles.models import Profile


# Create your views here.


def show_profiles(request):
    context = {"profiles": Profile.objects.all()}
    return render(request, "index.html", context=context)


def show_profile(request, profile_id):
    context = {"profile": Profile.objects.get(pk=profile_id)}
    return render(request, "profile.html", context=context)


def show_register_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        sure_name = request.POST.get("sure_name")
        age = request.POST.get("age")
        status = request.POST.get("status")
        salary = request.POST.get("salary")
        description = request.POST.get("description")

        Profile.objects.create(Name=name,
                               Sure_Name=sure_name,
                               Age=age,
                               Status=status,
                               Salary=salary,
                               Description=description)

    return render(request, "Register.html")
