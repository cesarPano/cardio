from django.db import models

class Tecnico (models.Model):
        tecnico_nombre = models.CharField(max_length=100)
        def __str__(self):
                return self.tecnico_nombre

class Tipo_Desfibrilador (models.Model):
        tipo_desfibrilador = models.CharField(max_length=10)
        def __str__(self):
                return self.tipo_desfibrilador

class Tipo_Revision (models.Model):
        tipo_revision = models.CharField(max_length=20)
        def __str__(self):
                return self.tipo_revision

class Desfibrilador (models.Model):
	tipo = models.ForeignKey(Tipo_Desfibrilador, on_delete=models.PROTECT)
	localizacion = models.CharField(max_length=100)
	responsable  = models.CharField(max_length=100)
	imagen = models.ImageField(upload_to='images/', default = 'pic.png') 
	def __str__(self):
		return self.localizacion

class Transmision (models.Model):
	desfibrilador = models.ForeignKey(Desfibrilador, on_delete=models.CASCADE)
	trans_date = models.DateTimeField('date transmitted')
	trans_text = models.CharField(max_length=100)
	def __str__(self):
		return self.desfibrilador.localizacion

class Revision (models.Model):
        desfibrilador = models.ForeignKey(Desfibrilador, on_delete=models.CASCADE)
        tecnico = models.ForeignKey(Tecnico, on_delete=models.PROTECT)
        rev_tipo = models.ForeignKey(Tipo_Revision, on_delete=models.PROTECT)
        rev_date = models.DateTimeField('date revision')
        def __str__(self):
                return self.desfibrilador.localizacion
