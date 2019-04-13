from __future__ import absolute_import, print_function, unicode_literals


class Store(object):

    def __init__(self, state=None, root_reducer=None):
        self.__state = state or {}
        self.root_reducer = root_reducer
        self.listeners = []

    def dispatch(self, action):
        new_state = self.root_reducer(self.state, action)
        if new_state != self.state:
            self.__state = new_state
            self.__notify()

    def __notify(self):
        for listener in self.listeners:
            listener()

    def subscribe(self, listener):
        self.listeners.append(listener)

    def get_state(self, action):                        # Added get_state function, I don't know if it works correctly
        print(self.root_reducer(self.state, action))
        return self.__state

    @property
    def state(self):
        return self.__state
