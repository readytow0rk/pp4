from django.db import models

class TestModel(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()

# Create and save a test object
test_obj = TestModel(name='John Doe', email='johndoe@example.com')
test_obj.save()