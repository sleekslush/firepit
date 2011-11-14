from firepit import __version__
from firepit.campfire.connection import CampfireConnection
from firepit.ui import Dialog
from gi.repository import Gtk

class ConnectionDialog(Dialog):
    def __init__(self, application):
        """
        Constructs a connection dialog.
        """
        super(ConnectionDialog, self).__init__(
                'resources/connection_dialog.glade',
                'connection_dialog',
                application)

    def on_dialog_response(self, response_id):
        if response_id != Gtk.ResponseType.OK:
            return

        domain = self.get_widget('campfire_domain_entry').get_text()
        username = self.get_widget('campfire_username_entry').get_text()
        password = self.get_widget('campfire_password_entry').get_text()

        return CampfireConnection(domain, username, password)

class AboutDialog(Dialog):
    def __init__(self, application):
        """
        Constructs a new about dialog.
        """
        super(AboutDialog, self).__init__(
                'resources/about_dialog.glade',
                'about_dialog',
                application)

    def prepare_ui(self):
        """
        Sets all dynamic values in the UI.
        """
        self.widget.set_version(__version__)

class PreferencesDialog(Dialog):
    def __init__(self, application):
        """
        Constructs a preferences dialog.
        """
        super(PreferencesDialog, self).__init__(
                'resources/preferences_dialog.glade',
                'preferences_dialog',
                application)
