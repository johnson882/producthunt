from django.db import models
from django.contrib.auth.models import User

class Vote(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    #product = models.ForeignKey(Product, on_delete=models.CASCADE)




class Product(models.Model):
    title = models.CharField(max_length=255)
    pub_date = models.DateTimeField()
    body = models.TextField()
    url = models.TextField()
    image = models.ImageField(upload_to='images/')
    icon = models.ImageField(upload_to='images/')
    votes_total_int = models.IntegerField(default=0)
    hunter = models.ForeignKey(User, on_delete=models.CASCADE)
    votes_total = models.ManyToManyField(Vote, related_name="votes", blank=True)

    def __str__(self):
        return self.title

    def summary(self):
        return self.body[:100]

    def pub_date_pretty(self):
        return self.pub_date.strftime('%b %e %Y')
