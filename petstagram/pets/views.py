from django.shortcuts import render, redirect
from petstagram.pets.models import Pet
from petstagram.pets.forms import PetForm, PetDeleteForm
from petstagram.common.forms import CommentForm
# Create your views here.

def pet_add(request):
    form = PetForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('profile-details', pk=1)

    context = {'form': form}
    return render(request, template_name='pets/pet-add-page.html', context=context)

def pet_details(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    all_photos = pet.photo_set.all()
    comment_form = CommentForm()
    context = {
        "pet": pet,
        'comment_form': comment_form,
        "all_photos": all_photos
    }
    return render(request, template_name='pets/pet-details-page.html', context=context)

def pet_edit(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    if request.method == 'GET':
        form = PetForm(instance=pet, initial=pet.__dict__)
        print(pet.__dict__)

    else:
        form = PetForm(request.POST, instance=pet)
        if form.is_valid():
            form.save()
            return redirect('pet-details', username, pet_name)

    context = {'form': form}
    return render(request, template_name='pets/pet-edit-page.html', context=context)

def pet_delete(request, username, pet_name):
    pet = Pet.objects.get(slug=pet_name)
    if request.method == 'POST':
        pet.delete()
        return redirect('pet-details', pk=1)

    form = PetDeleteForm(__initial__=pet.__dict__)
    context = {'form': form}

    return render(request, template_name='pets/pet-delete-page.html', context=context)