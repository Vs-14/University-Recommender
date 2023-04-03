from django.shortcuts import render
from .forms import PostForm
from .models import Post

# Create your views here.

def discussion(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            form = PostForm()
    else:
        form = PostForm()

    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'discuss.html', {'form': form, 'posts': posts})