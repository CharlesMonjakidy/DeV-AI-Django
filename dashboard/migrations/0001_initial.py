from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion

class Migration(migrations.Migration):
    initial=True
    dependencies=[migrations.swappable_dependency(settings.AUTH_USER_MODEL)]
    operations=[migrations.CreateModel(
        name="Analysis",
        fields=[
            ("id", models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name="ID")),
            ("heures_revision", models.FloatField()),
            ("exercices", models.FloatField()),
            ("absence", models.FloatField()),
            ("note_precedente", models.FloatField()),
            ("resultat", models.CharField(max_length=100)),
            ("conseil", models.TextField()),
            ("created_at", models.DateTimeField(auto_now_add=True)),
            ("user", models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name="analyses", to=settings.AUTH_USER_MODEL)),
        ],
        options={"ordering":["-created_at"]},
    )]
