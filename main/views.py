from django.shortcuts import render, redirect
from .models import Post
from django.contrib.auth.decorators import login_required
from .form import *
from django.core.files.storage import FileSystemStorage

# Create your views here.

def main(request):
    posts = Post.objects.all()
    return render(request, 'posts.html', {"posts": posts})

    
@login_required(login_url='/accounts/login')
def post(request, id):
    post = Post.objects.get(id=id)
    return render(request, 'post-page.html', {"post": post})


def addPost(request):
    if request.method == 'POST':
        form = PostForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return redirect('/')
    else:
        form = PostForm()
        return render(request, 'add-post.html', {'form': form})



def editPost(request, id):
    post = Post.objects.get(id=id)

    if request.method == 'POST':
        category = request.POST["category"]
        title = request.POST["title"]
        content = request.POST["content"]
        description = request.POST["description"]
        

        post.category = category
        post.title = title
        post.description = description
        post.content = content
        if 'image' in request.FILES:
            image = request.FILES["image"]
            fs = FileSystemStorage()
            photo = fs.save(image.name, image)
            post.photo = photo
        post.save()

        return redirect('/')

    else:
        return render(request, "edit-post.html", {"post": post})


def deletePost(request, id):
    post = Post.objects.get(id=id)
    post.delete()
    return redirect("/")