from django.shortcuts import render
from .models import FindMembers

# Create your views here.
members = FindMembers.objects.all()

def index(request):
    return render(
        request,
        'members/index.html',
        {
            'members' : members
        }
    )