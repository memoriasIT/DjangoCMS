from django.contrib import admin

# Register your models here.
from .models import Posts

class PostModelAdmin(admin.ModelAdmin):
	list_display = ["title", "created_at", "id"]
	search_fields = ["title", "body"]

	#change_form_template = '/templates/admin/change_form.html'

	class Meta:
		model = Posts


admin.site.register(Posts, PostModelAdmin)