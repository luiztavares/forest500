from django.db import models

class IntRange(models.Model):
	start = models.IntegerField()
	end = models.IntegerField()

class Status(models.Model):
	id = models.BigIntegerField()
	id_str = models.TextField()
	conversation_id = models.BigIntegerField()
	conversation_id_str = models.TextField()
	created_at = models.DateTimeField()
	display_text_range = models.ForeignKey(IntRange)

class Hashtag(models.Model):
	indices = models.ForeignKey(IntRange)
	text = models.TextField()
	status = models.ForeignKey(Status)

class Photo(models.Model):
	id = models.BigIntegerField()
	id_str = models.TextField()
	indices = models.ForeignKey(IntRange)
	media_url = models.URLField()
	media_url_https = models.URLField()
	url = models.URLField()
	display_url = models.URLField()
	expanded_url = models.URLField()
	#sizes

class Sizes(models.Model):
	

class Company(models.Model):
	#brands
	#commodities_other
	#commodities_powerbroker
