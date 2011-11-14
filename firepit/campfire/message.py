class CampfireMessage(object):
    def __init__(self, backend):
        self.message = backend

    def is_joining(self):
        return self.message.is_joining()

    def is_leaving(self):
        return self.message.is_leaving()

    def is_text(self):
        return self.message.is_text()
