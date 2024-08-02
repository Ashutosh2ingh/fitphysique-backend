import re
from rest_framework import serializers
from .models import Customer, Navbar, HeroSlider, About, Achievement, Class, Trainer, Membership, Testimonial, Blog, Brand, FooterGallery, Footer

# Create your serializers here.
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = Customer
        fields = '__all__' 
    
    def validate_password(self, value):
        if not value.isalnum():
            raise serializers.ValidationError("Password should only contain alphabets and numbers.")
        return value

    def validate_first_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("First name should only contain alphabets.")
        return value

    def validate_last_name(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Last name should only contain alphabets.")
        return value
    
    def validate_country(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("Country should only contain alphabets.")
        return value
    
    def validate_city(self, value):
        if not value.isalpha():
            raise serializers.ValidationError("City should only contain alphabets.")
        return value
    
    def validate_state(self, value):
        if not all(char.isalpha() or char.isspace() for char in value):
            raise serializers.ValidationError("State should only contain alphabets.")
        return value
    
    def validate_address(self, value):
        if not re.match(r'^[a-zA-Z0-9\s/-]+$', value):
            raise serializers.ValidationError("Address contains invalid characters. Only letters, digits, spaces, slashes, hyphens, and periods are allowed.")
        return value
    
    def validate_phone(self, value):
        if not str(value).isdigit():
            raise serializers.ValidationError("Phone number should only contain digits.")
        return value
    
    def validate_zip(self, value):
        if not str(value).isdigit():
            raise serializers.ValidationError("Zip number should only contain digits.")
        return value


# Navbar Serializer
class NavbarSerializer(serializers.ModelSerializer):
    class Meta:
        model = Navbar
        fields = '__all__'


# Slider Serializer
class HeroSliderSerializer(serializers.ModelSerializer):
    class Meta:
        model = HeroSlider
        fields = '__all__'


# About Serializer
class AboutSerializer(serializers.ModelSerializer):
    class Meta:
        model = About
        fields = '__all__'


# Achievement Serializer
class AchievementSerializer(serializers.ModelSerializer):
    class Meta:
        model = Achievement
        fields = '__all__'


# Class Serializer
class ClassSerializer(serializers.ModelSerializer):
    class Meta:
        model = Class
        fields = '__all__'


# Trainer Serializer
class TrainerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Trainer
        fields = '__all__'


# Membership Serializer
class MembershipSerializer(serializers.ModelSerializer):
    class Meta:
        model = Membership
        fields = '__all__'


# Testimonial Serializer
class TestimonialSerializer(serializers.ModelSerializer):
    class Meta:
        model = Testimonial
        fields = '__all__'


# Blog Serializer
class BlogSerializer(serializers.ModelSerializer):
    class Meta:
        model = Blog
        fields = '__all__'


# Brand Serializer
class BrandSerializer(serializers.ModelSerializer):
    class Meta:
        model = Brand
        fields = '__all__'


# Footer Gallery Serializer
class FooterGallerySerializer(serializers.ModelSerializer):
    class Meta:
        model = FooterGallery
        fields = '__all__'


# Footer Serializer
class FooterSerializer(serializers.ModelSerializer):
    gallery = FooterGallerySerializer(many=True, read_only=True)

    class Meta:
        model = Footer
        fields = '__all__'