import random
from django.core.cache import cache


def send_otp_to_phone(phone,user_obj):
    if cache.get(phone):
        return False
    try:
        otp_to_sent = random.randint(1000,9999)
        cache.set(phone, otp_to_sent, timeout=60)
        user_obj.otp = otp_to_sent
        user_obj.save()
        return True
    except Exception as e:
        print(e)