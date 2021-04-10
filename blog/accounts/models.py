from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

# User Manager
class UserManager(BaseUserManager):

    def create_user(self, ID, email, password):

        if not ID:
            raise ValueError('User mush have an own ID')

        if not email:
            raise ValueError('User must have an own email')

        user = self.model(
            # 1. normalize 2. return lower case email
            ID = ID,
            email = self.normalize_email(email),
        )

        user.set_password(password)
        user.save()
        return user


    def create_superuser(self, ID, email, password):

        user = self.model(
            ID = ID,
            email = email,
            password = password,
        )

        user.is_admin = True
        user.save()
        return user

# Custon User Model.
class User(AbstractBaseUser):
    # ID
    ID = models.CharField(
        verbose_name = 'ID',
        max_length = 50,
        unique=True,
        primary_key=True, # django 내에서 자체적으로 indexing 하기 위해 ID 라는 필드를 사용함
    )

    # E-mail
    email = models.EmailField(
        verbose_name ='email address',
        max_length = 50,
        unique=True,
    )

    is_admin = models.BooleanField(default=False)

    objects = UserManager()

    # model identifier
    USERNAME_FIELD = 'ID'
    REQUIRED_FIELDS = ['email']


    class Meta:
        verbose_name = 'user'
        ordering = ['ID']

    def __str__(self):
        return self.ID
