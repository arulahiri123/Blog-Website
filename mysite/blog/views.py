from django.shortcuts import render,get_object_or_404,redirect
from django.views.generic import TemplateView,ListView,DetailView,CreateView,UpdateView,DeleteView
from blog.models import Comment, Post
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.decorators import login_required
from blog.forms import CommentForm,PostForm
from django.urls import reverse_lazy

# Create your views here.
class AboutView(TemplateView):
    template_name = 'blog/about.html'

class PostListView(ListView):
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__lte = timezone.now()).order_by('-publish_date')


class PostDetailView(DetailView):
    model = Post

class CreatePost(LoginRequiredMixin, CreateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post

class UpdatePost(LoginRequiredMixin, UpdateView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    form_class = PostForm
    model = Post


class DeletePost(LoginRequiredMixin, DeleteView):
    model = Post
    success_url = reverse_lazy('post_list')

class DraftListPost(LoginRequiredMixin, ListView):
    login_url = '/login/'
    redirect_field_name = 'blog/post_detail.html'
    model = Post

    def get_queryset(self):
        return Post.objects.filter(publish_date__isnull = True)

##################
##################
@login_required
def post_publish(req,pk):
    post = get_object_or_404(Post, pk =pk)
    post.pulish()
    return redirect('post_detail',pk = pk)


@login_required
def add_comment_to_post(req, pk):
    post = get_object_or_404(Post, pk=pk)

    if req.method == 'POST':
        form = CommentForm(req.POST)

        if form.is_valid():
            comment = form.save(commit = False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk =post.pk)
    else:

        form = CommentForm()
    return render(req,'blog/comment_form.html',{'form':form})



@login_required
def comment_approve(req, pk):
    comment = get_object_or_404(Comment, pk= pk)
    comment.approve()
    return redirect('post_detail',pk = comment.post.pk)

@login_required
def comment_remove(req,pk):
    comment = get_object_or_404(Comment, pk = pk)
    post_pk = comment.post.pk
    comment.delete()
    return redirect('post_detail',pk = post_pk)
