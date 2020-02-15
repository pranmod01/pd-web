from django.db import models

# Create your models here.
#Justin
#class Class_Name_Singular(models.Model):
#	normal_field_item  =  models.FieldTyle(args)
#	foreign_key_item_name_singular  =  models.ForeignKey(foreign_key_item_class_name, related_name  =  "classname_foreignkeyname")
#	many_many_relations_name_plural  =  models.ManyToManyField(Other_Class_Name, related_name  =  "classnameplural_otherclassplural")
class Committee (models.Model):
    # id_committee = models.PositiveIntegerField(default = 0)
    year_start = models.PositiveIntegerField(default = 0)
    year_end = models.PositiveIntegerField(default = 0)
    name = models.CharField(max_length = 45)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    # User_id_user = models.ForeignKey(User.id_user, related_name = "members")

class User (models.Model):
    # id_user = models.PositiveIntegerField(primary_key = True)
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    year = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    phone_number = models.PositiveIntegerField(default = 0)
    in_rcsa = models.BooleanField(default=False) #SmallIntegerField()
    # committee = models.CharField(max_length = 45)
    committee = models.ManyToManyField(Committee, related_name="users_committees")
    authentication_level = models.PositiveIntegerField(default = 0)

class Authenticated(models.Model):
    authenticator = models.ForeignKey(User, related_name="authenticator_authenticated", on_delete=models.PROTECT)
    authenticated = models.BooleanField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class Article (models.Model):
    # id_article = models.PositiveIntegerField(default = 0)
    author = models.ForeignKey(User, related_name = "article_user", on_delete=models.PROTECT)
    title = models.CharField(max_length = 45, primary_key = True)
    content = models.TextField() #CharField(max_length = 225)
    archive = models.SmallIntegerField() #justin: what is this for?
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

class Repeat(models.Model):
    # id_repeat = models.PositiveIntegerField(default = 0)
    monday = models.PositiveIntegerField(default = 0)
    tuesday = models.PositiveIntegerField(default = 0)
    wednesday = models.PositiveIntegerField(default = 0)
    thursday = models.PositiveIntegerField(default = 0)
    friday = models.PositiveIntegerField(default = 0)
    saturday = models.PositiveIntegerField(default = 0)
    sunday = models.PositiveIntegerField(default = 0)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

class DateTime(models.Model):
    # id_date_time = models.PositiveIntegerField(primary_key = True)
    day =  models.PositiveIntegerField(default = 0)
    month = models.PositiveIntegerField(default = 0)
    month_word = models.CharField(max_length = 45)
    year = models.PositiveIntegerField(default = 0)
    hour = models.PositiveIntegerField(default = 0)
    minute = models.PositiveIntegerField(default = 0)
    second = models.PositiveIntegerField(default = 0)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    # repeats = models.SmallIntegerField()
    repeats = models.ManyToManyField(Repeat, related_name="datetime_repeats")

# class House (models.Model):
#     id_house = models.PositiveIntegerField(primary_key = True)
#     name = models.CharField(max_length = 45)
#     create_time = models.DateTimeField(auto_now_add = True)
#     update_time = models.DateTimeField(auto_now = True)
#     User_id_user = models.ForeignKey(User.id_user, related_name = "members")

class Event (models.Model):
    # id_event = models.PositiveIntegerField(default = 0)
    tb_event = models.CharField(max_length = 45) #what does this rep?
    rsvp = models.CharField(max_length = 45)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

#class Event_has_Company (models.Model):
#class User_has_Company (models.Model):
#class Article_has_Industry (models.Model):
#class Event_has_Industry (models.Model):
#class User_has_Major (models.Model):
#class Company_has_Industry (models.Model):
#class DateTime_has_Event (models.Model):
#class Article_has_Tag (models.Model):

class Tag (models.Model):
    # id_tag = models.PositiveIntegerField(default = 0)
    tag = models.CharField(max_length = 45)
    category = models.CharField(max_length = 45)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

class Industry (models.Model):
    # id_industry = models.PositiveIntegerField(primary_key = True)
    name = models.CharField(max_length = 45)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    umbrella = models.CharField(max_length = 45)

class Major (models.Model):
    # id_major = models.PositiveIntegerField(primary_key = True)
    college = models.CharField(max_length = 45)
    name = models.CharField(max_length = 45)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

class CompanyStatus(models.Model):
    # id_company_status = models.PositiveIntegerField(primary_key = True)
    connected = models.BooleanField() #SmallIntegerField()
    pending = models.BooleanField() #SmallIntegerField()
    contacted = models.BooleanField() #SmallIntegerField()
    future = models.BooleanField() #SmallIntegerField()
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    notes = models.TextField() #CharField(max_length = 255)

class Company(models.Model):
    # id_company = models.PositiveIntegerField(primary_key = True)
    company_name = models.CharField(max_length = 45)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)
    company_status = models.ForeignKey(CompanyStatus, related_name="company_status", on_delete=models.PROTECT) #CompanyStatus.id_company_status(primary_key = True)

# class DateTime(models.Model):
#     # id_date_time = models.PostiiveIntegerField(primary_key)
#     day = models.PositiveIntegerField(default = 0)
#     month = models.PositiveIntegerField(default = 0)
#     month_word = models.CharField(max_length = 45)
#     year = models.PositiveIntegerField(default = 0)
#     hour = models.PositiveIntegerField(default = 0)
#     minute = models.PositiveIntegerField(default = 0)
#     second = models.PositiveIntegerField(default = 0)
#     create_time = models.DateTimeField(auto_now_add = True)
#     update_time = models.DateTimeField(auto_now = True)
#     repeats = models.SmallIntegerField()