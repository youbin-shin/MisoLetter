from django.db import models


class User(models.Model):    
    id = models.IntegerField(primary_key=True)
    username = models.CharField(max_length=32)
    password = models.CharField(max_length=32)
    email = models.CharField(max_length=68)
    status = models.IntegerField() # enum으로 변경하기
    is_staff = models.BooleanField()
    last_login = models.DateTimeField()
    date_joined = models.DateTimeField(auto_now_add=True)
    leaved = models.DateTimeField()
    created = models.DateTimeField(auto_now_add=True)
    

class Profile(models.Model):
    id = models.IntegerField(primary_key=True)
    nickname = models.CharField(max_length=25)
    user_id = models.ForeignKey("User", related_name="user", on_delete=models.CASCADE, db_column='user_id')
    profile_url = models.CharField(max_length=100)
    info = models.CharField(max_length=10)
    birth_date = models.DateField()




