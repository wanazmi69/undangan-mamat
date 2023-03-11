from django.shortcuts import render
from django.http import JsonResponse
from UserMessage.forms import UserForm
from UserMessage.models import User

def index(request):
    users = User.objects.all()
    
    form = UserForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return JsonResponse({'status': 'success'})
        else:
            return JsonResponse({'status': 'errors'})
    else:
        form = UserForm()

    context = {
        'users': users,
        'form': form,
    }
    return render(request, 'index.html', context)
# halogha

    