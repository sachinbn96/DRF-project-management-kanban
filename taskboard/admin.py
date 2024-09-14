from django.contrib import admin
from taskboard.models import (TaskBoard, Task)

# Register your models here.
admin.site.register([TaskBoard, Task])
