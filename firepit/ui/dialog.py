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

        subdomain = self.get_widget('subdomain_entry').get_text()
        username = self.get_widget('username_entry').get_text()
        password = self.get_widget('password_entry').get_text()
        enable_ssl = self.get_widget('ssl_check_button').get_active()

        return CampfireConnection(subdomain, username, password, enable_ssl)

class PreferencesDialog(Dialog):
    def __init__(self, application):
        """
        Constructs a preferences dialog.
        """
        super(PreferencesDialog, self).__init__(
                'resources/preferences_dialog.glade',
                'preferences_dialog',
                application)

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

class MessageDialog(Gtk.MessageDialog):
    def __init__(self, message_type, button_type, parent, title, message):
        super(MessageDialog, self).__init__(
                parent,
                Gtk.DialogFlags.DESTROY_WITH_PARENT,
                message_type,
                button_type,
                message)

        self.set_title(title)

    def run(self):
        result = super(MessageDialog, self).run()
        self.destroy()
        return result

class ErrorDialog(MessageDialog):
    def __init__(self, parent, title, message, secondary_message):
        super(ErrorDialog, self).__init__(
                Gtk.MessageType.ERROR,
                Gtk.ButtonsType.CLOSE,
                parent,
                title,
                message)

        self.format_secondary_text(secondary_message)
