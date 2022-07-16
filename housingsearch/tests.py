

# Create your tests here.
from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse
from .models import Review, Housing, Rating, Profile, Post, Comment
#Source: https://www.youtube.com/watch?v=ljG1WzBAboQ
class BaseTest(TestCase):
    def setUp(self):
        self.login_url = reverse('logout')
# class LoginTest(BaseTest):

#     def test_login(self):
# #         # c = Client()
# #         # c.login(username="tester", password="password123")
# #         # User = get_user_model()
# #         # user = User.objects.get(username="tester")
# #         # self.assertTrue(user.is_authenticated)
# #         # c.logout()
# #         # self.assertFalse(user.is_anonymous)
#         response = self.client.get(self.login_url)
#         self.assertEqual(response.status_code, 301)
#         #self.assertTemplateUsed(response, 'home.html')


class ReviewTest(TestCase):
    def test_review(self):
        # c = Client()

        housing = Housing.objects.create(id=1,address="address1", rent="500", bed="3", bath="3", sqft="1000")
        review = Review.objects.create(review_text="good house", housing_id=housing.id)
        #review.housing_id = housing.pk
        #response = self.client.get(reverse('detail'), args=(1,), kwargs={'pk': "1"})
        self.assertEqual(review.housing_id, housing.id)
    def test_no_review(self):
        # c = Client()

        housing = Housing.objects.create(id=1,address="address1", rent="500", bed="3", bath="3", sqft="1000")
        review = Review.objects.create(review_text="", housing_id=housing.id)
        #review.housing_id = housing.pk
        #response = self.client.get(reverse('detail'), args=(1,), kwargs={'pk': "1"})
        self.assertEqual(review.review_text, "")
class RatingTest(TestCase):
    def test_rating(self):
        # c = Client()

        housing = Housing.objects.create(id=1,address="address1", rent="500", bed="3", bath="3", sqft="1000")
        rating = Rating.objects.create(rate_text="3", rate=2,housing_id=housing.id)
        #review.housing_id = housing.pk
        #response = self.client.get(reverse('detail'), args=(1,), kwargs={'pk': "1"})
        self.assertEqual(rating.housing_id, housing.id)
    def test_rate(self):
        # c = Client()

        housing = Housing.objects.create(id=1,address="address1", rent="500", bed="3", bath="3", sqft="1000")
        rating = Rating.objects.create(rate_text="3", rate=2, housing_id=housing.id)
        #review.housing_id = housing.pk
        #response = self.client.get(reverse('detail'), args=(1,), kwargs={'pk': "1"})
        self.assertEqual(rating.rate, 2)

class MapTest(TestCase):
    def test_marker_redirect_to_address_page(self):
        housing = Housing.objects.create(id=1, address="address1", rent="500", bed="3", bath="3", sqft="1000")

class ProfileTest(TestCase):
    def test_age(self):
        prof = Profile.objects.create(username="",age="21", gender= " ", school_year=" ")
        self.assertEqual(prof.age, "21")
    def test_gender(self):
        prof = Profile.objects.create(username="",age="", gender= "Other", school_year=" ")
        self.assertEqual(prof.gender, "Other")
    def test_school_year(self):
        prof = Profile.objects.create(username="",age="", gender= "", school_year="Second Year")
        self.assertEqual(prof.school_year, "Second Year")

class RoommateFinder(TestCase):
    def post_body(self):
        post = Post.objects.create(id=1, author="benny", content="this is a post")
        self.assertEqual(post.content,"this is a post")

    def post_author(self):
        post = Post.objects.create(id=1, author="benny", content="this is a post")
        self.assertEqual(post.author,"benny")
    

