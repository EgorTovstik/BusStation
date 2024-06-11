from django.db import models


class Buses(models.Model):
    model = models.CharField(verbose_name='модель', max_length=100)
    capacity = models.IntegerField(verbose_name='вместимость')
    bus_number = models.CharField(verbose_name='гос. номер', max_length=10)

    class Meta:
        verbose_name = 'Автобус'
        verbose_name_plural = 'Автобусы'

    def __str__(self):
        return f'{self.model} {self.bus_number}'

class Cruises(models.Model):
    destination_city = models.ForeignKey('Cities',
                                         related_name='destination_city',
                                         verbose_name='город отправления', 
                                         on_delete=models.CASCADE)
    city_arrival = models.ForeignKey('Cities', 
                                    related_name='city_arrival',
                                    verbose_name='город прибытия', 
                                    on_delete=models.CASCADE)
    dispatch_time = models.DateTimeField(verbose_name='время отправления')
    arrival_time = models.DateTimeField(verbose_name='время прибытия')
    total_distance = models.IntegerField(verbose_name='общее расстояние')
    organization_id = models.ForeignKey('Carrier',
                                        verbose_name='код перевозчика',
                                        on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Рейс'
        verbose_name_plural = 'Рейсы'

    def __str__(self):
        return f'{self.id}'
    
class Gender(models.Model):
    gender = models.CharField(verbose_name='пол', max_length=1)

    class Meta:
        verbose_name = 'Пол'
        verbose_name_plural = 'Пол'

    def __str__(self):
        return f'{self.gender}'

class Passengers(models.Model):
    name = models.CharField(verbose_name='имя', max_length=50)
    surname = models.CharField(verbose_name='фамилия', max_length=50)
    patronymic = models.CharField(verbose_name='отчество', max_length=50, null=True)
    gender = models.ForeignKey('Gender', 
                               verbose_name='пол', 
                               on_delete=models.CASCADE)
    birth_date = models.DateField(verbose_name='дата рождения')
    document_id = models.ForeignKey('Documents',
                                    verbose_name='id документа',
                                    on_delete=models.CASCADE)
    document_number = models.CharField(verbose_name='номер документа', max_length=10)
    citizenship = models.CharField(verbose_name='гражданство', max_length=50)
    phone_number = models.CharField(verbose_name='номер телефона', max_length=15)
    Email = models.CharField(verbose_name='электронная почта', max_length=100, null=True)

    class Meta:
        verbose_name = 'Пассажир'
        verbose_name_plural = 'Пассажиры'

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronymic}'

class Documents(models.Model):
    document_type = models.CharField(verbose_name='тип документа', max_length=50)

    class Meta:
        verbose_name = 'Документ'
        verbose_name_plural = 'Документы'

    def __str__(self):
        return f'{self.document_type}'

