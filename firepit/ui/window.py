from firepit import __version__
from firepit.ui import Window
from firepit.ui.dialog import AboutDialog, ConnectionDialog, PreferencesDialog
from gi.repository import WebKit

class MainWindow(Window):
    def __init__(self, application):
        """
        Constructs a new MainWindow.
        """
        super(MainWindow, self).__init__(
                'resources/main_window.glade',
                'main_window',
                application)

    def prepare_ui(self):
        """
        Adds a WebKit.WebView widget to the chat view.
        """
        self.set_toolbar_visibility()
        #self.set_user_list_vibility()
        #self.set_room_list_visibility()
        #self.set_upload_list_visibility()

        webkit_view = WebKit.WebView()
        webkit_view.load_html_string('<b>hi there!</b>', 'utf-8')
        self.get_widget('chat_scrolled_window').add(webkit_view)

    def set_toolbar_visibility(self):
        is_visible = self.set_default_widget_visibility('toolbar', 'show-toolbar')
        self.get_widget('view_toolbar_menu_item').set_active(is_visible)

    def set_default_widget_visibility(self, widget_name, settings_name):
        is_visible = self.application.settings.get_boolean(settings_name)
        self.get_widget(widget_name).set_visible(is_visible)
        return is_visible

    def connect_signals(self):
        """
        Connects signals from all of the user-actionable widgets in this MainWindow.
        """
        self.connect_menu_signals()
        self.connect_toolbar_signals()

    def connect_menu_signals(self):
        """
        Connects menu item signals.
        """
        # File menu
        self.connect_signal('connect_menu_item', 'activate', self.on_new_connection_event)
        self.connect_signal('disconnect_menu_item', 'activate', self.on_disconnect_event)
        self.connect_signal('join_room_menu_item', 'activate', self.on_join_room_event)
        self.connect_signal('leave_room_menu_item', 'activate', self.on_leave_room_event)
        self.connect_signal('quit_menu_item', 'activate', self.application.quit)

        # Edit menu
        self.connect_signal('preferences_menu_item', 'activate', self.on_preferences_event)

        # View menu
        self.connect_signal('view_toolbar_menu_item', 'toggled', self.on_view_toolbar_toggle)
        self.connect_signal('view_room_list_menu_item', 'toggled', self.on_view_room_list_toggle)
        self.connect_signal('view_user_list_menu_item', 'toggled', self.on_view_user_list_toggle)
        self.connect_signal('view_upload_list_menu_item', 'toggled', self.on_view_upload_list_toggle)

        # Help menu
        self.connect_signal('about_menu_item', 'activate', self.on_about_event)

    def on_new_connection_event(self, widget):
        connection_verified = False

        while not connection_verified:
            campfire_connection = ConnectionDialog(self.application).show()

            if not campfire_connection:
                return

            try:
                campfire_connection.connect()
            except:
                # connection error!
                pass
            else:
                connection_verified = True

    def on_disconnect_event(self, widget):
        pass

    def on_join_room_event(self, widget):
        pass

    def on_leave_room_event(self, widget):
        pass

    def on_preferences_event(self, widget):
        """
        Shows the preferences dialog.
        """
        PreferencesDialog(self.application).show()

    def on_view_toolbar_toggle(self, widget):
        """
        """
        is_active = widget.get_active()
        self.get_widget('toolbar').set_visible(is_active)
        self.application.settings.set_boolean('show-toolbar', is_active)

    def on_view_room_list_toggle(self, widget):
        pass

    def on_view_user_list_toggle(self, widget):
        pass

    def on_view_upload_list_toggle(self, widget):
        pass

    def on_about_event(self, widget):
        """
        Shows the about dialog.
        """
        AboutDialog(self.application).show()

    def connect_toolbar_signals(self):
        self.connect_signal('connect_button', 'clicked', self.on_new_connection_event)
        self.connect_signal('preferences_button', 'clicked', self.on_preferences_event)
