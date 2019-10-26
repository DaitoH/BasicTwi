from django.db import models
from django.contrib.auth.models import User


# Messageクラス
class Message(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='message_owner')
    content = models.TextField(max_length=10000)
    share_id = models.IntegerField(default=-1)
    pub_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.content) + ' (' + str(self.owner) + ')'

    class Meta:
        ordering = ('-pub_date',)





# Friendクラス
class Friend(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, related_name='friend_owner')
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return str(self.user) + ' (group:"' + str(self.group) + '") '
