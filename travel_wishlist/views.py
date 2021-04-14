from django.shortcuts import render, redirect, get_object_or_404
from .models import Place
from .forms import NewPlaceForm, TripReviewForm
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseForbidden
from django.contrib import messages


@login_required()
def place_list(request):
    if request.method == 'POST':
        # create new place
        form = NewPlaceForm(request.POST)  # creating from data in request
        place = form.save(commit=False)  # creating a model object from form
        place.user = request.user
        if form.is_valid():  # validation against DB constraints
            place.save()  # saves place to DB
            return redirect('place_list')  # reloads home page

    places = Place.objects.all().filter(visited=False).order_by('name')
    new_place_form = NewPlaceForm()  # creates HTML
    return render(request, 'travel_wishlist/wishlist.html', {'places': places, 'new_place_form': new_place_form})


@login_required
def about(request):
    """ handles the About section """
    author = 'SvenJonis'
    about = 'A website to create a list of places to visit'
    return render(request, 'travel_wishlist/about.html', {'author': author, 'about': about})


@login_required
def places_visited(request):
    """ renders a list of visited places """
    visited = Place.objects.filter(user=request.user).filter(visited=True)  # loads all the places that have been
    # visited
    return render(request, 'travel_wishlist/visited.html', {'visited': visited})  # renders the visited page


@login_required
def place_was_visited(request, place_pk):
    """ changes status of a place to visited """
    if request.method == 'POST':
        place = get_object_or_404(Place, pk=place_pk)  # if the request is invalid returns 404 error
        if place.user == request.user:
            place.visited = True  # changes status to visited
            place.save()  # saves the change
        else:
            return HttpResponseForbidden()
    return redirect('place_list')  # reloads home page


@login_required
def place_details(request, place_pk):
    """ allows user to record a review of a visited place """
    place = get_object_or_404(Place, pk=place_pk)
    # does this place belong to the current user?
    if place.user != request.user:
        return HttpResponseForbidden()
    # is this a GET or POST request?
    if request.method == 'POST':
        form = TripReviewForm(request.POST, request.FILES, instance=place)
        if form.is_valid():
            form.save()
            messages.info(request, 'Trip information updated!')
        else:
            messages.error(request, form.errors)
        return redirect('place_details', place_pk=place_pk)
    else:
        # if GET request show place info and optional form
        if place.visited:
            review_form = TripReviewForm(instance=place)
            return render(request, 'travel_wishlist/place_detail.html', {'place': place, 'review_form': review_form})
        else:
            return render(request, 'travel_wishlist/place_detail.html', {'place': place})


@login_required
def delete_place(request, place_pk):
    """ allows user to delete a place  """
    if request.method == 'POST':
        place = get_object_or_404(Place, pk=place_pk)
        if place.user == request.user:
            place.delete()
            return redirect('place_list')
        else:
            return HttpResponseForbidden()
