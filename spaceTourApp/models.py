from django.db import models


class Advantage(models.Model):
    heading = models.CharField("Heading", max_length=100)
    content = models.CharField("Content", max_length=100)
    extra_content = models.CharField("ExtraContent", max_length=100, blank=True)
    description = models.CharField("Description", max_length=240)

    def __str__(self):
        return f"{self.heading}  {self.description}"


class MenuItem(models.Model):
    text = models.CharField("Text", max_length=50)
    url = models.SlugField("Url", max_length=50, blank=True)

    def __str__(self):
        return self.text