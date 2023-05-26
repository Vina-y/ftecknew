from django.db import models

class bookDemo(models.Model):
    id = models.BigAutoField(primary_key=True)
    name = models.CharField(max_length=64,blank=True, null=True)
    phone = models.CharField(max_length=10,blank=True, null=True)
    email = models.EmailField(unique=True, error_messages={'unique':"Email address already exists."}, max_length=100)
    subject=models.TextField()
    message=models.TextField()
    created_date = models.DateTimeField(auto_now_add=True)
    class Meta:
        managed = True
        db_table = 'book_demo'