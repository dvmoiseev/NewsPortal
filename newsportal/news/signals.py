from django.db.models.signals import m2m_changed
from django.dispatch import receiver
from news.models import PostCategory
from django.core.mail import send_mail
from newsportal.settings import EMAIL_HOST_USER

@receiver(m2m_changed, sender = PostCategory)
def send_email_newpost(sender, instance, **kwargs):
    if kwargs['action'] == 'post_add':
        categories = instance.categories.all()
        emails = [] #список адресов всех подписчиков, которым собираемся отправить письма
        for category in categories:
            for subscriber in category.subscribers.all():
                if subscriber.email != '':
                    emails.append(subscriber.email)
        link = 'http://127.0.0.1:8000/news/'+str(instance.pk)
        message = 'Ознакомьтесь с новой статьёй по ссылке ' + link
        send_mail(
            'Новое сообщение на портале новостей!',
            message,
            EMAIL_HOST_USER,
            emails,
            fail_silently=True,
        )