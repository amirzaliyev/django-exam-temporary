from django.db.models import Model, ForeignKey, CASCADE, CharField, DecimalField, ImageField, TextField, PositiveIntegerField
from django.db.models.enums import IntegerChoices
from django.contrib.auth.models import  User


class CustomUser(User):
    phone_number = CharField(max_length=255)


# Create your models here.
class Book(Model):
    title = CharField(max_length=255)
    price = DecimalField(max_digits=12, decimal_places=2)
    author = ForeignKey('bookstore.Author', on_delete=CASCADE, related_name='books')

    # thumbnail = ImageField('books/thumbnail/')

    def __str__(self):
        return self.title


class Author(Model):
    first_name = CharField(max_length=50, null=True, blank=True)
    last_name = CharField(max_length=50, null=True, blank=True)
    alias = CharField(max_length=200, null=True, blank=True)

    @property
    def fullname(self):
        return self.first_name + " " + self.last_name

    @property
    def alias_or_fullname(self):
        """
        if alias exists
        it returns alias
        otherwise fullname
        """
        if self.alias is None:
            return self.fullname

        return self.alias

    def __str__(self):
        if self.alias:
            return self.alias

        return self.fullname


class Review(Model):
    class Ratings(IntegerChoices):
        ONE = 1, "⭐"
        TWO = 2, '⭐⭐'
        THREE = 3, '⭐⭐⭐'
        FOUR = 4, '⭐⭐⭐⭐'
        FIVE = 5, '⭐⭐⭐⭐⭐'

    book = ForeignKey('bookstore.Book', on_delete=CASCADE, related_name='reviews')
    review_text = TextField()
    # user = ForeignKey('auth.User', on_delete=CASCADE)
    user_name = CharField(max_length=100)
    rating = PositiveIntegerField(choices=Ratings, default=Ratings.FIVE)

    def __str__(self):
        return self.review_text[:10]

