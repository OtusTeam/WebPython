from models import session, Post, User, Tag, tags_posts_table

# Удаляем данные из таблиц
session.query(Post).delete()
session.query(User).delete()
session.query(Tag).delete()
session.commit()

# Добавляем данные
# Пользователи
user = User(username='john')
session.add(user)
session.commit()
# Посты
post = Post(title='My post', user_id=user.id)
session.add(post)
session.commit()

# Явное указание ключей
p = session.query(Post).join(User, Post.user_id == User.id).first()
print(p.user.username)  # john

# Неявное указание ключей
p = session.query(Post).join(User).first()
print(p.user.username)  # john

# Добавляем тэг
tag = Tag(name='python')
session.add(tag)

p = session.query(Tag).join(User, Tag.id == User.id).first()
print(p) # <__main__.Tag object at 0x103471630>

p = session.query(Tag, User).join(User, Tag.id == User.id).first()
print(p)  # (<__main__.Tag object at 0x1036aea58>, <__main__.User object at 0x1036aec50>)

# Добавляем еще 1 тэг и 1 пользователя
session.add(User(username='kate'))
session.add(Tag(name='java'))
session.commit()

# Количество
p = session.query(Tag, User).count()
print(p)  # 4

# Добавим еще пост не john
post = Post(title='New', user_id=2)
# Тэг python
post.tags.append(tag)
session.add(post)
session.commit()

# FILETR по FK
# Посты пользователя john
posts = session.query(Post).join(User).filter(User.username == 'john').all()
print('john posts:', posts)


# Без join
posts = session.query(Post, User).filter(User.username == 'john').all()
print(posts)

# Filter m2m
tag_id = session.query(Tag.id).filter(Tag.name=='python').scalar()
posts = session.query(Post).join(tags_posts_table).filter(
    tags_posts_table.c.tag_id == tag_id,
)

print(posts.first().tags[0].name)