__version__ = '0.1'

from gi.repository import Gio, Gtk
from firepit.ui.window import MainWindow

class Application(Gtk.Application):
    def __init__(self):
        super(Application, self).__init__(
                application_id='org.sleekware.firepit',
                flags=Gio.ApplicationFlags.FLAGS_NONE)

        self.settings = Settings()

        self.connect('activate', self.on_activate)

    def run(self, arguments=None):
        super(Application, self).run(arguments)

    def on_activate(self, application):
        main_window = MainWindow(self)
        main_window.show()

        self.add_window(main_window.widget)

    def quit(self, *args):
        for window in self.get_windows():
            self.remove_window(window)

class Settings(Gio.Settings):
    def __init__(self):
        super(Settings, self).__init__('org.sleekware.firepit')
