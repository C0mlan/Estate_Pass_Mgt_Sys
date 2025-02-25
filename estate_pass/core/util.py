import random
def generate():
    while True:
        code=str(random.randint(100000,99999))
        if not Guest.objects.filter(code=code).exists():
            return code