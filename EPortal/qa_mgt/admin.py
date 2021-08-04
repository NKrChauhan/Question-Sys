from django.contrib import admin
from .models import QuestionBank,ResposeBank,UserScore
# Register your models here.

admin.site.register(QuestionBank)
admin.site.register(ResposeBank)
admin.site.register(UserScore)