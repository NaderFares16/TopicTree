from django.db import models

class Topic(models.Model):
  # ASSUNTO NA QUAL USUÁRIO ESTÁ APRENDENDO
  text = models.CharField(max_length=200)
  date_added = models.DateTimeField(auto_now_add=True)

  def __str__(self):
    # RETORN STRING DO MODELO
    return self.text