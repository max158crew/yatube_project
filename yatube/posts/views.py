from django.http import HttpResponse


def index(request):
    return HttpResponse('Index page first Django project. Yahooo!')

def group_posts_list(request):
    return HttpResponse('Group list is here')
def group_post_detail(request, slug):
    return HttpResponse(f'Post number {slug}')



