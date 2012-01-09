class CampfireMessage(object):
    def __init__(self, backend):
        self.message = backend

    @property
    def is_joining(self):
        return self.message.is_joining()

    @property
    def is_leaving(self):
        return self.message.is_leaving()

    @property
    def is_text(self):
        return self.message.is_text()
