from django.db import models

"""
" Author: Benjamin Knox
" Purpose: Models for the PDT document management portal
"""

"""
" The document table contains the information
"    for each document.
"""
class Document(models.Model):
	id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=255)
	descripion = models.TextField()
	approved = models.BooleanField()
	date = models.DateField()

"""
" The documentlocation table contains the location
"    for the files that make up a document.
"    -There is one `document` for multiple `documentlocation`
"	rows
"""
class Documentlocation(models.Model):
	id = models.AutoField(primary_key=True)
	location = models.CharField(max_length=255)
	documentid = models.ForeignKey(Document)
	date = models.DateField()

"""
" The Comment table contains the comment information
"    for a file or document.
"    -There is one `documentlocation` for multiple `comment` rows.
"""
class Comment(models.Model):
	id = models.AutoField(primary_key=True)
	documentid = models.ForeignKey(Document)
	documentlocationid = models.ForeignKey(Documentlocation, blank=True)
	userid = models.IntegerField()
	content = models.TextField()
	date = models.DateField()
