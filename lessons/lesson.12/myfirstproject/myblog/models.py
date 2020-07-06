from django.db import models


class Author(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField(unique=True)

    @property
    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def __str__(self):
        return self.full_name


class Article(models.Model):
    DRAFT = 'draft'
    ON_REVIEW = 'on-review'
    APPROVED = 'approved'
    PUBLISHED = 'published'
    STATUSES = (
        (DRAFT, 'Draft'),
        (ON_REVIEW, 'On review'),
        (APPROVED, 'Approved'),
        (PUBLISHED, 'Published'),
    )

    title = models.CharField(max_length=200)
    text = models.TextField()
    last_changed = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=9, choices=STATUSES, default=PUBLISHED)

    author = models.ForeignKey(Author, on_delete=models.PROTECT)

    def __str__(self):
        return self.title
