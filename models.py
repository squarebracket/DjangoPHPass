from django.db import models

# Create your models here.
class users(models.Model):
	user_login   = models.CharField(max_length=60)
	user_pass    = models.CharField(max_length=64)
	display_name = models.CharField(max_length=250)
	irc_nicks    = models.CharField(max_length=250)
	



# +---------------------+---------------------+------+-----+---------------------+----------------+
# | Field               | Type                | Null | Key | Default             | Extra          |
# +---------------------+---------------------+------+-----+---------------------+----------------+
# | ID                  | bigint(20) unsigned | NO   | PRI | NULL                | auto_increment |
# | user_login          | varchar(60)         | NO   | MUL |                     |                |
# | user_pass           | varchar(64)         | NO   |     |                     |                |
# | user_nicename       | varchar(50)         | NO   | MUL |                     |                |
# | user_email          | varchar(100)        | NO   |     |                     |                |
# | user_url            | varchar(100)        | NO   |     |                     |                |
# | user_registered     | datetime            | NO   |     | 0000-00-00 00:00:00 |                |
# | user_activation_key | varchar(60)         | NO   |     |                     |                |
# | user_status         | int(11)             | NO   |     | 0                   |                |
# | display_name        | varchar(250)        | NO   |     |                     |                |
# | irc_nicks           | varchar(250)        | YES  |     | NULL                |                |
# | bio                 | longtext            | YES  |     | NULL                |                |
# +---------------------+---------------------+------+-----+---------------------+----------------+
