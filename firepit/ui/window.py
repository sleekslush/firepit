from firepit import __version__
from firepit.ui import Window
from firepit.ui.dialog import AboutDialog, PreferencesDialog
from gi.repository import WebKit

class MainWindow(Window):
    def __init__(self, application):
        """
        Constructs a new MainWindow.
        """
        super(MainWindow, self).__init__('main_window', application)

    def prepare_ui(self):
        """
        Adds a WebKit.WebView widget to the chat view.
        """
        webkit_view = WebKit.WebView()
        webkit_view.load_html_string('<b>hi there!</b>', 'utf-8')
        self.get_widget('chat_scrolled_window').add(webkit_view)

    def connect_signals(self):
        self.connect_signal(self.widget, 'delete-event', self.application.quit)
        self.connect_signal('quit_menu_item', 'activate', self.application.quit)
        self.connect_signal('preferences_button', 'clicked', self.on_preferences_event)
        self.connect_signal('preferences_menu_item', 'activate', self.on_preferences_event)
        self.connect_signal('about_menu_item', 'activate', self.on_about_event)

    def on_preferences_event(self, widget):
        PreferencesDialog(self.application).show()

    def on_about_event(self, widget):
        AboutDialog(self.application).show()
