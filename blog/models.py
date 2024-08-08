from django.db import models
from django.core.validators import MinLengthValidator

# Create your models here.

class Author(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email_address = models.EmailField() #essentially a CharField with an EmailValidator

    def __str__(self):
        return f"{self.first_name} {self.last_name}"

class Tags(models.Model):
    caption = models.CharField(max_length=20)

    def __str__(self):
        return self.caption
    class Meta:
        verbose_name_plural ="Tags"

class Post(models.Model):
    title = models.CharField(max_length=100)
    excerpt = models.CharField(max_length=200)
    image = models.ImageField(upload_to="posts",null=True)
    date = models.DateField(auto_now=True)
    slug = models.SlugField(unique=True)#unique makes sure our slug is unqiue for every post(like db_index)
    content = models.TextField(validators=[MinLengthValidator(10)])
    author = models.ForeignKey(Author,null=True,on_delete = models.SET_NULL,related_name="posts")
    tags=models.ManyToManyField(Tags)


    def __str__(self):
        return self.title


class Comment(models.Model):
    user_name = models.CharField(max_length=120)
    user_email = models.EmailField() 
    text = models.TextField(max_length=400)
    post = models.ForeignKey(
        Post, on_delete=models.CASCADE, related_name="comments")