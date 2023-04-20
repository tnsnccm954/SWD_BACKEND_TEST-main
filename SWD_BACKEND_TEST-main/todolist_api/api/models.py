from django.db import models

# Create your models here.
class Task(models.Model):
    title = models.CharField(max_length=50)
    descript = models.TextField()
    piority = models.IntegerField(default=3)
    is_complete = models.BooleanField(default=False)
    date_created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering=['piority']
        db_table='task'
    def __str__(self):
        return 'id:'+str(self.id) +', task:'+self.title +', piority:'+str(self.piority)