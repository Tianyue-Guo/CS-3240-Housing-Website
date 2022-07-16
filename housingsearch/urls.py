from django.urls import path
from django.views.generic import TemplateView

from . import views
from django.conf import settings
from django.contrib.staticfiles.urls import static
app_name = ''
urlpatterns = [
    path('', views.index, name='index'),
    path('housing/<int:housing_id>/', views.housing_detail_view, name='detail'),
    path('housing/<int:housing_id>/rate/', views.rate, name='rate'),
    path('home/', views.HomePageView.as_view(), name='home'),
    path('accounts/login', views.HousingLogoutView.as_view(), name='logout'),
    path('home/advice/', views.housing_advice_view.as_view(), name='advice'),
    path('home/saveAdvice', views.saveAdvice, name='save_advice'),
    path('home/advicePost', views.advice, name='advice_post'),
    path('home/roommatefinder/', views.PostList.as_view(), name='roommatefinder'),
    path('map/', views.MapView.as_view(), name='map'),
    path('profile/', views.profile_view, name='profile'),
    path('editprofile/', views.edit_profile_view, name='editprofile'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('home/post', views.make_post, name='make_post')
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)