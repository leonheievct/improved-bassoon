from rest_framework import serializers
from .models import Category,Tag,Post,Comment
from django.contrib.auth.models import User

# class UserSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = User
#         fields = ['id','username','email']

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = "__all__"

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "_-all__"


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = ['id','author','text','creat_at']
        read_only_fields = ['author','creat_at']  

# class PostCreateSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Post
#         fields = ['title','content','category']

class PostSerializer(serializers.ModelSerializer):
    # author = UserSerializer(read_only=True)  
    # category = CategorySerializer(read_only=True)
    # tag = TagSerializer(many=True,read_only=True)

    class Meta:
        model = Post
        fields = '__all__'
        # read_only = ['author','creat_at','updete_at']    
