from firepit.ui import Dialog

class AboutDialog(Dialog):
    def __init__(self, application):
        super(AboutDialog, self).__init__('about_dialog', application)

class PreferencesDialog(Dialog):
    def __init__(self, application):
        super(PreferencesDialog, self).__init__('preferences_dialog', application)
