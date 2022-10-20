from objectpack.actions import ObjectPack
from objectpack.slave_object_pack.actions import SlavePack
from objectpack.ui import ModelEditWindow, _create_dict_select_field
from django.contrib.contenttypes.models import ContentType
from django.contrib.auth.models import User
from django.contrib.auth.models import Group
from django.contrib.auth.models import Permission

from . import ui
from .controller import observer

class ContentTypePack(ObjectPack):

    model = ContentType
    add_to_desktop = True
    add_to_menu = True

    edit_window = add_window = ModelEditWindow.fabricate(model)


class UserPack(ObjectPack):

    model = User
    add_to_desktop = True
    add_to_menu = True

    edit_window = add_window = ui.UserAddWindow


class GroupPack(ObjectPack):

    model = Group
    add_to_desktop = True
    add_to_menu = True

    edit_window = add_window = ModelEditWindow.fabricate(model)


class PermissionPack(ObjectPack):

    model = Permission
    add_to_desktop = True
    add_to_menu = True


    add_window = edit_window = ModelEditWindow.fabricate(
        model=model, model_register=observer)
