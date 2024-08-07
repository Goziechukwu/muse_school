from django.db import models
from django.contrib.auth.models import User


class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category',
        null=True,
        blank=True,
        on_delete=models.SET_NULL
    )
    sku = models.CharField(
        max_length=254,
        null=True,
        blank=True
    )
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(
        max_digits=6,
        decimal_places=2
    )
    rating = models.DecimalField(
        max_digits=6,
        decimal_places=2,
        null=True,
        blank=True
    )
    image = models.ImageField(
        upload_to='products/',
        null=True,
        blank=True
    )

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey(
        Product,
        on_delete=models.CASCADE,
        related_name='reviews'
    )
    user = models.ForeignKey(
        User,
        on_delete=models.SET_NULL,
        null=True,
        blank=True
    )
    rating = models.IntegerField(
        choices=[(i, str(i)) for i in range(1, 6)]  # Ratings 1-5
    )
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)


    def __str__(self):
        return (f'Review for {self.product.name} by '
                f'{self.user.username if self.user else "Anonymous"}')