class Stations(models.Model):
    station_name = models.CharField(verbose_name='название станции', max_length=100)
    address = models.CharField(verbose_name='адрес', max_length=255)
    district_id = models.ForeignKey('Districts',
                                    verbose_name='Район',
                                    on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Станция'
        verbose_name_plural = 'Станции'

    def __str__(self):
        return f'{self.station_name} {self.city_id} {self.address}'

class Discounts(models.Model):
    description = models.TextField(verbose_name='описание', max_length=500)
    discount_percent = models.IntegerField()
    start_date = models.DateTimeField(verbose_name='действует с', null=True)
    end_date = models.DateTimeField(verbose_name='действует до', null=True)
    document_confirming = models.ForeignKey('Documents',
                                            verbose_name='документ подтверждающий скидку',
                                            on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Скидка'
        verbose_name_plural = 'Скидки'

    def __str__(self):
        return f'{self.description}'

class Tickets(models.Model):
    cruise_id = models.ForeignKey('Cruises',
                                  verbose_name='рейс id',
                                  on_delete=models.CASCADE)
    passenger_id = models.ForeignKey('Passengers',
                                     verbose_name='пассажир id',
                                     on_delete=models.CASCADE)
    registration_method_id = models.ForeignKey('Registration_method',
                                               verbose_name='способ оформления id',
                                               on_delete=models.CASCADE)
    employe_id = models.ForeignKey('Employes',
                                   verbose_name='сотрудник id',
                                   on_delete=models.CASCADE)
    discount_id = models.ForeignKey('Discounts',
                                    verbose_name='скидка id',
                                    on_delete=models.CASCADE,
                                    null=True)
    document_number = models.CharField(verbose_name='номер документа', max_length=10)
    order_date = models.DateTimeField(verbose_name='дата заказа')
    place_number = models.IntegerField(verbose_name='номер места')
    baggage = models.IntegerField(verbose_name='багаж')

    class Meta:
        verbose_name = 'Билет'
        verbose_name_plural = 'Билеты'

    def __str__(self):
        return f'{self.id}'
    
class Employes(models.Model):
    name = models.CharField(verbose_name='имя', max_length=50)
    surname = models.CharField(verbose_name='фамилия', max_length=50)
    patronymic = models.CharField(verbose_name='отчество', max_length=50, null=True)
    password = models.CharField(verbose_name='пароль', max_length=250)
    Email = models.CharField(verbose_name='электронная почта', max_length=100)
    post = models.CharField(verbose_name='должность', max_length=50)

    class Meta:
        verbose_name = 'Сотрудник'
        verbose_name_plural = 'Сотрудники'

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronymic}'
    
class Payment(models.Model):
    payment_date = models.DateTimeField(verbose_name='дата платежа')
    cost = models.DecimalField(verbose_name='стоимость',
                               max_digits=10,
                               decimal_places=2)
    payment_method = models.CharField(max_length=50)
    ticket_id = models.ForeignKey('Tickets',
                                  verbose_name='билет id',
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Оплата'
        verbose_name_plural = 'Оплата'

    def __str__(self):
        return f'{self.id}'
    
class Drivers(models.Model):
    name = models.CharField(verbose_name='имя', max_length=50)
    surname = models.CharField(verbose_name='фамилия', max_length=50)
    patronymic = models.CharField(verbose_name='отчество', max_length=50, null=True)
    license_number = models.CharField(verbose_name='номер лицензии', max_length=50)
    phone_number = models.CharField(verbose_name='Номер телефона', max_length=15)

    class Meta:
        verbose_name = 'Водитель'
        verbose_name_plural = 'Водители'

    def __str__(self):
        return f'{self.name} {self.surname} {self.patronymic}'

class Activity_logs(models.Model):
    employe_id = models.ForeignKey('Employes',
                                   verbose_name='сотрудник id',
                                   on_delete=models.CASCADE)
    added_ticket_id = models.ForeignKey('Tickets',
                                        verbose_name='добавленный билет',
                                        on_delete=models.CASCADE)
    date_time = models.DateTimeField()

    class Meta:
        verbose_name = 'Логи активности'
        verbose_name_plural = 'Логи активности'

    def __str__(self):
        return f'{self.id}'

class Countrys(models.Model):
    country_name = models.CharField(verbose_name='название страны', max_length=50)

    class Meta:
        verbose_name = 'Страна'
        verbose_name_plural = 'Страны'

    def __str__(self):
        return f'{self.country_name}'

class Cruise_type(models.Model):
    cruise_type = models.CharField(verbose_name='тип рейса', max_length=50)

    class Meta:
        verbose_name = 'Тип рейса'
        verbose_name_plural = 'Тип рейса'
   
    def __str__(self):
        return f'{self.cruise_type}'

class Carrier_organizations(models.Model):
    organization_name = models.CharField(verbose_name='название организации', max_length=100)
    organization_license = models.CharField(verbose_name='лицензия перевозчика', max_length=100)

    class Meta:
        verbose_name = 'Организация перевозчик'
        verbose_name_plural = 'Организации перевозчики'
   
    def __str__(self):
        return f'{self.organization_name}'

class Carrier(models.Model):
    driver_id = models.ForeignKey('Drivers',
                                  verbose_name='Водитель id',
                                  on_delete=models.CASCADE)
    organization_id = models.ForeignKey('Carrier_organizations',
                                        verbose_name='организация id',
                                        on_delete=models.CASCADE)
    bus_id = models.ForeignKey('Buses',
                               verbose_name='автобус id',
                               on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Перевозчик'
        verbose_name_plural = 'Перевозчики'

    def __str__(self):
        return f'{self.id}'
    
class Cruise_route(models.Model):
    cruise_id = models.ForeignKey('Cruises',
                                  verbose_name='рейс id',
                                  on_delete=models.CASCADE)
    station_number = models.IntegerField()
    station_destination = models.ForeignKey('Stations',
                                            related_name='station_destination',
                                            verbose_name='станция отправления',
                                            on_delete=models.CASCADE)
    dispatch_time = models.DateTimeField(verbose_name='время отправления')
    station_arrival = models.ForeignKey('Stations',
                                        related_name='station_arrival',
                                        verbose_name='станция прибытия',
                                        on_delete=models.CASCADE)
    arrival_time = models.DateTimeField(verbose_name='время прибытия')
    distance = models.IntegerField()

    class Meta:
        verbose_name = 'Маршрут рейса'
        verbose_name_plural = 'Маршруты рейсов'

    def __str__(self):
        return f'{self.id}'

class Cities(models.Model):
    name = models.CharField(verbose_name='название', max_length=50)
    type = models.ForeignKey('City_type',
                            verbose_name='тип населенного пункта',
                            on_delete=models.CASCADE)
    region_id = models.ForeignKey('Regions',
                                  verbose_name='регион id',
                                  on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Город'
        verbose_name_plural = 'Города'

    def __str__(self):
        return f'{self.name}'

class City_type(models.Model):
    city_type = models.CharField(verbose_name='Тип населенного пункта', max_length=100)

    class Meta:
        verbose_name = 'Тип города'
        verbose_name_plural = 'Типы городов'

    def __str__(self):
        return f'{self.city_type}'
    
class Regions(models.Model):
    region_name = models.CharField(verbose_name='название региона',
                                   max_length=100)
    country_id = models.ForeignKey('Countrys',
                                   verbose_name='страна id',
                                   on_delete=models.CASCADE)

    class Meta:
        verbose_name = 'Регион'
        verbose_name_plural = 'Регионы'

    def __str__(self):
        return f'{self.region_name}'

class Districts(models.Model):
    name = models.CharField(verbose_name='название района',
                            max_length=100)
    city_id = models.ForeignKey('Cities',
                                verbose_name='город id',
                                on_delete=models.CASCADE)
    class Meta:
        verbose_name = 'Район'
        verbose_name_plural = 'Районы'

    def __str__(self):
        return f'{self.name}'
    
class Registration_method(models.Model):
    description = models.CharField(verbose_name='оформление билета', max_length=50)

    class Meta:
        verbose_name = 'Способ оформления'
        verbose_name_plural = 'Способ оформления'

    def __str__(self):
        return f'{self.description}'

class Tariffs(models.Model):
    organization_id = models.ForeignKey('Carrier',
                                        verbose_name='код перевозчика',
                                        on_delete=models.CASCADE)
    price_per_km = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        verbose_name = 'Тариф'
        verbose_name_plural = 'Тарифы'

    def __str__(self):
        return f'{self.id}'
    