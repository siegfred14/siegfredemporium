import jwt
from rest_framework import authentication


class JWTAuthentication(authentication.BaseAuthentication):

    def authenticate(self, request):
        return super().authenticate(request)
