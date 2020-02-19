# PD Website TODO Tasks
## 02/09/20
### Pranati
- Basically what I mean is setting up the following:
  1) HTML formatting for a form in a template (I'll set up the files, comment in useful links, etc...)
    - https://djangobook.com/mdj2-django-templates/
  2) In views.py write in the logic for processing the articles basically so we have it in our databases (https://docs.djangoproject.com/en/3.0/topics/http/views/) (we'll probably change this later but just for usage now). If you don't know how to write it out actually (like what model names to use from models.py) just write in pseudocode (which is just like:
    - article = request.get("article_body")
    - Articles.objects.create("temp", article, ...) #this isn't an actual model name but just temporary and so on and so forth
  3) link up which URL should display the template (Google will be your best friend and I'll link the basic ones) and which URL should go to which view.
### Justin
- Set up models.py file (see PD Website.mwb)
- Refer to links below:
  - https://docs.djangoproject.com/en/3.0/ref/models/fields/
  - https://docs.djangoproject.com/en/3.0/ref/models/fields/
  - https://ultimatedjango.com/learn-django/lessons/create-the-model/ (steps 1 and 2; for 2: see below)
- Making Migrations:
  - python manage.py
  - makemigrations [name_of_model_class_created]
  - ONE CLASS AT A TIME
  
### Caroline
- Go through all the files and sort into what is needed (categorising)
- Set up framework w/ migrations and Django hijinks
- Create README.md file for reference tasks
- Comment through basic code w/ file names/documentation

## Remember: ask me if you need help ASAP!!!
