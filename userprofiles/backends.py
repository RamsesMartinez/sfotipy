from django.contrib.auth.models import User
from django.db.models import Q


class EmailBackend(object):
    @staticmethod
    def authenticate(email_or_username=None, password=None):
        try:
            user = User.objects.get(Q(username=email_or_username) | Q(email=email_or_username))
            if user.check_password(password):
                return user
        except User.DoesNotExist:
            return None

    @staticmethod
    def get_user(user_id):
        try:
            return User.objects.get(id=user_id)
        except User.DoesNotExist:
            return None
