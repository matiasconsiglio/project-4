from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib import messages
from django.views import generic, View
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from .models import Post, Comment
from .forms import CommentForm, ContactForm


class EventList(generic.ListView):
    """
    Class for rendering finished events macro view in base.html.
    """
    model = Post
    queryset = Post.objects.filter(status=1).order_by('-created_on')
    template_name = 'index.html'
    paginate_by = 6


class EventDetail(View):
    """
    Class for rendering finished events micro view in base.html.
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
            messages.success(request, "Your comment is waiting for approval.")
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
    Class used to see if some user has liked the event.
    """
    def post(self, request, slug, *args, **kwargs):
        post = get_object_or_404(Post, slug=slug)
        if post.likes.filter(id=request.user.id).exists():
            post.likes.remove(request.user)
            messages.success(request, "1.")
        else:
            post.likes.add(request.user)
            messages.success(request, "2.")
        messages.success(request, "3.")
        return HttpResponseRedirect(reverse('post_detail', args=[slug]))


@login_required
def delete_comment(request, comment_id):
    """
    Function for deleting a comment for logged user.

    Parameters:
    request, comment id
    Returns:
    base.html with post_detail.html view updated with comment deleted
    """
    comment = get_object_or_404(Comment, id=comment_id)
    comment.delete()
    messages.success(request, "Your comment was successfully deleted.")
    return HttpResponseRedirect(reverse(
        'post_detail', args=[comment.post.slug]))


@login_required
def update_comment(request, comment_id):
    comment = get_object_or_404(Comment, id=comment_id)
    form = CommentForm(instance=Comment.objects.get(id=comment_id), data=request.POST)
    if request.method == 'POST':
        if form.is_valid():
            new_form = form.save(commit=False)
            new_form.approved = False
            new_form.save()
        messages.success(request, "Your comment is waiting for approval.")
        return redirect(reverse('home'))

    return render(request, 'update_comment.html', {'form': form})

def contact_form(request):
    """
    View for contact form
    """
    form = ContactForm()
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Your message was sent successfully.")
        return redirect(reverse('home'))

    context = {
        'form': form
    }
    return render(request, 'contact_form.html', context)
