from django.contrib.auth.models import AbstractBaseUser,BaseUserManager,PermissionsMixin
from django.db import models 
from django.conf import settings

class UserManager(BaseUserManager):  

    use_in_migrations = True    

    def create_user(self, email, nickname, password=None):        
        if not email :            
            raise ValueError('must have user email')        
        user = self.model(            
            email = self.normalize_email(email),            
            nickname = nickname        
        )        
        user.set_password(password)        
        user.save(using=self._db)        
        return user

    def create_superuser(self, email, nickname, password ):        

        user = self.create_user(            
            email = self.normalize_email(email),            
            nickname = nickname,            
            password=password        
        )        
        user.is_admin = True        
        user.is_superuser = True        
        user.is_staff = True        
        user.save(using=self._db)        
        return user 


class User(AbstractBaseUser,PermissionsMixin):    

    objects = UserManager()
    username = None
    email = models.EmailField(verbose_name='email', unique=True)
    nickname = models.CharField(
        max_length=20,
        null=False,
        unique=True
    )
    date_joined = models.DateTimeField(auto_now_add=True)     
    USERNAME_FIELD = 'email'    # 유저 아이디를 이메일로 변경
    REQUIRED_FIELDS = ['nickname']  # 필수 입력 값 설정
    is_superuser = models.BooleanField(default=False)    
    is_staff = models.BooleanField(default=False)     