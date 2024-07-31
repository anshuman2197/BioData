from django.shortcuts import render

# Create your views here.
def skill(request):
    skill={'skill':"active"}
    return render(request,'edu/skill.html',skill)