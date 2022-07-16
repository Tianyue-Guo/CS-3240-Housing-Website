from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import generic
from django.contrib.auth.views import LogoutView
from django.views.generic import CreateView
from django.contrib.auth.models import User
from .models import Housing, Rating, Review, Profile, Post, AdvicePost
from django.utils import timezone
from django.urls import reverse
from django.utils import timezone
from django.contrib.auth.mixins import LoginRequiredMixin
from django.utils.text import slugify
from django.urls import reverse_lazy
from django.contrib import messages
from .forms import CommentForm, PostForm

def index(request):
    return HttpResponseRedirect('home')

class HomePageView(generic.ListView):
    #model = Housing
    template_name = "home.html"
    context_object_name = "housing_set"
    def get_queryset(self):
        return Housing.objects.all()

class HousingLogoutView(LogoutView):
    template_name = 'home.html'

class housing_advice_view(generic.ListView):
    template_name = 'advice.html'
    context_object_name = 'advice_list'

    def get_queryset(self):
        return AdvicePost.objects.all()

def advice(request):
    return render(request, 'make_advice.html')

# Form handler
def saveAdvice(request):
    selected_title = request.POST.get('title',"")
    selected_body = request.POST.get('body',"")
    if (not selected_title or not selected_body):
        return render(request, 'advice.html', {'error_message': "You didn't input a title and/or the text"})
    else:
        advice = AdvicePost(title=selected_title,body=selected_body)
        advice.save()
        return HttpResponseRedirect(reverse('advice'))
# DELETE THIS AND REPLACE WITH CLASS
def roommate_finder_view(request):
    return render(request, 'roommate.html')

# class HousingDetailView(generic.DetailView):
#     model = Housing
#     template_name = 'detail.html'
#     def get_queryset(self):
#         return Housing.objects.all()

def housing_detail_view(request, housing_id):
    housing = get_object_or_404(Housing, pk=housing_id)
    #queryset_profile = Profile.objects.filter(username=request.user.username)
    #profile = get_object_or_404(queryset_profile)
    #review = None
    # new_review = None
    # if request.method == 'POST':
    #     review = Review(data=request.POST)
    #     print(review)
    #     if review.is_valid():
    #         # Create Post object but don't save to database yet
    #         new_review = review.save(commit=False)
    #         new_review.name = request.user
    #         print(new_review)
    #         print(new_review.name)
    #         # Save the post to the database
    #         new_review.save()
    #print(Rating.objects.filter(housing_id=housing_id))
    rating = Rating.objects.filter(housing_id=housing_id)
    #review = Review.objects.filter(housing_id=housing_id)
    #print(Review.objects.filter(housing_id=housing_id))
    average = 0
    count = 0
    #profile = Profile.objects.get(username=request.user.username)
    for r in rating:
        count += r.rate
        average += int(r.rate_text) * r.rate
        #print(r.review_text)
    average /= count if count != 0 else 1
    average = float('%.3g' % average)
    #print(average)
    #review = rate_and_review.review_text
    return render(request, 'detail.html', {'housing':housing, 'rating': rating, 'average': average})

def rate(request, housing_id):
    housing = get_object_or_404(Housing, pk=housing_id)
    #review = get_object_or_404(Review, pk=housing_id)
    print("request.post", request.POST)
    try:
        selected_rate = housing.rating_set.get(pk=request.POST['choice'])
        #print("selected rate", selected_rate)
        review = Review()
        review.review_text = request.POST['review']
        review.name = request.user.username
        review.housing_id = housing_id
        #print(review, review.review_text, review.pk)
        review.save()
       # print(selected_rate.review_text)
    except (KeyError, Rating.DoesNotExist):
        # Redisplay the question voting form.
        return render(request, 'detail.html', {
            'housing': housing,
            'error_message': "You didn't select a rating.",
        })
    else:
        selected_rate.rate += 1
        selected_rate.save()

        # Always return an HttpResponseRedirect after successfully dealing
        # with POST data. This prevents data from being posted twice if a
        # user hits the Back button.
        return HttpResponseRedirect(reverse('detail', args=(housing.id,)))


class MapView(CreateView):
    model = Housing
    fields = ['address']
    template_name = 'map.html'
    success_url = '/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['addresses'] = Housing.objects.all()
        return context


def profile_view(request):
    #profile = get_object_or_404(Profile)

    if not Profile.objects.filter(username=request.user.username):
        profile = Profile()
        name = request.user.username
        profile.username = name
        profile.save()
    # if request.method == "POST":
    #     profile.age = request.POST['age']
    #     profile.gender = request.POST['gender']
    #     profile.save()
        return render(request, 'profile.html',{'profile': profile})
    else:
        queryset = Profile.objects.filter(username=request.user.username)
        profile = get_object_or_404(queryset)
        return render(request, 'profile.html', {'profile': profile})

def edit_profile_view(request):
    print(request.user)
    queryset = Profile.objects.filter(username=request.user.username)
    profile = get_object_or_404(queryset)
    print(profile)
    # profile = Profile()
    # name = request.user.username
    # profile.username = name
    if request.method == "POST":
        if request.POST['age'] :
            print(request.POST)
            profile.age = request.POST['age']

            print(request.POST)
            print(profile.age)


            profile.save()
        if request.POST['gender'] != "Choose...":
            profile.gender = request.POST['gender']
            print(profile.gender)
            profile.save()

        if request.POST['school_year'] != "Choose...":
            profile.school_year = request.POST['school_year']
            print(profile.school_year)
            profile.save()
        return HttpResponseRedirect('/profile')
    return render(request, 'editprofile.html',{'profile': profile})

class PostList(generic.ListView):
    """
    Return all posts that are with status 1 (published) and order from the latest one.
    """
    queryset = Post.objects.filter(status=1).order_by('-created_at')
    template_name = 'index.html'

def post_detail(request, slug):
    template_name = 'post_detail.html'
    post = get_object_or_404(Post, slug=slug)
    comments = post.comments.filter(active=True)
    new_comment = None
    # Comment posted
    if request.method == 'POST':
        comment_form = CommentForm(data=request.POST)
        if comment_form.is_valid():

            # Create Comment object but don't save to database yet
            new_comment = comment_form.save(commit=False)
            # Assign the current post to the comment

            new_comment.post = post
            new_comment.name = request.user
            # Save the comment to the database
            new_comment.save()
    else:
        comment_form = CommentForm()

    return render(request, template_name, {'post': post,
                                           'comments': comments,
                                           'new_comment': new_comment,
                                           'comment_form': comment_form})

def make_post(request):
    template_name = 'make_post.html'
    new_post = None
    
    if request.method == 'POST':
        post_form = PostForm(data=request.POST)
        #print(post_form)
        if post_form.is_valid():
            # Create Post object but don't save to database yet
            new_post = post_form.save(commit=False)
            new_post.author = request.user
            # Save the post to the database
            new_post.save()
    else:
        post_form = PostForm()

    return render(request, template_name, {'new_post': new_post,
                                           'post_form': post_form})



#Citations for HTMLs:
#https://getbootstrap.com/docs/5.1/examples/
#https://getbootstrap.com/docs/5.1/getting-started/introduction/
#Postgres: https://stackoverflow.com/questions/46416877/duplicate-key-issue-when-loading-back-json-file-postgresql,
#https://medium.com/djangotube/django-sqlite-to-postgresql-database-migration-e3c1f76711e1
