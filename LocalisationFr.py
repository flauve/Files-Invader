__author__ = 'root'

from enum import Enum

class LocalisationFr(Enum):

    WINDOW_PROGRAM_NAME = "Files Invader"

    TEXT_BROWSE = "Parcourir"

    PANEL_POLLUTE = "Polution"
    PANEL_POLLUTE_CONTENT = "Content pollution blablablablablabla"
    PANEL_POLLUTE_BUTTON = "Polluer"

    PANEL_UNPOLLUTE = "Dépolution"
    PANEL_UNPOLLUTE_CONTENT = "Content dépollution blablablablablabla"
    PANEL_UNPOLLUTE_BUTTON = "Dépolluer"

    PANEL_ABOUT = "A propos"
    PANEL_ABOUT_CONTENT = "Files Invader a été créé par Florian VAUTARD. Il est possible de l'utiliser et de le modifier mais en\n ancun cas de" \
                  " de le vendre sans son autorisation."

    MESSAGE_INFORMATION = "Information"
    MESSAGE_WARNING = "Attention"
    MESSAGE_ERROR = "Erreur"