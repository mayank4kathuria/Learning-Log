from django.db import models

# Create your models here.

class Topic(models.Model):
    """A topic the user is learning about"""
    text = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        """Return a string representation of the model"""
        return self.text

class Entry(models.Model):
    """An entry on the progress of the topic"""
    topic = models.ForeignKey(Topic)
    text = models.TextField()
    date_added = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name_plural = "entries"
    
    def __str__(self):
        """Returns the contents of entries"""
        if len(self.text) < 50:
            return self.text
        else:
            return self.text[:50] + "..."


