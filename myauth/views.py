from django.shortcuts import render
from .forms import LogInForm


def log_in(request):
    if request.method == 'POST':
        form = LogInForm(data=request.POST)
        if form.is_valid():
            new_post = form
            new_post.save()
    else:
        form = LogInForm(request.POST)
    return render(request, 'myauth/log_in.html', context={'form': form})
