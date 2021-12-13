from posting.models import Article

articles = Article.objects.all()
print(articles)
