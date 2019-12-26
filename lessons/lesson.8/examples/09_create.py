from models import session, Post

posts = [
    {'id': 1, 'title': 'foo post'},
    {'id': 2, 'title': 'bar post'},
]
# for post_info in posts:
#     session.add(Post(**post_info))
#     session.commit()  # 2 запроса
for post_info in posts:
    session.add(Post(**post_info))
session.commit()  # 1 запрос

#session.execute(Post.__table__.insert(), posts)  # 1 запрос