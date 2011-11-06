from gi.repository import Gtk
from firepit.ui import Window
from firepit.ui.dialog import AboutDialog

class MainWindow(Window):
    def __init__(self, application):
        super(MainWindow, self).__init__('main_window', application)

    def connect_signals(self):
        self.connect_signal(self.widget, 'destroy', self.on_quit_event)
        self.connect_signal('quit_menu_item', 'activate', self.on_quit_event)
        self.connect_signal('about_menu_item', 'activate', self.on_about_activate)

    def on_about_activate(self, widget):
        AboutDialog(self.application).show()

    def on_quit_event(self, *args, **kwargs):
        Gtk.main_quit()
