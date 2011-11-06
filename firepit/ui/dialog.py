from firepit import __version__
from firepit.ui import Dialog
from gi.repository import Gtk

class AboutDialog(Dialog):
    def __init__(self, application):
        super(AboutDialog, self).__init__('about_dialog', application)

    def init_ui(self):
        self.widget.set_version(__version__)

class PreferencesDialog(Dialog):
    def __init__(self, application):
        super(PreferencesDialog, self).__init__('preferences_dialog', application)

    def on_dialog_response(self, response_id):
        pass
