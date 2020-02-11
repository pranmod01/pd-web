from django.db import models

# Create your models here.
<<<<<<< HEAD
class Article (models.Model):
    id_article=models.PositiveIntegerField()
    User_id_user=models.ManyToManyField(User.id_user, verbose_name="name of users")
    title=models.CharField(max_length=45, primary_key=True)
    content=models.CharField(max_length=225)
    archive=models.SmallIntegerField()
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)

class User (models.Model):
    id_user=models.PositiveIntegerField(primary_key=True)
    first_name=models.CharField(max_length=45)
    last_name=models.CharField(max_length=45)
    year=models.CharField(max_length=45)
    email=models.CharField(max_length=45)
    phone_number=PostiiveIntegerField()
    in_rcsa=SmallIntegerField()
    committee=models.CharField(max_length=45)
    authentication_level=PositiveIntegerField()

class DateTime(models.Model):
    id_date_time=models.PositiveIntegerField(primary_key=True)
    day= models.PositiveIntegerField()
    month=models.PositiveIntegerField()
    month_word=models.CharField(max_length=45)
    year=models.PositiveIntegerField()
    hour=models.PositiveIntegerField()
    minute=models.PositiveIntegerField()
    second=models.PositiveIntegerField()
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    repeats=models.SmallIntegerField()

class House (models.Model):
    id_house=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    User_id_user=models.ForeignKey(User.id_user, related_name="members")

class Event (models.Model):
    id_event=models.PositiveIntegerField()
    tb_event=models.CharField(max_length=45)
    rsvp=models.CharField(max_length=45)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)

#class Event_has_Company (models.Model):
#class User_has_Company (models.Model):
#class Article_has_Industry (models.Model):
#class Event_has_Industry (models.Model):
#class User_has_Major (models.Model):
#class Company_has_Industry (models.Model):
#class DateTime_has_Event (models.Model):
#class Article_has_Tag (models.Model):

class Repeat(models.Model):
    id_repeat=models.PositiveIntegerField()
    monday=models.PositiveIntegerField()
    tuesday=models.PositiveIntegerField()
    wednesday=models.PositiveIntegerField()
    thursday=models.PositiveIntegerField()
    friday=models.PositiveIntegerField()
    saturday=models.PositiveIntegerField()
    sunday=models.PositiveIntegerField()
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)

class Committee (models.Model):
    id_committee=models.PositiveIntegerField()
    year_start=models.PositiveIntegerField()
    year_end=models.PositiveIntegerField()
    name=models.CharField(max_length=45)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    User_id_user=models.ForeignKey(User.id_user, related_name="members")

class Tag (models.Model):
    id_tag=models.PositiveIntegerField()
    tag=models.CharField(max_length=45)
    category=models.CharField(max_length=45)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)

class Industry (models.Model):
    id_industry=models.PositiveIntegerField(primary_key=True)
    name=models.CharField(max_length=45)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    umbrella=models.CharField(max_length=45)

class Major (models.Model):
    id_major=models.PositiveIntegerField(primary_key=True)
    college=models.CharField(max_length=45)
    name=models.CharField(max_length=45)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)

class Company(models.Model):
    id_company=models.PositiveIntegerField(primary_key=True)
    company_name=models.CharField(max_length=45)
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    company_status=CompanyStatus.id_company_status(primary_key=True)

class CompanyStatus(models.Model):
    id_company_status=models.PositiveIntegerField(primary_key=True)
    connected=models.SmallIntegerField()
    pending=models.SmallIntegerField()
    contacted=models.SmallIntegerField()
    future=models.SmallIntegerField()
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    notes=models.CharField(max_length=255)

class DateTime(models.Model):
    id_date_time=models.PostiiveIntegerField(primary_key)
    day=models.PositiveIntegerField()
    month=models.PositiveIntegerField()
    month_word=models.CharField(max_length=45)
    year=models.PositiveIntegerField()
    hour=models.PositiveIntegerField()
    minute=models.PositiveIntegerField()
    second=models.PositiveIntegerField()
    create_time=models.DateTimeField(auto_now_add=True)
    update_time=models.DateTimeField(auto_now=True)
    repeats=models.SmallIntegerField()
=======

#Justin
#class Class_Name_Singular(models.Model):
#	normal_field_item = models.FieldTyle(args)
#	foreign_key_item_name_singular = models.ForeignKey(foreign_key_item_class_name, related_name = "classname_foreignkeyname")
#	many_many_relations_name_plural = models.ManyToManyField(Other_Class_Name, related_name = "classnameplural_otherclassplural")
>>>>>>> 75b338aaf2f8cba1b01f8946c62fcda78b609d78
