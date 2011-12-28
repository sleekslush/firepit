class CampfireUser(object):
    def __init__(self, backend):
        self.user = backend

    @property
    def data(self):
        return self.user.get_data()
