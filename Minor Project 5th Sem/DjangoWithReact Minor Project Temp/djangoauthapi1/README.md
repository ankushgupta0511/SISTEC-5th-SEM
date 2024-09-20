# install packages inside 'djangoauthapi1'
``` 
pip install djangorestframework



// simple jwt packages :- https://django-rest-framework-simplejwt.readthedocs.io/en/latest/getting_started.html
pip install djangorestframework-simplejwt





// setting.py
REST_FRAMEWORK = {
    'DEFAULT_AUTHENTICATION_CLASSES': (
        'rest_framework_simplejwt.authentication.JWTAuthentication',
    )
}


INSTALLED_APPS = [
    ...
    'rest_framework_simplejwt',
    ...
]



from datetime import timedelta

SIMPLE_JWT = {
    "ACCESS_TOKEN_LIFETIME": timedelta(minutes=5),
    "REFRESH_TOKEN_LIFETIME": timedelta(days=1),



    "AUTH_HEADER_TYPES": ("Bearer",),
    "AUTH_HEADER_NAME": "HTTP_AUTHORIZATION",
    "USER_ID_FIELD": "id",
    "USER_ID_CLAIM": "user_id",
    "USER_AUTHENTICATION_RULE": "rest_framework_simplejwt.authentication.default_user_authentication_rule",

    "AUTH_TOKEN_CLASSES": ("rest_framework_simplejwt.tokens.AccessToken",),
    "TOKEN_TYPE_CLAIM": "token_type",
    "TOKEN_USER_CLASS": "rest_framework_simplejwt.models.TokenUser",

    "JTI_CLAIM": "jti",


    "TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainPairSerializer",
    "TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSerializer",
    "TOKEN_VERIFY_SERIALIZER": "rest_framework_simplejwt.serializers.TokenVerifySerializer",
    "TOKEN_BLACKLIST_SERIALIZER": "rest_framework_simplejwt.serializers.TokenBlacklistSerializer",
    "SLIDING_TOKEN_OBTAIN_SERIALIZER": "rest_framework_simplejwt.serializers.TokenObtainSlidingSerializer",
    "SLIDING_TOKEN_REFRESH_SERIALIZER": "rest_framework_simplejwt.serializers.TokenRefreshSlidingSerializer",
}











// import i urls.py  it provide access token for login 
from rest_framework_simplejwt.views import (
    TokenObtainPairView,
    TokenRefreshView,
)

urlpatterns = [
    ...
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    ...
]

``` 




# course policy error
```
// https://pypi.org/project/django-cors-headers/
pip install django-cors-headers


// import in setting.py
INSTALLED_APPS = [
    ...,
    "corsheaders",
    ...,
]


// import in setting.py
MIDDLEWARE = [
    ...,
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
    ...,
]




// import in setting.py
CORS_ALLOWED_ORIGINS = [
    "http://localhost:3080",
    "http://127.0.0.1:3000",
]

```


# full example of customizing authentication 
```
// https://docs.djangoproject.com/en/4.0/topics/auth/customizing/#a-full-example


```



# Note :- Errors Detail Show like this in terminal
```
    {'email': [ErrorDetail(string='This field is required.', code='required')], 'name': [ErrorDetail(string='This field is required.', code='required')], 'password': [ErrorDetail(string='This field is required.', code='required')], 'password2': [ErrorDetail(string='This field is required.', code='required')], 'tc': [ErrorDetail(string='This field is required.', code='required')]}
```




# Creating tokens manually
```
// source :-  https://django-rest-framework-simplejwt.readthedocs.io/en/latest/creating_tokens_manually.html


from rest_framework_simplejwt.tokens import RefreshToken

def get_tokens_for_user(user):
    refresh = RefreshToken.for_user(user)

    return {
        'refresh': str(refresh),
        'access': str(refresh.access_token),
    }

```





# Note :- for getting current user profile then you basic need a token and then maro request in postman like [ Bearer <Toekn> ]  then jo user login honga wo aapko mil jayenga as a output

```
// for example 

// maro request on url :- http://127.0.0.1:8000/api/user/profile/

// write code in HTTP headers in postman 
Authorization  :   Bearer <Token>

```



# NOTE :-  Token will be use in :-
```
1) UserProfile Access
2)
```



#  PASSWORD_RESET_TIMEOUT  
```
PASSWORD_RESET_TIMEOUT = 900

```


# Email Send Process :-
```
// .env install for security  source :- https://github.com/jpadilla/django-doten
pip install django-dotenv
// put in manage.py
import dotenv
// write inside f() of manage.py
dotenv.read_dotenv()



// write code in .env file in chile project
EMAIL_USER = 'ankushgupta0510@gmail.com'
EMAIL_PASS = '123456'                          # write email password
EMAIL_FROM = 'ankushgupta0510@gmail.com'



// emai configuration put in seeting.py
import os
EMAIL_BACKEND = "django.core.mail.backends.mail.smtp.EmailBackend"
EMAIL_HOST = 'smtp.gmail.com'
EMAIL_PORT = 587
EMAIL_HOST_USER = os.environ.get('EMAIL_USER')  # access value of EMAIL_USER From .env file 
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_PASS')
EMAIL_USE_TLS = True



// make  other file utils.py in project app  and write your code.



// then in gmail account 'ankushgupta0510@gmail.com' enable like this  :-

Enhanced Safe Browsing for your account 
Less secure app access




```



#  Django email configuration
```
// source :-  https://docs.djangoproject.com/en/5.1/topics/email/
```