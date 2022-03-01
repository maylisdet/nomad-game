import threading

from common import Profile

hard_coded_profile = Profile("Nick Name")

USER_PATH = "~/.local/share/nomad/profiles/"


def threaded(fn):
    def wrapper(*args, **kwargs):
        threading.Thread(target=fn, args=args, kwargs=kwargs).start()

    return wrapper
