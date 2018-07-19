from .base import *

SECRET_KEY = env('DJANGO_SECRET_KEY', default='&(kcen5xwk^vgxblzh$qyqm1eliackx&ipad1w=f1tjmwo=3*l')
DEBUG = env.bool('DJANGO_DEBUG', default=True)