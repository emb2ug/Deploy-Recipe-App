from django.db import models

# Create your models here.

class user(models.Model):
	# automatically has autoincrementing id field
	username = models.CharField(max_length=30, unique=True)
	favorites = models.ManyToManyField(Recipe)


class recipe(models.Model):
	# automatically has autoincrementing id field	title = models.CharField(max_length=30)
	description = models.CharField(max_length=250)
	tags = models.ManyToManyField(tag)
	chef = models.ForeignKey(user, on_delete=models.CASCADE)
	post_date = models.DateField(auto_now_add=True)
	# recipe.comment_set.all to get all comments on a given recipe

class comment(models.Model):
	# automatically has autoincrementing id field	poster = models.ForeignKey(user, on_delete=models.CASCADE)
	title = models.CharField(max_length=60)
	content = models.CharField(max_length=300)
	post_date_time = models.DateTimeField(auto_now_add=True)
	recipe = models.ForeignKey(recipe)



class tag(models.Model):
	# automatically has autoincrementing id field
	title = models.CharField(max_length=20)
	recipes = models.ManyToManyField(recipe)


