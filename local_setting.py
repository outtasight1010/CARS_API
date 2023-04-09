# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-do#=@p*dqil6itxur@%rf4t61^1*6ybcjj#amu=(x7!2^di##6'

# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'cars_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}