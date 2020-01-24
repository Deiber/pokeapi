from django.db import models


class PokeApiBaseModel(models.Model):
	
	"""Abstract model for common information"""

	external_id = models.IntegerField(
		help_text="The record's external id in the pokeapi platform",
		unique=True
	)
	external_url = models.URLField(
		help_text="The record's external url"
	)
	created_date = models.DateTimeField(auto_now_add=True)

	class Meta:
		abstract = True
