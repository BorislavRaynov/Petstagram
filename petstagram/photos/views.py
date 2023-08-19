from django.shortcuts import render, redirect
from petstagram.photos.models import Photo
from petstagram.photos.forms import PhotoCreateForm, PhotoEditForm
from petstagram.common.forms import CommentForm
# Create your views here.


def photo_add(request):
    form = PhotoCreateForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('index')

    context = {'form': form}

    return render(request, template_name='photos/photo-add-page.html', context=context)

def photo_details(request, pk):
    photo = Photo.objects.get(pk=pk)
    likes = photo.like_set.all()
    comments = photo.comment_set.all()
    comment_form = CommentForm()
    context = {
        "photo": photo,
        "likes": likes,
        'comment_form': comment_form,
        "comments": comments
    }
    return render(request, template_name='photos/photo-details-page.html', context=context)

def photo_edit(request, pk):
    form = PhotoEditForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        form.save()
        return redirect('photo-details')

    context = {'form': form}
    return render(request, template_name='photos/photo-edit-page.html', context=context)

def photo_delete(request, pk):
    photo = Photo.objects.get(pk=pk)
    photo.delete()
    return redirect('index')