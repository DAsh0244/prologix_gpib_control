from common import PrologixSerialDecive
from typing import Optional
from abc import ABC, abstractmethod

class ScopeSettings(dict):
    pass

DEFAULT_SETTINGS = ScopeSettings()

class Scope(PrologixSerialDecive):
    def __init__(self, output_settings:ScopeSettings=DEFAULT_SETTINGS, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._settings = output_settings
        self._id:str = self.get_id()
        self._channels = None

    def self_test(self) -> bool:
        self.send_cmd('*TST?')
        # self test takes ___ many seconds, maybe sleep
        resp = int(self.read_response())
        if resp == 0:
            return True
        else:
            return False