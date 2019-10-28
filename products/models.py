from django.db import models
from django.conf import settings

from likert_field.models import LikertField
from products.choices import *


# Create your models here.
class Product(models.Model):
    # 분류는 어떻게 나눠야 하는지 모르겠음.
    name = models.CharField(max_length=400)
    image = models.ImageField()
    # 패키지 정보
    package = models.IntegerField(blank=True)
    width = models.IntegerField(blank=True)
    height = models.IntegerField(blank=True)
    length = models.IntegerField(blank=True)
    diameter = models.IntegerField(blank=True)
    weight = models.IntegerField(blank=True)
    # 제품정보
    feature = models.TextField(blank=True)
    construction = models.TextField(blank=True)
    safty = models.TextField(blank=True)
    care = models.TextField(blank=True)
    designer = models.CharField(max_length=100)
    price = models.IntegerField()
    color = models.CharField(max_length=50)
    #재질 및 환경
    material = models.TextField()
    environment = models.TextField(blank=True)
    document = models.FileField(blank=True)
    # M:N
    like_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='like_products', blank=True)
    basket_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='basket_products', blank=True)

class Comment(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    # score = LikertField(blank=False)
    score = models.IntegerField(choices=STATUS_CHOICES)
    title = models.CharField(max_length=100, blank=True)
    content = models.TextField()
    recommend = models.IntegerField(choices=RELEVANCE_CHOICES, blank=True)  # 추천
    value_for_money = models.IntegerField(choices=STATUS_CHOICES, blank=True)   # 가성비
    quality = models.IntegerField(choices=STATUS_CHOICES, blank=True)   # 품질
    design = models.IntegerField(choices=STATUS_CHOICES, blank=True)    # 외관
    furnish = models.IntegerField(choices=STATUS_CHOICES, blank=True)   # 조립/설치
    function = models.IntegerField(choices=STATUS_CHOICES, blank=True)  # 기능
    # 1:N
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    # M:N
    reference_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='reference_comments', blank=True)
    unreference_users = models.ManyToManyField(settings.AUTH_USER_MODEL, related_name='unreference_comments', blank=True)



