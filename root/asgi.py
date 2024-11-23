

import os

from django.core.asgi import get_asgi_application
from apps.routing import

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'root.settings')

application = ProtocolTypeRouter(

)
