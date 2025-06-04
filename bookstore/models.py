from django.db.models import Model, ForeignKey, CASCADE, CharField, DecimalField, ImageField
from django.db.models.fields import TextField, PositiveIntegerField


# Create your models here.
class Book(Model):
    title = CharField(max_length=255)
    price = DecimalField(max_digits=12, decimal_places=2)
    author = ForeignKey('bookstore.Author', on_delete=CASCADE, related_name='books')
    # thumbnail = ImageField('books/thumbnail/')

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
    book = ForeignKey('bookstore.Book', on_delete=CASCADE, related_name='reviews')
    review_text = TextField()
    user = ForeignKey('auth.User', on_delete=CASCADE)
    rating = PositiveIntegerField()