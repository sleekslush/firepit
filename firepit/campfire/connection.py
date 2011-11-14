import pyfire
from firepit.campfire.room import CampfireRoom

class CampfireConnection(object):
    def __init__(self, subdomain, username, password, use_ssl=True):
        self.subdomain = subdomain
        self.username = username
        self.password = password
        self.use_ssl = use_ssl

    def connect(self):
        self.campfire = pyfire.Campfire(self.subdomain, self.username, self.password, self.use_ssl)

    def get_rooms(self, sort=False):
        for room in self.campfire.get_rooms():
            yield CampfireRoom(room)

    def get_room(self, id):
        return CampfireRoom(self.campfire.get_room(id))
