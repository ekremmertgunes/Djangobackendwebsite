from django.contrib import admin

from .models import Services,About,Comments,BuildPackets,UserPackets

admin.site.register(Services)
admin.site.register(About)
admin.site.register(Comments)
admin.site.register(BuildPackets)
admin.site.register(UserPackets)

