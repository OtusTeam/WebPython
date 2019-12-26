from models import session, Post

q = session.query(Post.id).filter(Post.id == 1)
print(type(q))  # <class 'sqlalchemy.orm.query.Query'>
print(list(q))  # [(1,)]
print(q.all())  # аналог list()
print(q.one())  # берёт все результаты, выбрасывает ошибку, если их не 1
print(q.first())  # делает запрос с limit 1 и возвращает этот объект или None
print(q.scalar())  # аналог one()[0]
