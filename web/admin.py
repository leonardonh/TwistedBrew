from django.contrib import admin
# imports from within the Django web_x app must be scoped below the web_x package
from models import Brew, Worker, Measurement, Command

admin.site.register(Brew)
admin.site.register(Worker)
admin.site.register(Measurement)
admin.site.register(Command)