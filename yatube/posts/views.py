from django.http import HttpResponse
from django.shortcuts import render


def index(request):
    template = 'posts/index.html'
    return render(request, template)

def group_posts_list(request):
    template = 'posts/group_list.html'
    return render(request, template)
def group_post_detail(request, slug):
    return HttpResponse(f'Post number {slug}')



