class CampfireUser(object):
    def __init__(self, backend):
        self.user = backend

    def get_data(self):
        return self.user.get_data()
