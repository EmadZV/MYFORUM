from django.shortcuts import render

from mycontent.forms import PostCreateForm


def landing_page(request):
    logged_in = True
    return render(request, 'mycontent/landing_page.html', {'logged_in': logged_in})


def post_create(request):
    new_post = None

    if request.method == 'POST':
        form = PostCreateForm(data=request.POST)
        if form.is_valid():
            new_post = form
            new_post.save()
    else:
        form = PostCreateForm(request.POST)
    return render(request, 'mycontent/post_create.html', context={'form': form,
                                                                  'newpost': new_post})
