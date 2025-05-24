from django.utils.timezone import now
import datetime

def is_user_online(user):
    if user.last_seen:
        return now() - user.last_seen < datetime.timedelta(minutes=5)  # онлайн, якщо активний останні 5 хвилин
    return False
