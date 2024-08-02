from django.contrib import admin
from .models import Customer, Navbar, HeroSlider,About,Achievement,Class,Trainer, Membership,Testimonial,Blog,Brand,FooterGallery,Footer

# Register your models here.

# Register Customer 
@admin.register(Customer)
class CustomerAdmin(admin.ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'phone')


# Register Navbar
@admin.register(Navbar)
class NavbarAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'target', 'offset')


# Register Navbar
@admin.register(HeroSlider)
class SliderAdmin(admin.ModelAdmin):
    list_display = ('id','heading', 'paragraph')


# Register About
@admin.register(About)
class AboutAdmin(admin.ModelAdmin):
    list_display = ('id','icon', 'title', 'subtitle')


# Register Achievement
@admin.register(Achievement)
class AchievementAdmin(admin.ModelAdmin):
    list_display = ('id','icon', 'title', 'award')


# Register Class
@admin.register(Class)
class ClassAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'description')


# Register Trainer
@admin.register(Trainer)
class TrainerAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'role', 'description')


# Register Membership
@admin.register(Membership)
class MembershipAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'price')


# Register Testimonial
@admin.register(Testimonial)
class TestimonialAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'message')


# Register Blog
@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('id','title', 'link', 'date')


# Register Brand
@admin.register(Brand)
class BrandAdmin(admin.ModelAdmin):
    list_display = ('id','name', 'link')


# Register Footer Gallery
@admin.register(FooterGallery)
class FooterGalleryAdmin(admin.ModelAdmin):
    list_display = ('id', 'image')


# Register Footer
@admin.register(Footer)
class FooterAdmin(admin.ModelAdmin):
    list_display = ('title', 'location', 'contact', 'email')