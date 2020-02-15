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

class Industry (models.Model):
    # id_industry = models.PositiveIntegerField(primary_key = True)
    name = models.CharField(max_length = 45)
    umbrella = models.CharField(max_length = 45)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

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
    notes = models.TextField() #CharField(max_length = 255)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

class Company(models.Model):
    # id_company = models.PositiveIntegerField(primary_key = True)
    company_name = models.CharField(max_length = 45)
    company_status = models.ForeignKey(CompanyStatus, related_name="company_status", on_delete=models.PROTECT) #CompanyStatus.id_company_status(primary_key = True)
    industries = models.ManyToManyField(Industry, related_name="companies_industries")
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

class User (models.Model):
    # id_user = models.PositiveIntegerField(primary_key = True)
    first_name = models.CharField(max_length = 45)
    last_name = models.CharField(max_length = 45)
    year = models.CharField(max_length = 45)
    email = models.CharField(max_length = 45)
    phone_number = models.PositiveIntegerField(default = 0)
    in_rcsa = models.BooleanField(default=False) #SmallIntegerField()
    # committee = models.CharField(max_length = 45)
    committees = models.ManyToManyField(Committee, related_name="users_committees")
    authentication_level = models.PositiveIntegerField(default = 0)
    companies = models.ManyToManyField(Company, related_name="users_companies")
    majors = models.ManyToManyField(Major, related_name="users_majors")
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class Authenticated(models.Model):
    authenticator = models.ForeignKey(User, related_name="authenticator_authenticated", on_delete=models.PROTECT)
    authenticated = models.BooleanField()
    create_time = models.DateTimeField(auto_now_add=True)
    update_time = models.DateTimeField(auto_now=True)

class Tag (models.Model):
    # id_tag = models.PositiveIntegerField(default = 0)
    tag = models.CharField(max_length = 45)
    category = models.CharField(max_length = 45)
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)

class Article (models.Model):
    # id_article = models.PositiveIntegerField(default = 0)
    author = models.ForeignKey(User, related_name = "article_user", on_delete=models.PROTECT)
    title = models.CharField(max_length = 45, primary_key = True)
    content = models.TextField() #CharField(max_length = 225)
    archive = models.SmallIntegerField() #justin: what is this for?
    authetication = models.ForeignKey(Authenticated, related_name="article_authentication", on_delete=models.PROTECT, default=None)
    industries = models.ManyToManyField(Industry, related_name="articles_industries")
    tags = models.ManyToManyField(Tag, related_name="articles_tags")
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

class Event (models.Model):
    # id_event = models.PositiveIntegerField(default = 0)
    tb_event = models.CharField(max_length = 45) #what does this rep?
    rsvp = models.CharField(max_length = 45)
    companies = models.ManyToManyField(Company, related_name="events_companies")
    industries = models.ManyToManyField(Industry, related_name="events_industries")
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
    # repeats = models.SmallIntegerField()
    repeats = models.ManyToManyField(Repeat, related_name="datetime_repeats")
    events = models.ManyToManyField(Event, related_name="datetimes_events")
    create_time = models.DateTimeField(auto_now_add = True)
    update_time = models.DateTimeField(auto_now = True)