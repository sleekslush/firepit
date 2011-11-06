from abc import ABCMeta
from gi.repository import Gtk

class Window(object):
    __metaclass__ = ABCMeta
    
    def __init__(self, window_name, application):
        self.window_name = window_name
        self.application = application
        self.init_ui()
        self.connect_signals()

    @property
    def builder(self):
        """
        Returns the builder object that has all the UI objects.
        """
        return self.application.builder

    @property
    def widget(self):
        """
        The GtkObject that represents this window.
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

    def connect_signal(self, widget, signal, callback):
        """
        Connects the callback to the specified signal on the widget provided. The 'widget'
        parameter can be either the string name of the widget to pull from the builder, or
        an instance of an already constructed widget.
        """
        if type(widget) is str:
            self.get_widget(widget).connect(signal, callback)
        else:
            widget.connect(signal, callback)

    def init_ui(self):
        """
        Called by the constructor, but meant to be overridden. Add custom widgets or attach
        values and special behavior in this method.
        """

    def connect_signals(self):
        """
        Called by the constructor, but meant to be overridden. Connect your signals in this
        method.
        """

    def show(self):
        """
        Show the window.
        """
        self.widget.show_all()

class Dialog(Window):
    __metaclass__ = ABCMeta

    def __init__(self, window_name, application):
        super(Dialog, self).__init__(window_name, application)

    def show(self):
        self.widget.run()
        self.widget.hide()
