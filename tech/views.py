
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Comp
#from .forms import CompForm
from django.shortcuts import redirect
from django.contrib.auth.decorators import login_required

# Create your views here.
@login_required
def tech_list(request):

    techs = Comp.objects.all()
    return render(request, 'tech/tech_list.html', {'techs': techs})
