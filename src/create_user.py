import os
import sys
import django

# Add src directory to path
sys.path.insert(0, os.path.dirname(__file__))

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()

user, created = User.objects.get_or_create(
    username="renato.c",
    defaults={
        "email": "renatochagas.m@gmail.com",
        "is_superuser": True,
        "is_staff": True,
    },
)

if created:
    user.set_password("123")
    user.save()
    print("✓ Usuário criado com sucesso!")
    print(f"  - Username: renato.c")
    print(f"  - Email: renatochagas.m@gmail.com")
    print(f"  - Tipo: Superusuário")
else:
    print("✓ Usuário já existe!")
