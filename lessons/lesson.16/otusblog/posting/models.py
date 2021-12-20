from django.contrib.auth import get_user_model
from django.db import models
from django.utils.functional import cached_property


class Author(models.Model):
    STATUS_JR = 'J'
    STATUS_MD = 'M'
    STATUS_SR = 'S'

    STATUS_CHOICES = [
        (STATUS_JR, 'junior'),
        (STATUS_MD, 'middle'),
        (STATUS_SR, 'senior'),
    ]

    user = models.OneToOneField(get_user_model(),
                                on_delete=models.CASCADE,
                                primary_key=True)

    status = models.CharField(max_length=1,
                              choices=STATUS_CHOICES,
                              default=STATUS_JR)
    bio = models.TextField(blank=True)

    def __str__(self):
        return f"Author <{self.user}>"

    @cached_property
    def some_method(self):
        print('call some_method')
        return 'some_method'

    class Meta:
        ordering = ['pk']


class ArticleTag(models.Model):
    name = models.CharField(max_length=32)

    def __str__(self):
        return self.name

    class Meta:
        ordering = ['pk']


class Article(models.Model):
    DRAFT = 'd'
    ON_REVIEW = 'o'
    APPROVED = 'a'
    PUBLISHED = 'p'
    STATUSES = (
        (DRAFT, 'Draft'),
        (ON_REVIEW, 'On review'),
        (APPROVED, 'Approved'),
        (PUBLISHED, 'Published'),
    )

    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    title = models.CharField(max_length=150)
    text = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    published_at = models.DateTimeField(null=True, blank=True)
    edited_at = models.DateTimeField(auto_now=True)
    status = models.CharField(max_length=1, choices=STATUSES, default=DRAFT)
    read_qty = models.PositiveIntegerField(default=0)

    tag = models.ManyToManyField(ArticleTag, related_name='articles')

    def __str__(self):
        # return f"Article(title={self.title}, author={self.author})"
        return f"Article(title={self.title})"

    class Meta:
        ordering = ['pk']
