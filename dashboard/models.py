from django.conf import settings
from django.db import models

class Analysis(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name="analyses")
    heures_revision = models.FloatField()
    exercices = models.FloatField()
    absence = models.FloatField()
    note_precedente = models.FloatField()
    resultat = models.CharField(max_length=100)
    conseil = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ["-created_at"]
