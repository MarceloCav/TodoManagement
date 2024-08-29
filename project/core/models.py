from django.db import models

class BaseModel(models.Model):
    created_at  = models.DateTimeField(verbose_name='Registrado em', auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(verbose_name='Atualizado em', auto_now=True)

    class Meta:
        abstract = True


class TestModel(BaseModel):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name