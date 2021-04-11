import json

from django.shortcuts import render

# Create your views here.
from flight_ticket.models import FlightTicket
from base.models import User


def index(request):
    user = request.user
    context = {}
    if user.is_authenticated:
        try:
            auth0user = user.social_auth.get(provider='auth0')
            userdata = {
                'user_id': auth0user.uid,
                'name': user.first_name,
                'picture': auth0user.extra_data['picture'],
                'email': auth0user.extra_data['email'],
            }
        except Exception:
            auth0user = user
            userdata = {
                'user_id': user.id,
                'name': user.first_name,
                'email': user.email,
            }

        context = {'auth0User': auth0user, 'userdata': json.dumps(userdata, indent=4)}


    context = {**context, 'flight_tickets': FlightTicket.objects.all()}

    return render(request, 'flight_ticket/index.html', context)
