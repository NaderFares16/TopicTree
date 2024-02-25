from django.db import models
from django.contrib.auth.models import User

class Topic(models.Model):
  # ASSUNTO NA QUAL USUÁRIO ESTÁ APRENDENDO
  text = models.CharField(max_length=200)
  date_added = models.DateTimeField(auto_now_add=True)
  owner = models.ForeignKey(User, on_delete=models.CASCADE)

  def __str__(self):
    # RETORNA STRING DO MODELO
    return self.text
  
class Entry(models.Model):
  # NOTA DO APRENDIZADO
  topic = models.ForeignKey(Topic, on_delete=models.CASCADE)
  text = models.TextField()
  date_added = models.DateTimeField(auto_now_add=True)

  class Meta:
    verbose_name_plural = 'entries'

  def __str__(self):
    # RETORNA STRING DO MODELO
    return self.text[:50] + '...'