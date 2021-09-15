from django.contrib import admin
from django.forms import ModelChoiceField, ModelForm, ValidationError
from django.utils.safestring import mark_safe

from PIL import Image

from .models import *



class FieldsAdminForm(ModelForm): #Этот класс дополняет оформление полей при создании товара в админке

    def __init__(self,*args,**kwargs): #Функция выоводит вспомогательный текст для поля ['image'] при создании товара

         super().__init__(*args,**kwargs)
         self.fields['image'].help_text =mark_safe(
             """<span style="color:red; font-size:13px;">При загрузке изображения размером больше {}x{} оно будет обрезано</span>
             """.format(
                 *Product.MAX_RESOLUTION
            )
         )


    def clean_image(self):#Проверка добавляемого изображения на соблюдение условий
        #по объему изображения - .size и размеру изображения - img.width, img.height
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_img_width, min_img_height = Product.MIN_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 3Mb')
        if img.width < min_img_width or img.height < min_img_height:
            raise ValidationError('Загруженное изображение меньше минимального разрешения')


class NotebookAdmin(admin.ModelAdmin):

    form = FieldsAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs):
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='notebooks'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


class SmatphoneAdminForm(ModelForm):

    def __init__(self, *args,
                 **kwargs):  # Функция выоводит вспомогательный текст для поля ['image'] при создании товара

        super().__init__(*args, **kwargs)
        self.fields['image'].help_text = mark_safe(
            """<span style="color:red; font-size:13px;">При загрузке изображения размером больше {}x{} оно будет обрезано</span>
            """.format(
                *Product.MAX_RESOLUTION
            )
        )

        instance = kwargs.get('instance')
        if not instance.sd:# Это условие проверяет поле sd, если его значение =False, то выполняется условие
            # в котором атрибуту readonly (только чтение) дается значение True ('readonly': True)
            self.fields['sd_volume_max'].widget.attrs.update({
                'readonly': True, 'style': 'background: lightgray'
            })

    def clean_image(self):  # Проверка добавляемого изображения на соблюдение условий
        # по объему изображения - .size и размеру изображения - img.width, img.height
        image = self.cleaned_data['image']
        img = Image.open(image)
        min_img_width, min_img_height = Product.MIN_RESOLUTION
        if image.size > Product.MAX_IMAGE_SIZE:
            raise ValidationError('Размер изображения не должен превышать 3Mb')
        if img.width < min_img_width or img.height < min_img_height:
            raise ValidationError('Загруженное изображение меньше минимального разрешения')


    def clean(self):
        if not self.cleaned_data['sd']:
            self.cleaned_data['sd_volume_max'] = None
        return self.cleaned_data

class SmartphoneAdmin(admin.ModelAdmin):


    change_form_template = 'admin.html'

    form = SmatphoneAdminForm

    def formfield_for_foreignkey(self, db_field, request, **kwargs): # Эта функция дает выбрать только определенную
        # категорию при создании товара. Например: если создаешь товар категории smartphones, то в поле выбора категории
        # возможно будет выбрать только категорию smartphones
        if db_field.name == 'category':
            return ModelChoiceField(Category.objects.filter(slug='smartphones'))
        return super().formfield_for_foreignkey(db_field, request, **kwargs)


admin.site.register(Category)
admin.site.register(Cart)
admin.site.register(CartProduct)
admin.site.register(Customer)
admin.site.register(Smartphone, SmartphoneAdmin)
admin.site.register(Notebook, NotebookAdmin)




# Register your models here.
