__version__ = '0.1'

from gi.repository import Gio, Gtk
from firepit.ui.window import MainWindow

class Application(Gtk.Application):
    def __init__(self):
        super(Application, self).__init__(
                application_id='org.sleekware.FirePit',
                flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.connect('activate', self.on_activate)

    def on_activate(self, application):
        self.builder = Gtk.Builder()
        self.builder.add_from_file('resources/ui.glade')

        main_window = MainWindow(self)
        main_window.show()

        self.add_window(main_window.widget)

    def quit(self, *args):
        for window in self.get_windows():
            self.remove_window(window)
