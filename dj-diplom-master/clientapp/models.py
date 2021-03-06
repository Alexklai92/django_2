from django.db import models
from django.contrib.auth.models import (
    BaseUserManager, AbstractBaseUser
)
from django.urls import reverse


class MyUserManager(BaseUserManager):
    def create_user(self, email, password=None):
        if not email:
            raise ValueError('Users must have an email address')

        user = self.model(
            email=self.normalize_email(email),
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, email, password):
        user = self.create_user(
            email,
            password=password,
        )
        user.is_admin = True
        user.save(using=self._db)
        return user


class MyUser(AbstractBaseUser):
    email = models.EmailField(
        verbose_name='email address',
        max_length=255,
        unique=True,
    )
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    objects = MyUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    def __str__(self):
        return self.email

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class Category(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name

    def get_absolute_url(self):
        return reverse('category', kwargs={'slug': self.slug})


def image_folder(instance, filename):
    filename = instance.slug + '.' + filename.split('.')[1]
    return '{0}/{1}'.format(instance.slug, filename)


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    title = models.CharField(max_length=120)
    slug = models.SlugField()
    description = models.TextField()
    image = models.ImageField(upload_to=image_folder)
    price = models.DecimalField(max_digits=9, decimal_places=2)



    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('product', kwargs={'slug': self.slug})


class CartItem(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    qty = models.PositiveIntegerField(default=1)

    def __str__(self):
        return 'Cart item for product {0}'.format(self.product.title)

    def change_number_product(self, qty):
        self.qty = qty
        self.save()


class Cart(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(CartItem, blank=True)

    def __str__(self):
        return "Корзина {}".format(self.user)

    def add_to_cart(self, slug):
        product = Product.objects.get(slug=slug)
        new_item = CartItem.objects.get_or_create(product=product)
        if new_item not in self.items.all():
            self.items.add(new_item[0])
            self.save()

    def remove_from_cart(self, slug):
        product = Product.objects.get(slug=slug)
        for cart_item in self.items.all():
            if cart_item.product == product:
                self.items.remove(cart_item)
                cart_item.qty = 1
                cart_item.save()
                self.save()


class Order(models.Model):
    user = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    items = models.ManyToManyField(Product, blank=True)
    count = models.IntegerField(default=0)
    order_total = models.DecimalField(max_digits=9, decimal_places=2,
                                     default=0.00)
    date_creation = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "Заказ №{}".format(str(self.id))

    def order_registration(self, cart, user):
        self.user = user
        for item in cart.items.all():
            self.count += item.qty
            item.qty = 1
            item.save()
            self.order_total += float(item.product.price)*item.qty
        self.save()
        for item in cart.items.all():
            self.items.add(item.product)
        self.save()
        cart.delete()

    class Meta:
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'
        ordering = ('date_creation',)


class Article(models.Model):
    title = models.CharField(max_length=120)
    description = models.CharField(max_length=500)
    product = models.ManyToManyField(Product, blank=True)
    date_creation = models.DateTimeField()

    def __str__(self):
        return self.title


class AnonymousReviews(models.Model):
    name = models.CharField(max_length=120)
    description = models.CharField(max_length=500, blank=True)
    mark = models.PositiveIntegerField()
    product = models.ForeignKey(Product, blank=True,
                                          on_delete=models.CASCADE)

    def __str__(self):
        return 'Анонимный отзыв №{}'.format(self.id)

    class Meta:
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'
