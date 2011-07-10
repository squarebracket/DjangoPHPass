import MySQLdb
import auth_funcs
from models import users
from django.contrib.auth.models import User, Group

class WordpressBackend:
    """
    Authenticates against a Wordpress v3.1.4 user database using PHPass

    Requires MySQLdb to be installed
    """

    supports_object_permissions = False
    supports_anonymous_user = False
    supports_inactive_user = False

    def authenticate(self, username=None, password=None):
        wp = users.objects.all()
        try:
	    wp = users.objects.get(user_login=username)
            pwd_db = wp.user_pass
            login_valid = True
	except:
	    return None
        pwd_valid = (pwd_db == auth_funcs.hash(password, pwd_db))
	if login_valid and pwd_valid:
            try:
                user = User.objects.get(username=username)
            except User.DoesNotExist:
                # Create a new user. Note that we can set password
                # to anything, because it won't be checked; the password
                # from settings.py will.
                user = User(username=username, password='get from wordpress')
                user.is_staff = True
                #user.is_superuser = True
                user.save()
		user.groups.add(Group.objects.get(name='inputters'))
            return user
        return None

    def get_user(self, user_id):
        try:
            return User.objects.get(pk=user_id)
        except User.DoesNotExist:
            return None

