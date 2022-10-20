# Команды Django Shell
from django.contrib.auth.models import User

User.objects.create_user('user1')

User.objects.create_user('user2')

from news.models import *

Category.objects.create(name = 'Спорт')

Category.objects.create(name = 'Политика')

Category.objects.create(name = 'Образование')

Category.objects.create(name = 'Экономика')

u1 = User.objects.get(username = 'user1')

u2 = User.objects.get(username = 'user2')

a1 = Author.objects.create(user_link_id = u1.id)

a2 = Author.objects.create(user_link_id = u2.id)

Post.objects.create(author = a1, post_type = 'ARTICLE', title = 'В России учредили премию «Иноагент года»', text = 'Минюст объявил об учреждении новой престижной премии «Иностранный агент» года.')

Post.objects.create(author = a2, post_type = 'ARTICLE', title = 'В Сколково вывели породу не испражняющихся голубей', text = 'На площадке инновационного центра «Сколково» прошла презентация новой породы российских голубей, получившей название «московский сизый». Её вывели при участии столичной мэрии и по поручению Сергея Собянина.')

Post.objects.create(author = a2, post_type = 'NEWS', title = 'Чубайсу вручили медаль «75 лет со дня основания ЦРУ»', text = 'В Вашингтоне состоялась торжественная церемония награждения золотыми памятными медалями за заслуги перед ЦРУ. Единственным гражданином России, получившим почётную награду, стал экономист Анатолий Чубайс.')

c2 = Category.objects.get(name = 'Политика')

c3 = Category.objects.get(name = 'Образование')

c4 = Category.objects.get(name = 'Экономика')

p1 = Post.objects.get(id = 1)

p2 = Post.objects.get(id = 2)

p3 = Post.objects.get(id = 3)

PostCategory.objects.create(post = p1, category = c2)

PostCategory.objects.create(post = p2, category = c3)

PostCategory.objects.create(post = p2, category = c4)

PostCategory.objects.create(post = p3, category = c2)

Comment.objects.create(post = p1, user = u1, text = 'Наконец-то быть иноагентом почётно и престижно!')

Comment.objects.create(post = p1, user = u2, text = 'А это не фейк?..')

Comment.objects.create(post = p2, user = u1, text = 'Ура! Чистые памятники, заборы, скамейки!')

Comment.objects.create(post = p3, user = u2, text = 'ЦРУ что-то знает о Чубайсе...')

a1 = Author.objects.get(id = 1)

p1.like()

<...>

p1.dislike()

com1=Comment.objects.get(id = 1)

com1.like()

<...>

from news.models import *

a1 = Author.objects.get(id = 1)

a2 = Author.objects.get(id = 2)

a1.update_rating()

a2.update_rating()
