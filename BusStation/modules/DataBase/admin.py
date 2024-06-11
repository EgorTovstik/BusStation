from django.contrib import admin
from .models import (Buses, Cruises, Passengers, Documents, Stations,
                     Discounts, Tickets, Employes, Payment, Drivers,
                     Activity_logs, Countrys, Cruise_type, Carrier_organizations,
                     Carrier, Cruise_route, Cities, Regions, Districts,
                     Registration_method, Tariffs, Gender, City_type)


@admin.register(Buses)
class BusesAdmin(admin.ModelAdmin):
    list_display = ('id', 'model', 'capacity', 'bus_number')
@admin.register(Cruises)
class CruisesAdmin(admin.ModelAdmin):
    list_display = ('id', 'destination_city', 'city_arrival', 'dispatch_time', 'arrival_time', 'total_distance', )
@admin.register(Passengers)
class PassengersAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic', 'gender',
                    'birth_date', 'document_id', 'document_number', 
                    'citizenship', 'phone_number', 'Email')
@admin.register(Gender)
class GenderAdmin(admin.ModelAdmin):
    list_display = ('id', 'gender')
@admin.register(Documents)
class DocumentsAdmin(admin.ModelAdmin):
    list_display = ('id', 'document_type')
@admin.register(Stations)
class StationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'station_name', 'address', 'district_id')
@admin.register(Discounts)
class DiscountsAdmin(admin.ModelAdmin):
    list_display = ('id', 'description', 'discount_percent', 'start_date',
                    'end_date', 'document_confirming')
@admin.register(Tickets)
class TicketsAdmin(admin.ModelAdmin):
    list_display = ('id', 'cruise_id', 'passenger_id', 'registration_method_id',
                    'employe_id', 'discount_id', 'document_number', 'order_date',
                    'place_number', 'baggage')
admin.site.register(Employes)
class EmployesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 'patronymic', 'password',
                    'Email', 'post')
@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('id', 'payment_date', 'cost', 'payment_method', 'ticket_id')
@admin.register(Drivers)
class DriversAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'surname', 
                    'patronymic', 'license_number', 'phone_number')
@admin.register(Activity_logs)
class ActivityLogsAdmin(admin.ModelAdmin):
    list_display = ('id', 'employe_id', 'added_ticket_id', 'date_time')
@admin.register(Countrys)
class CountrysAdmin(admin.ModelAdmin):
    list_display = ('id', 'country_name')
@admin.register(Cruise_type)
class CruiseTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'cruise_type')
@admin.register(Carrier_organizations)
class CarrierOrganizationsAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization_name', 'organization_license')
@admin.register(Carrier)
class CarrierAdmin(admin.ModelAdmin):
    list_display = ('id', 'driver_id', 'organization_id', 'bus_id')
@admin.register(Cruise_route)
class CruiseRouteAdmin(admin.ModelAdmin):
    list_display = ('id', 'cruise_id', 'station_number', 'station_destination', 
                    'dispatch_time', 'station_arrival', 'arrival_time', 'distance')
@admin.register(Cities)
class CitiesAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'type', 'region_id')
@admin.register(City_type)
class CityTypeAdmin(admin.ModelAdmin):
    list_display = ('id', 'city_type')
@admin.register(Regions)
class RegionsAdmin(admin.ModelAdmin):
    list_display = ('id', 'region_name', 'country_id')
@admin.register(Districts)
class DistrictsAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'city_id')
@admin.register(Registration_method)
class RegistrationMethodAdmin(admin.ModelAdmin):
    list_display = ('id', 'description')
@admin.register(Tariffs)
class TariffsAdmin(admin.ModelAdmin):
    list_display = ('id', 'organization_id', 'price_per_km')

