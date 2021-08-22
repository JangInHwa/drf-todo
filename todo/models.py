from django.db import models

# Create your models here.
class Todo(models.Model):
	title = models.CharField(max_length=100)
	is_done = models.BooleanField(default=False, blank=True)

	def __str__(self) -> str:
		return ('✓' if self.is_done else '⃝') + ' : ' + self.title
