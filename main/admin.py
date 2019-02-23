from django.contrib import admin
from .models import Tutorial,TutorialCategory,TutorialSeries
#from tinymce.widgets import TinyMCE
from django.db import models

# Register your models here.
class TutorialAdmin(admin.ModelAdmin):

    fields = ["tutorial_title",
              "tutorial_published",
              "tutorial_content",
              "tutorial_series",
              "tutorial_slug"]

    # formfield_overrides = {
    #     models.TextField: {'widget': TinyMCE()},
    #     }

admin.site.register(TutorialSeries)
admin.site.register(TutorialCategory)
admin.site.register(Tutorial,TutorialAdmin)