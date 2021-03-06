from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.db import models


class UserManager(BaseUserManager):
    def create_user(self, email, password=None, **extra_fields):
        if not email:
            raise ValueError("User must have an Email Address")

        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password, name):
        user = self.create_user(email=email, password=password, name=name)
        user.is_superuser = True
        user.is_staff = True
        user.save(using=self._db)
        return user


class User(AbstractBaseUser, PermissionsMixin):
    email = models.EmailField(max_length=255, unique=True)
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    handle_verified = models.BooleanField(default=False)
    is_gfg = models.BooleanField(default=False)

    objects = UserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['name']

    def __str__(self):
        return self.name


class GFGData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    gfg_handle = models.CharField(max_length=255)
    total_questions = models.IntegerField(default=0)
    coding_score = models.IntegerField(default=0)
    school = models.IntegerField(default=0)
    basic = models.IntegerField(default=0)
    easy = models.IntegerField(default=0)
    medium = models.IntegerField(default=0)
    hard = models.IntegerField(default=0)

    class Meta:
        verbose_name = "GFG Data"
        verbose_name_plural = "GFG Data"

    def __str__(self):
        return f'{self.user.name}\'s GFG Data'


class LeetcodeData(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True)
    leetcode_handle = models.CharField(max_length=255)
    total_questions = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    easy = models.IntegerField(default=0)
    medium = models.IntegerField(default=0)
    hard = models.IntegerField(default=0)

    class Meta:
        verbose_name = "Leetcode Data"
        verbose_name_plural = "Leetcode Data"

    def __str__(self):
        return f'{self.user.name}\'s Leetcode Data'


class DailyGFGData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_questions = models.IntegerField(default=0)
    coding_score = models.IntegerField(default=0)
    school = models.IntegerField(default=0)
    basic = models.IntegerField(default=0)
    easy = models.IntegerField(default=0)
    medium = models.IntegerField(default=0)
    hard = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Daily GFG Data"
        verbose_name_plural = "Daily GFG Data"

    def __str__(self):
        return f'{self.user.name}\'s Daily GFG Data'


class DailyLeetcodeData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    total_questions = models.IntegerField(default=0)
    points = models.IntegerField(default=0)
    easy = models.IntegerField(default=0)
    medium = models.IntegerField(default=0)
    hard = models.IntegerField(default=0)
    date = models.DateField(auto_now_add=True)

    class Meta:
        verbose_name = "Daily Leetcode Data"
        verbose_name_plural = "Daily Leetcode Data"

    def __str__(self):
        return f'{self.user.name}\'s Daily Leetcode Data'
