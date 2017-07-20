from django.shortcuts import render,get_object_or_404
from .models import Post
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from django.views.generic import ListView
#from .froms import EmailPostForm

# Create your views here.
class PostListView(ListView):
    """docstring for PostListView"""
    queryset = Post.published.all()
    context_object_name = 'posts'
    paginate_by = 3
    template_name = 'blog/post/list.html'
    '''
def post_list(request):
    object_list = Post.published.all()
    paginator =Paginator(object_list,3)  #3 posts in each page
    page = request.GET.get('page')
    try:
        #if page is not an integer deliver the first page
        posts = paginator.page(1)
    except EmptyPage:
        #if page is out of range deliver last page of redults
        posts = paginator.page(paginator.num_pages)
    return render(request,'blog/post/list.html',{'posts':posts})
'''
def post_detail(request,year,month,day,post):
    post = get_object_or_404(Post,slug=post,status='published',publish__year=year,publish__month=month,publish__day=day)
    return render(request,'blog/post/detail.html',{'post':post})
'''
def post_share(request,post_id):
    #retrieve post by id
    post =get_object_or_404(Post,id=post_id,status='published')
    if request.method=='POST':
        #Form was submitted
        from=EmailPostForm(request.POST)
        if form.is_valid():
            #Form field passed validation
            cd = form.cleaned_data
            #send email
        else:
            form =EmailPostForm()
        return render(request,'blog/post/share.html',{'post':post,'form':form})
'''
