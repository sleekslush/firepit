from smores.ui import Dialog

class AboutDialog(Dialog):
    def __init__(self, application):
        super(AboutDialog, self).__init__('about_dialog', application)
