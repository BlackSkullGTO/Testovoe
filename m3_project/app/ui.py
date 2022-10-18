from m3_ext.ui import all_components as ext
from m3_ext.ui.fields.complex import ExtDictSelectField

from objectpack.ui import BaseEditWindow
from objectpack.ui import ObjectGridTab
from objectpack.ui import ObjectTab
from objectpack.ui import TabbedEditWindow
import six

from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import Permission

from datetime import date

from .controller import observer
from . import actions

class UserAddWindow(BaseEditWindow):

    def _init_components(self):
        """
        Здесь следует инициализировать компоненты окна и складывать их в
        :attr:`self`.
        """
        super(UserAddWindow, self)._init_components()

        self.field__password = ext.ExtStringField(
            label=u'Пароль',
            name='password',
            allow_blank=False,
            anchor='100%')

        self.field__last_login = ext.ExtDateField(
            label=u'Последняя авторизация',
            name='last_login',
            format='d.m.Y',
            allow_blank=True,
            anchor='100%')

        self.field__superuser_status = ext.ExtCheckBox(
            label=u'Супер пользователь',
            name='superuser_status',
            anchor='100%')

        self.field__username = ext.ExtStringField(
            label=u'Логин',
            name='username',
            allow_blank=False,
            anchor='100%',
            # vtype=User.username_validator,
            max_length_text=150)

        self.field__first_name = ext.ExtStringField(
            label=u'Имя',
            name='first_name',
            allow_blank=True,
            anchor='100%',
            max_length_text=150)

        self.field__last_name = ext.ExtStringField(
            label=u'Фамилия',
            name='last_name',
            allow_blank=True,
            anchor='100%',
            max_length_text=150)

        self.field__email = ext.ExtStringField(
            label=u'E-mail',
            name='email',
            allow_blank=True,
            anchor='100%',
            max_length_text=150)

        self.field__staff_status = ext.ExtCheckBox(
            label=u'Персонал',
            name='staff_status',
            anchor='100%')

        self.field__active = ext.ExtCheckBox(
            label=u'Действительный',
            name='active',
            checked=True,
            anchor='100%')

        self.field__date_joined = ext.ExtDateField(
            label=u'Дата создания',
            name='date_joined',
            allow_blank=False,
            format='d.m.Y',
            value=date.today().strftime('%d.%m.%Y'),
            anchor='100%')

    def _do_layout(self):
        """
        Здесь размещаем компоненты в окне
        """
        super(UserAddWindow, self)._do_layout()
        self.form.items.extend((
            self.field__password,
            self.field__last_login,
            self.field__superuser_status,
            self.field__username,
            self.field__first_name,
            self.field__last_name,
            self.field__email,
            self.field__staff_status,
            self.field__active,
            self.field__date_joined,
        ))

    def set_params(self, params):
        """
        Установка параметров окна

        :params: Словарь с параметрами, передается из пака
        """
        super(UserAddWindow, self).set_params(params)
        self.height = 'auto'

class PermissionTab(ObjectTab.fabricate(
    model=Permission, field_list=('name', 'content_type__id', 'codename',))):

    def init_components(self, *args, **kwargs):
        super(PermissionTab, self).init_components(*args, **kwargs)

        self._content_type_field = ExtDictSelectField(
            label='Content Type')
        self._controls.append(self._content_type_field)
    
    def set_params(self, *args, **kwargs):
        super(PermissionTab, self).set_params(*args, **kwargs)
        
        self._content_type_field.pack = actions.ContentTypePack
        self._content_type_field.display_field = (
            '__unicode__' if six.PY2 else '__str__'
        )
        # self._content_type_field.fields = ('app_label')


class PermissionEditWindow(TabbedEditWindow):
    tabs = [
        PermissionTab,
        # ObjectGridTab.fabricate_from_pack(
        #     pack_name='m3_project.app.actions.ContentTypePack',
        #     # tab_class_name='app_label',
        #     pack_register=observer,
        # ),
    ]

# class PermissionAddWindow(BaseEditWindow):

#     def _init_components(self):
#         """
#         Здесь следует инициализировать компоненты окна и складывать их в
#         :attr:`self`.
#         """
#         super(PermissionAddWindow, self)._init_components()

#         self.field__name = ext.ExtStringField(
#             label='Name',
#             name='name',
#             allow_blank=False,
#             anchor='100%',
#             max_length_text=255)

#         self.field__content_type = make_combo_box(
#             label='Content Type',
#             name='content_type',
#             allow_blank=False,
#             anchor='100%',
#             data=ContentType)

#         self.field__codename = ext.ExtStringField(
#             label='Codename',
#             name='codename',
#             allow_blank=False,
#             anchor='100%',
#             max_length_text=100)

#     def _do_layout(self):
#         """
#         Здесь размещаем компоненты в окне
#         """
#         super(PermissionAddWindow, self)._do_layout()
#         self.form.items.extend((
#             self.field__name,
#             self.field__content_type,
#             self.field__codename,
#         ))

#     def set_params(self, params):
#         """
#         Установка параметров окна

#         :params: Словарь с параметрами, передается из пака
#         """
#         super(PermissionAddWindow, self).set_params(params)
#         self.height = 'auto'