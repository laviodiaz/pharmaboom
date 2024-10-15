from django.db import models


class DrugStatus(models.Model):
    drug_status = models.CharField(max_length=25, verbose_name="Статус наличия товара")

    class Meta:
        verbose_name_plural = "Статусы наличия"
        ordering = ['drug_status']

    def __str__(self):
        return f'{self.drug_status}'


class OrderStatus(models.Model):
    order_status = models.CharField(max_length=25, verbose_name="Статус заказа")

    class Meta:
        verbose_name_plural = "Статусы заказа"
        ordering = ['order_status']

    def __str__(self):
        return f'{self.order_status}'


class WorkStatus(models.Model):
    work_status = models.CharField(max_length=25, verbose_name="Статус работы аптеки")

    class Meta:
        verbose_name_plural = "Статусы работы"
        ordering = ['work_status']

    def __str__(self):
        return f'{self.work_status}'


class Country(models.Model):
    counry_name = models.CharField(max_length=50, verbose_name="Страна")

    class Meta:
        verbose_name_plural = "Страны"
        ordering = ['counry_name']

    def __str__(self):
        return f'{self.counry_name}'


class City(models.Model):
    city_name = models.CharField(max_length=25, verbose_name="Город")
    country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Города"
        ordering = ['city_name']

    def __str__(self):
        return f'{self.city_name}, {self.country}'


class Corporation(models.Model):
    corp_name = models.CharField(max_length=50, verbose_name='Наименование производителя')
    corp_country = models.ForeignKey(Country, on_delete=models.DO_NOTHING)

    class Meta:
        verbose_name_plural = "Производители"
        ordering = ['corp_name']

    def __str__(self):
        return f'{self.corp_name}'


class Brand(models.Model):
    brand_name = models.CharField(max_length=50, verbose_name='Название бренда')

    class Meta:
        verbose_name_plural = "Бренды>"
        ordering = ['brand_name']

    def __str__(self):
        return f'{self.brand_name}'


class DrugForm(models.Model):
    form_name = models.CharField(max_length=50, verbose_name='Лекарственная форма')

    class Meta:
        verbose_name_plural = "Лекарственные формы"
        ordering = ['form_name']

    def __str__(self):
        return f'{self.form_name}'


class DrugType(models.Model):
    drug_type = models.CharField(max_length=50, verbose_name='Форма отпуска')

    class Meta:
        verbose_name_plural = "Формы отпуска"
        ordering = ['drug_type']

    def __str__(self):
        return f'{self.drug_type}'


class Drug(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование препарата')
    corp = models.ForeignKey(Corporation, on_delete=models.DO_NOTHING)
    photo = models.ImageField(upload_to='products/', null=True, blank=True)
    brand = models.ForeignKey(Brand, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(DrugStatus, on_delete=models.DO_NOTHING)
    drug_form = models.ForeignKey(DrugForm, on_delete=models.DO_NOTHING)
    drug_type = models.ForeignKey(DrugType, on_delete=models.DO_NOTHING)
    price = models.DecimalField(max_digits=6, decimal_places=2, verbose_name='Цена товара, сом')
    amount = models.IntegerField(verbose_name='Количество')

    def __str__(self):
        return f'{self.name} {self.corp}'

    class Meta:
        verbose_name_plural = "Лекарственные средства"
        ordering = ['name']

class ProductEntry(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    drug = models.ForeignKey(Drug, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()
    entry_date = models.DateField()

    class Meta:
        verbose_name_plural = "Приходы"
        ordering = ['entry_date']

    def __str__(self):
        return f'{self.drug} {self.entry_date}'

class Product(models.Model):
    price = models.DecimalField(max_digits=6, decimal_places=2)
    drug = models.ForeignKey(Drug, on_delete=models.DO_NOTHING)
    amount = models.IntegerField()

    class Meta:
        verbose_name_plural = "Товары"
        ordering = ['drug']

    def __str__(self):
        return f'{self.drug}'


class PharmChain(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование сети')
    status = models.ForeignKey(WorkStatus, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=50, verbose_name='Адрес')

    def __str__(self):
        return f'{self.name}'

    class Meta:
        verbose_name_plural = "Аптечные сети"
        ordering = ['name']


class Pharmacy(models.Model):
    name = models.CharField(max_length=50, verbose_name='Наименование аптеки')
    pharm_chain = models.ForeignKey(PharmChain, on_delete=models.DO_NOTHING)
    status = models.ForeignKey(WorkStatus, on_delete=models.DO_NOTHING)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    address = models.CharField(max_length=50, verbose_name='Адрес')

    def __str__(self):
        return f'{self.name}, город {self.city}, {self.address}'

    class Meta:
        verbose_name_plural = "Аптеки"
        ordering = ['name']

    # class Manager(models.Model):
    #     name = models.CharField(max_length=50, verbose_name='Имя менеджера')
    #     surname = models.CharField(max_length=50, verbose_name='Фамилия менеджера')
    #     pharm_chain = models.ForeignKey(PharmChain, on_delete=models.DO_NOTHING)
    #     email = models.EmailField(verbose_name="Электронная почта")
    #     password = models.CharField(max_length=50, verbose_name="Пароль")
    #     status = models.CharField(max_length=50, verbose_name='Статус')

    # def __str__(self):
    #     return f'{self.surname} {self.name} {self.chain} {self.status}'
    #
    # class Meta:
    #     verbose_name_plural = "Менеджеры"
    #     ordering = ['surname'], ['chain']
