from django.db import models
from django.contrib.auth.models import (
  AbstractBaseUser, BaseUserManager
)
from django.conf import settings

# Django DOC that custom user model
# https://docs.djangoproject.com/ja/4.0/topics/auth/customizing/#specifying-a-custom-user-model

# AbstractBaseUser
# https://docs.djangoproject.com/ja/4.0/topics/auth/customizing/#specifying-a-custom-user-model

# PermissionMixIn
# https://docs.djangoproject.com/ja/4.0/topics/auth/customizing/#custom-users-and-permissions


# authenticate with Email & pass
class CustomUserManager(BaseUserManager):
  # BaseUserManagerをオーバーライド
  def create_user(self, email, date_of_birth, password=None):
    if not email:
      raise ValueError("this field can't be blank")

    # データを正規化（validation）してから入力
    user = self.model(
      email=self.normalize_email(email),
      date_of_birth=date_of_birth,
    )
    user.set_password(password)
    user.save(using=self._db)
    return user

  def create_superuser(self, email, date_of_birth, password=None):
    user = self.create_user(
      email,
      password=password,
      date_of_birth=date_of_birth,
    )
    user.is_admin = Trueuser.save(using=self._db)
    return user

class CustomUser(AbstractBaseUser):
  email = models.EmailField(
    verbose_name='メールアドレス',
    max_length=255,
    unique=True,
  )
  date_of_birth = models.DateField()
  is_active = models.BooleanField(default=True)
  is_admin = models.BooleanField(default=False)

  objects = CustomUserManager()

  USERNAME_FIELD = 'email'
  REQUIRED_FIELDS = ['date_of_birth']

  def __str__(self):
      return self.email
