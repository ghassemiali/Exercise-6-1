from django.shortcuts import render
from blog.models import Post
import datetime


# below function filter the posts which their published date is lower than or equal to NOW
def blog_view(request):
    x = datetime.timedelta(hours=3, minutes=30)
    now = datetime.datetime.now().astimezone(datetime.timezone(x))
    posts = Post.objects.filter(published_date__lte=now)
    context = {'posts': posts}
    return render(request, 'blog/blog-home.html', context)

# below function is for adding 1 to the counted_views in database for specific post
def add_one_in_views(post):
    post.counted_views += 1
    post.save()

# below function is for showing the only first post in the main blog page
# it also contains add_one_in_views for dynamic views counter
def single_view(request):
    x = datetime.timedelta(hours=3, minutes=30)
    now = datetime.datetime.now().astimezone(datetime.timezone(x))
    posts = Post.objects.filter(published_date__lte=now)
    context = {'post': posts[0]}
    add_one_in_views(posts[0])
    return render(request, 'blog/blog-single.html', context)
    
def test_view(request, fname, lname, number):
    # http://127.0.0.1:8000/blog/ali/ghassemi/post-41/
    context = {'fname': fname, 'lname': lname, 'post_number': number}
    return render(request, 'blog/test.html', context)

