import os
import django

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'tienda_project.settings')
django.setup()

from django.contrib.auth import get_user_model

User = get_user_model()
username = 'admin'
email = 'arlette.suarez@uncp.edu.pe'
password = 'admin'

if not User.objects.filter(username=username).exists():
    User.objects.create_superuser(username=username, email=email, password=password)
    print(f"Superusuario '{username}' creado exitosamente con contraseña '{password}'.")
else:
    print(f"Superusuario '{username}' ya existe.")
