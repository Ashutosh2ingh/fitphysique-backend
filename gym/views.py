from rest_framework import generics
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Customer, Navbar, HeroSlider, About, Achievement, Class, Trainer, Membership, Testimonial, Blog, Brand, Footer
from .serializers import NavbarSerializer, HeroSliderSerializer, AboutSerializer, AchievementSerializer, ClassSerializer, TrainerSerializer, MembershipSerializer, TestimonialSerializer, BlogSerializer, BrandSerializer, FooterSerializer, UserSerializer
from rest_framework.authtoken.models import Token
from django.contrib.auth import authenticate,login
from rest_framework.decorators import authentication_classes, permission_classes
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated

# Create your views here.

# Create Register View
class RegisterView(APIView):
    def post(self, request, *args, **kwargs):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user_data = serializer.validated_data
            user = Customer.objects.create_user(
                email=user_data['email'],
                password=user_data['password'],
                first_name=user_data['first_name'],
                last_name=user_data['last_name'],
                country=user_data['country'],
                address=user_data['address'],
                city=user_data['city'],
                state=user_data['state'],
                zip=user_data['zip'],
                phone=user_data['phone']
            )
            return Response({
                'status':200,
                'message':'Registration Successful',
            })
        return Response({
            'status':400,
            'message':'Something went wrong',
            'error':serializer.errors
        })


# Create Login View
class LoginView(APIView):
    def post(self, request, *args, **kwargs):
        email=request.data.get('email')
        password=request.data.get('password')

        user=authenticate(email=email,password=password)
        if user is not None:
            login(request,user)
            token,created=Token.objects.get_or_create(user=user)
            return Response({
                'status':200,
                'message':'Login Successful',
                'user_id':user.id,
                'first_name':user.first_name,
                'last_name':user.last_name,
                'email':user.email,
                'token':token.key
            })
        return Response({
            'status':400,
            'message':'Invalid credentials'
        })
    

# Create Logout View
@authentication_classes([TokenAuthentication])
@permission_classes([IsAuthenticated])
class LogoutView(APIView):
    def post(self, request, *args, **kwargs):
        user = request.user
        Token.objects.filter(user=user).delete()
        return Response({
            "status": 200,
            "message": "Logout Successful"
        })


# Create Navbar View  
class NavbarView(generics.ListAPIView):
    queryset = Navbar.objects.all()
    serializer_class = NavbarSerializer


# Create Slider View  
class HeroSliderView(generics.ListAPIView):
    queryset = HeroSlider.objects.all()
    serializer_class = HeroSliderSerializer


# Create About View  
class AboutView(generics.ListAPIView):
    queryset = About.objects.all()
    serializer_class = AboutSerializer


# Create Achievement View  
class AchievementView(generics.ListAPIView):
    queryset = Achievement.objects.all()
    serializer_class = AchievementSerializer


# Create Class View  
class ClassView(generics.ListAPIView):
    queryset = Class.objects.all()
    serializer_class = ClassSerializer


# Create Trainer View  
class TrainerView(generics.ListAPIView):
    queryset = Trainer.objects.all()
    serializer_class = TrainerSerializer


# Create Membership View  
class MembershipView(generics.ListAPIView):
    queryset = Membership.objects.all()
    serializer_class = MembershipSerializer


# Create Membership View  
class TestimonialView(generics.ListAPIView):
    queryset = Testimonial.objects.all()
    serializer_class = TestimonialSerializer


# Create Blog View  
class BlogView(generics.ListAPIView):
    queryset = Blog.objects.all()
    serializer_class = BlogSerializer


# Create Brand View  
class BrandView(generics.ListAPIView):
    queryset = Brand.objects.all()
    serializer_class = BrandSerializer


# Create Footer View
class FooterView(generics.ListAPIView):
    queryset = Footer.objects.all()
    serializer_class = FooterSerializer