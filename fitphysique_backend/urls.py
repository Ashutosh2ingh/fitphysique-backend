from django.contrib import admin
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from gym.views import NavbarView,HeroSliderView,AboutView,AchievementView,ClassView,TrainerView,MembershipView,TestimonialView,BlogView,BrandView,FooterView,RegisterView,LoginView,LogoutView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', LoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(), name='logout'),
    path('gym/navbar/', NavbarView.as_view(), name='navbar'),
    path('gym/heroslider/', HeroSliderView.as_view(), name='hero_slider'),
    path('gym/about/', AboutView.as_view(), name='about'),
    path('gym/achievement/', AchievementView.as_view(), name='achievement'),
    path('gym/class/', ClassView.as_view(), name='class'),
    path('gym/trainer/', TrainerView.as_view(), name='trainer'),
    path('gym/membership/', MembershipView.as_view(), name='membership'),
    path('gym/testimonial/', TestimonialView.as_view(), name='testimonial'),
    path('gym/blog/', BlogView.as_view(), name='blog'),
    path('gym/brand/', BrandView.as_view(), name='brand'),
    path('gym/footer/', FooterView.as_view(), name='footer'),
]+static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
