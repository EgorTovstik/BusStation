from django.contrib import admin
from .models import (Buses, Cruises, Passengers, Documents, Stations,
                     Discounts, Tickets, Employes, Payment, Drivers,
                     Activity_logs, Countrys, Cruise_type, Carrier_organizations,
                     Carrier, Cruise_route, Cities, Regions, Districts,
                     Registration_method, Tariffs)


admin.site.register(Buses)
admin.site.register(Cruises)
admin.site.register(Passengers)
admin.site.register(Documents)
admin.site.register(Stations)
admin.site.register(Discounts)
admin.site.register(Tickets)
admin.site.register(Employes)
admin.site.register(Payment)
admin.site.register(Drivers)
admin.site.register(Activity_logs)
admin.site.register(Countrys)
admin.site.register(Cruise_type)
admin.site.register(Carrier_organizations)
admin.site.register(Carrier)
admin.site.register(Cruise_route)
admin.site.register(Cities)
admin.site.register(Regions)
admin.site.register(Districts)
admin.site.register(Registration_method)
admin.site.register(Tariffs)

