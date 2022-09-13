from django.db                     import models
from django.contrib.auth.base_user import AbstractBaseUser, BaseUserManager

from core.models     import TimeStampModel
from products.models import Product


class UserManager(BaseUserManager):
    """유저매니저 정의"""

    def create_user(self, email, password, **extra_fields):
        if not email:
            raise ValueError(_("Users must have an email address"))
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save()
        return user

    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError(_("Superuser must have is_staff=True."))
        if extra_fields.get("is_superuser") is not True:
            raise ValueError(_("Superuser must have is_superuser=True."))
        return self.create_user(email, password, **extra_fields)


class User(AbstractBaseUser, TimeStampModel):
    """
    유저 모델
    """
    email    = models.EmailField(max_length=120)
    username = models.CharField(max_length=50)
    address  = models.CharField(max_length=120)
    is_staff = models.BooleanField(_("Is staff"), default=False)

    objects         = UserManager()
    USERNAME_FIELD  = "email"
    EMAIL_FIELD     = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name        = _("user")
        verbose_name_plural = _("users")
        db_table            = "users"

    def clean(self):
        super().clean()
        self.email = self.__class__.objects.normalize_email(self.email)



class Comment(TimeStampModel):
    """
    댓글 모델
    """
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user    = models.ForeignKey(User, on_delete=models.CASCADE)
    comment = models.CharField(max_length=200)
    
    class Meta:
        db_table = 'comments'

    def __str__(self):
        return self.product