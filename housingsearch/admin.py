from django.contrib import admin
from .models import Housing, Rating, Review, Profile, Post, Comment
class RatingInline(admin.TabularInline):
    #...
    model = Rating
    #extra = 3
class ReviewInline(admin.TabularInline):
    #...
    model = Review
    #extra = 3
class HousingAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,               {'fields': ['address', 'lat', 'long', 'rent', 'bath', 'bed', 'sqft', 'image']}),
    ]
    inlines = [RatingInline, ReviewInline]
    #list_display = ('address')
    search_fields = ['address']
admin.site.register(Housing, HousingAdmin)
admin.site.register(Profile)

class PostAdmin(admin.ModelAdmin):
    list_display = ('title', 'slug', 'status',)
    list_filter = ('status',)
    search_fields = ('title', 'content',)
admin.site.register(Post, PostAdmin)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('name', 'body', 'post', 'created_on', 'active')
    list_filter = ('active', 'created_on')
    search_fields = ('name', 'body')