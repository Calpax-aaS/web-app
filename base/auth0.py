from social_core.backends.auth0 import Auth0OAuth2


class Auth0(Auth0OAuth2):
    EXTRA_DATA = [
        ('picture', 'picture'),
        ('email', 'email'),
    ]