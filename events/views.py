from django.shortcuts import render, get_object_or_404, reverse
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.views.generic import UpdateView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Post, Comment
from .forms import CommentForm


class EventList(generic.ListView):
    """
    Class for rendering finished events macro view in base.html

    Parameters:
    Html list view
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class EventDetail(View):
    """
    Class for rendering finished events micro view in base.html

    Parameters:
    Html list view from event
    Request:
    post_detail.html
    Returns:
    Html with events attributes with approved comments and likes
    """
    def get(self, request, slug, *args, **kwargs):
        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        return render(
            request,
            "post_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": False,
                "liked": liked,
                "comment_form": CommentForm()
            },
        )

    def post(self, request, slug, *args, **kwargs):

        queryset = Post.objects.filter(status=1)
        post = get_object_or_404(queryset, slug=slug)
        comments = post.comments.filter(approved=True).order_by("-created_on")
        liked = False
        if post.likes.filter(id=self.request.user.id).exists():
            liked = True

        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():
            comment_form.instance.email = request.user.email
            comment_form.instance.name = request.user.username
            comment = comment_form.save(commit=False)
            comment.post = post
            comment.save()
        else:
            comment_form = CommentForm()

        return render(
            request,
            "post_details.html",
            {
                "post": post,
                "comments": comments,
                "commented": True,
                "comment_form": comment_form,
                "liked": liked
            },
        )


class PostLike(View):
    """
    Class used to see if some user has liked the event

    Parameters:
    View
    Returns:
    Relod of base.html and post_detail.html with count of likes updated
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
        else:
            post.likes.add(request.user)

        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def delete_comment(request, comment_id):
    """
    Function for deleting a comment for logged user

    Parameters:
    request, comment id
    Returns:
    base.html with post_detail.html view updated with comment deleted
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    return HttpResponseRedirect(reverse(
        'post_detail', args=[comment.post.slug]))


class UpdateComment(LoginRequiredMixin, UpdateView):
    """
    Function for updating a comment for logged user

    Parameters:
    LoginRequiredMixin, UpdateView
    """
    model = Comment
    template_name = 'update_comment.html'
    form_class = CommentForm
