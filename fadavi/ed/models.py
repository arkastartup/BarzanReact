from django.db import models
import datetime

class judge(models.Model):
    judge_id = models.IntegerField(max_length = 20,primary_key=True)
    full_name = models.CharField(max_length = 150)
    user_name = models.CharField(max_length = 50)
    degree = models.CharField(max_length = 100)
    email = models.CharField(max_length = 150)
    face_book = models.CharField(max_length = 150)
    twitter = models.CharField(max_length = 150)
    link_edin = models.CharField(max_length = 150)
    description = models.CharField(max_length = 500)
    create_date = models.DateField(default = datetime.date.today())

#

class users(models.Model):
    user_id = models.IntegerField(max_length = 20, primary_key=True)
    role = models.IntegerField(max_length = 15)
    user_name = models.IntegerField(max_length = 50)
    name = models.IntegerField(max_length = 50)
    family = models.IntegerField(max_length = 80)
    country_id = models.IntegerField(max_length = 1)
    city_id = models.IntegerField(max_length = 1)
    teacher_id = models.IntegerField(max_length = 1)
    address = models.CharField(max_length = 500)
    status = models.IntegerField(max_length = 1)   #online=1 // offline=0
    phone = models.IntegerField(max_length = 20)
    Telegram = models.CharField(max_length = 50)
    grade_id = models.IntegerField(max_length = 20)
    study_branch = models.CharField(max_length = 60)
    create_date = models.DateField(default = datetime.date.today())

class country(models.Model):
    id = models.IntegerField(max_length = 10, primary_key=True)
    name = models.CharField(max_length = 70)
    country_id = models.IntegerField(max_length = 10)
    username_adder = models.CharField(max_length = 50)
    create_date = models.DateField(default = datetime.date.today())


class city(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    name = models.CharField(max_length = 70)
    province_id = models.IntegerField(max_length = 20)
    username_adder = models.CharField(max_length = 50)
    create_date = models.DateField(default = datetime.date.today())

class sponser(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    picture_name = models.CharField(max_length = 100)
    username_adder = models.CharField(max_length = 50)
    description = models.CharField(max_length = 70)
    create_date = models.DateField(default = datetime.date.today())


class site_views(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    views = models.IntegerField(max_length = 20)
    create_date = models.DateField(default = datetime.date.today())

class contact_us(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    first_name = models.CharField(max_length = 70)
    last_name = models.CharField(max_length = 120)
    email = models.CharField(max_length = 70)
    phone = models.IntegerField(max_length = 20)
    description = models.CharField(max_length = 500)
    subject = models.CharField(max_length = 150)
    message_state = models.IntegerField(max_length = 1)


class paper_ticket(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    name = models.CharField(max_length = 150)
    subject = models.CharField(max_length = 100)
    phone = models.IntegerField(max_length = 20)
    description = models.CharField(max_length = 500)
    create_date = models.DateField(default = datetime.date.today())
    username_adder = models.CharField(max_length = 50)
    response_username = models.CharField(max_length = 50)
    response_message = models.CharField(max_length = 500)
    message_read = models.IntegerField(max_length = 1)
    response_date = models.DateField(default = datetime.date.today())         ## doubt on this one
    response_status = models.IntegerField(max_length = 1)


class conferance_aspects(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    name = models.CharField(max_length = 70)
    username_adder = models.CharField(max_length = 50)
    create_date = models.DateField(default = datetime.date.today())


class news(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    title = models.CharField(max_length = 80)
    picture_name = models.CharField(max_length = 150)
    blog_group = models.IntegerField(max_length = 20)
    short_description = models.CharField(max_length = 250)
    description = models.CharField(max_length = 500)
    username_adder = models.CharField(max_length = 50)
    create_date = models.DateField(default = datetime.date.today())


class blog_group(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    name = models.CharField(max_length = 50)
    status = models.IntegerField(max_length = 1)
    username_adder = models.CharField(max_length = 50)
    create_date = models.DateField(default = datetime.date.today())


class scheduel(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    title = models.CharField(max_length = 150)
    short_description = models.CharField(max_length = 250)
    description = models.CharField(max_length = 500)
    start_time = models.CharField(max_length = 20)
    end_time = models.CharField(max_length = 20)
    date = models.DateField(default = datetime.date.today())
    speaker_id = models.IntegerField(max_length = 20)
    tag = models.CharField(max_length = 500)
    username_adder = models.CharField(max_length = 50)
    create_date = models.DateField(default = datetime.date.today())


class about_us(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    title = models.CharField(max_length = 500)
    short_description = models.CharField(max_length = 250)
    description = models.CharField(max_length = 500)
    picture_name = models.CharField(max_length = 100)
    username_adder = models.CharField(max_length = 50)
    create_date = models.DateField(default = datetime.date.today())


class faq(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    question = models.CharField(max_length = 500)
    answer = models.CharField(max_length = 500)
    username_adder = models.CharField(max_length = 50)
    create_date = models.DateField(default = datetime.date.today())

class user_comment(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    user_name = models.CharField(max_length = 50)
    full_name = models.CharField(max_length = 500)
    phone = models.IntegerField(max_length = 20)
    email = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    avatar = models.CharField(max_length = 500)
    blong_id = models.IntegerField(max_length = 20)


class response_comment(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    user_name = models.CharField(max_length = 50)
    full_name = models.CharField(max_length = 500)
    phone = models.IntegerField(max_length = 20)
    email = models.CharField(max_length = 100)
    description = models.CharField(max_length = 500)
    avatar = models.CharField(max_length = 500)
    comment_id = models.IntegerField(max_length = 20)


class paper_info(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    title = models.CharField(max_length = 500)
    categories_id = models.IntegerField(max_length = 20)
    username_adder = models.CharField(max_length = 50)
    file_name = models.CharField(max_length = 500)
    date_insert = models.DateField(default = datetime.date.today())
    paper_status_id = models.IntegerField(max_length = 1)
    description = models.CharField(max_length = 500)

class paper_status_now(models.Model):
    id = models.IntegerField(max_length = 20, primary_key=True)
    name = models.CharField(max_length = 500)
    username_adder = models.CharField(max_length = 50)
    date_inset = models.DateField(default = datetime.date.today())


class paper_delivery(models.Model):
    id = models.IntegerField(max_length = 20 , primary_key=True)
    paper_id = models.IntegerField(max_length = 20)
    judge_username = models.IntegerField(max_length = 20)
    sent_time = models.DateField(default = datetime.date.today())
    sent_status = models.IntegerField(max_length = 1)
    sent_description = models.CharField(max_length = 500)
    username_adder = models.CharField(max_length = 50)
    date_insert = models.DateField(default = datetime.date.today())
    
class user_log_report(models.Model):
    id = models.IntegerField(max_length = 20 ,primary_key=True)
    user_name = models.CharField(max_length = 50)
    description = models.CharField(max_length = 500) 
    date_insert =  models.DateField(default = datetime.date.today())
