from django.contrib.auth.models import User
from django.db import models
from django.db.models import Sum

article = 'ARTICLE'
news = 'NEWS'

POST_TYPE = [
    (article, 'Статья'),
    (news, 'Новость')
]


class Author(models.Model):
    user_link = models.OneToOneField(User, on_delete=models.CASCADE)
    rating = models.IntegerField(default=0)

    def update_rating(self):
        # суммарный рейтинг всех статей автора
        postRat = self.post_set.aggregate(postRating=Sum('rating'))
        pRat = 0
        pRat += postRat.get('postRating')
        # суммарный рейтинг всех комментариев автора
        commentRat = self.user_link.comment_set.aggregate(commentRating=Sum('rating'))
        cRat = 0
        cRat += commentRat.get('commentRating')
        self.rating = pRat * 3 + cRat
        self.save()


class Category(models.Model):
    name = models.CharField(max_length=255, unique=True)


class Post(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    categories = models.ManyToManyField(Category, through='PostCategory')
    post_type = models.CharField(max_length=7, choices=POST_TYPE, default=article)
    create_time = models.DateTimeField(auto_now_add=True)
    title = models.TextField(default='Заголовок статьи')
    text = models.TextField(default='Текст статьи')
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()

    def preview(self):
        s = str(self.text)
        if len(s) > 125:
            result = s[:125] + '...'
        else:
            result = s
        return result


class PostCategory(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)


class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    create_time = models.DateTimeField(auto_now_add=True)
    text = models.TextField(default='Комментарий')
    rating = models.IntegerField(default=0)

    def like(self):
        self.rating += 1
        self.save()

    def dislike(self):
        self.rating -= 1
        self.save()