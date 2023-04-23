from django.contrib import admin
from .models import Sorting, Shop, Feedbackall


# class ShopAdmin(admin.ModelAdmin):
#     readonly_fields = ('created',)

# readonly_fields принимает либо кортеж либо список. Только для чтения.


class FeedbackallAdmin(admin.ModelAdmin):
    readonly_fields = ('created',)




admin.site.register(Sorting)
admin.site.register(Shop)
admin.site.register(Feedbackall)















