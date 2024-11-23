from django.urls import path

websocet_urlpatterns = {
    path('ws' , ChatConsumer.as_asgi()),
}