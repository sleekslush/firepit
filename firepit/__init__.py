__version__ = '0.0.0.1'

from gi.repository import Gtk
from firepit.ui.window import MainWindow

class Application(object):
    def __init__(self, args):
        self.args = args
        self.builder = Gtk.Builder()
        self.builder.add_from_file('resources/ui.glade')

    def start(self):
        MainWindow(self).show()
        Gtk.main()

    def quit(self):
        # gracefully disconnect all open pyfire connections
        Gtk.main_quit()
