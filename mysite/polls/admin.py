from django.contrib import admin
from polls.models import Poll, Choice


# Register your models here.

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    fieldsets =  [
        (None,              { 'fields':['question'] }),
        ('Date Infomation', { 'fields':['pub_date'], 'classes': ['collapse'] })
    ]
    inlines = [ChoiceInline]
    list_display = ['question', 'pub_date', 'was_publish_recently']


admin.site.register(Poll, PollAdmin)
