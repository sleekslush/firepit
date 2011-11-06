from firepit import __version__
from firepit.ui import Window
from firepit.ui.dialog import AboutDialog, PreferencesDialog

class MainWindow(Window):
    def __init__(self, application):
        super(MainWindow, self).__init__('main_window', application)

    def connect_signals(self):
        self.connect_signal(self.widget, 'destroy', self.on_quit_event)
        self.connect_signal('quit_menu_item', 'activate', self.on_quit_event)
        self.connect_signal('preferences_button', 'clicked', self.on_preferences_event)
        self.connect_signal('preferences_menu_item', 'activate', self.on_preferences_event)
        self.connect_signal('about_menu_item', 'activate', self.on_about_event)

    def on_preferences_event(self, widget):
        PreferencesDialog(self.application).show()

    def on_about_event(self, widget):
        AboutDialog(self.application).show()

    def on_quit_event(self, *args, **kwargs):
        self.application.quit()
