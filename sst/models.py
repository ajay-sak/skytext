from django.db import models
from django.contrib.auth.models import User
from datetime import datetime

class TestPaper(models.Model):
    paper_name = models.CharField(max_length=50, verbose_name="Exam")
    q_paper = models.FileField(upload_to='q_papers/%y/%m/%d')
    created_on = models.DateTimeField(default=datetime.now())
    published_status = models.BooleanField(default=True)

    class Meta:
        ordering = ['-id']

    def __str__(self):
        return str(self.paper_name)

    def delete(self, *args, **kwargs):
        self.q_paper.delete()
        super().delete(*args, **kwargs)

class TestDetails(models.Model):
    name = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Username")
    user_id = models.CharField(max_length=50, default="sst21", verbose_name="ID")
    class_name = models.CharField(max_length=50, verbose_name="Class", default="seventh")
    test_name = models.CharField(max_length=50, verbose_name="Name of the Test")
    test_paper = models.ForeignKey(TestPaper, null=True, blank=True, verbose_name="Test Paper", on_delete=models.CASCADE)
    marks = models.IntegerField()
    total_marks = models.IntegerField(default=100)
    created_on = models.DateTimeField(default=datetime.now())
    published_status = models.BooleanField(default=True)

    class Meta:
        verbose_name_plural = 'Test Details'


    def __str__(self):
        return str(self.name) +  " | " + self.test_name
