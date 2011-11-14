from abc import ABCMeta
from gi.repository import Gtk

class Window(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, glade_file, window_name, application):
        """
        Constructs a new Window, which is backed by the GtkWidget defined in Glade,
        named 'window_name'.
        """
        self.window_name = window_name
        self.application = application

        self.builder = Gtk.Builder()
        self.builder.add_from_file(glade_file)

        self.prepare_ui()
        self.connect_signals()

    @property
    def widget(self):
        """
        Returns the widget that represents this window.
        """
        return self.get_widget(self.window_name)

    def get_widget(self, name):
        """
        Gets a widget by name from the GtkBuilder. Raises a KeyError if the widget
        was not found.
        """
        widget = self.builder.get_object(name)

        if not widget:
            raise KeyError('No widget named {} was found.'.format(name))

        return widget

    def resolve_widget(self, widget):
        """
        Returns the widget from glade if widget is a string, otherwise returns
        the widget unchanged.
        """
        return self.get_widget(widget) if type(widget) is str else widget

    def prepare_ui(self):
        """
        Allows implementing classes to create widgets, set properties, etc. during the
        __init__ process.
        """

    def connect_signal(self, widget, signal, callback):
        """
        Connects the callback to the specified signal on the widget provided. The 'widget'
        parameter can be either the string name of the widget to pull from the builder, or
        an instance of an already constructed widget.
        """
        return self.resolve_widget(widget).connect(signal, callback)

    def disconnect_signal(self, widget, handler_id):
        """
        Disconnects the signal handler_id from the specified widget.
        """
        self.resolve_widget(widget).disconnect(handler_id)

    def connect_signals(self):
        """
        Connects signals during the __init__() of this class.
        """

    def show(self):
        """
        Show the window.
        """
        self.widget.show_all()

class Dialog(Window):
    __metaclass__ = ABCMeta

    def __init__(self, glade_file, window_name, application):
        """
        Constructs a new Dialog instance.
        """
        super(Dialog, self).__init__(glade_file, window_name, application)

    def show(self):
        """
        Shows the dialog and executes the provided callback on the response.
        """
        response_id = self.widget.run()
        self.widget.destroy()
        return self.on_dialog_response(response_id)

    def on_dialog_response(self, response_id):
        """
        Handles the event where a dialog response was provided.
        """
