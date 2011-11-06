from gi.repository import Gtk
from ui.window import MainWindow

__version__ = '0.0.0.1'

class Application(object):
    def __init__(self, args):
        self.args = args
        self.builder = Gtk.Builder()
        self.builder.add_from_file('resources/ui.glade')

    def start(self):
        MainWindow(self).show()
        Gtk.main()
