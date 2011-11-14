from firepit.campfire.user import CampfireUser

class CampfireRoom(object):
    def __init__(self, backend):
        self.room = backend

    def join(self):
        return self.room.join()

    def leave(self):
        return self.room.leave()

    def recent_messages(self):
        for message in self.room.recent():
            yield CampfireMessage(message)

    def get_users(self):
        for user in self.room.get_users():
            yield CampfireUser(user)
