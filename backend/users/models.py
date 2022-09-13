from django.db import models

from django.contrib.auth.models import AbstractUser, BaseUserManager


class UserManager(BaseUserManager):
    def create_user(self, email, address, username, password=None):
        if not email:
            raise ValueError("계정 이메일을 입력해주세요.")
        if not password:
            raise ValueError("비밀번호를 입력해주세요.")
        if not username:
            raise ValueError("유저이름을 입력해주세요.")
        if not address:
            raise ValueError("주소를 입력해주세요.")

        user = self.model(
            email = email,
            password = password,
            username = username,
            address = address
        )

        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, username, address, password=None):
        user = self.create_user(
            email = email,
            password = password,
            username = username,
            address = address
        )

        user.is_staff = True
        user.is_superuser = True

        user.save(using=self._db)
        return user


class User(AbstractUser):
    email = models.CharField(max_length=120, unique=True)
    address = models.CharField(max_length=100)
    username = models.CharField(max_length=100)

    # status
    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=True)

    objects = UserManager()

    class Meta:
        db_table = "users"