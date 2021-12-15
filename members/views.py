from django.shortcuts import render
from .models import FindMembers

def index(request):
    members = FindMembers.objects.all()
    return render(
        request,
        'members/index.html',
        {
            'members' : members
        }
    )

def members_all_info(request, pk):
    member = FindMembers.objects.get(pk=pk)
    return render(
        request,
        'members/members_all_info.html',
        {
            'member' : member
        }
    )
