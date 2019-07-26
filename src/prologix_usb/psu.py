from .common import PrologixSerialDecive
from typing import Optional
from abc import ABC, abstractmethod

class PSUSettings(dict):
    pass

DEFAULT_SETTINGS = PSUSettings()

class PSU(PrologixSerialDecive):
    def __init__(self, output_settings:PSUSettings=DEFAULT_SETTINGS, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._settings = output_settings
        self._id:str = self.get_id()
        self._channels = None

    def self_test(self) -> Optional[bool]:
        self.send_cmd('*TST?')
        # self test takes ___ many seconds, maybe sleep
        resp = int(self.read_response())
        if resp == 0:
            return True
        elif resp == -300:
            return False
        else:
            return None

    def sel_channel(self, channel:int):
        self.send_cmd('INST:NSEL {}'.format(channel))

    def update_settings(self,settings:PSUSettings):
        pass

    def set_output_enable(self,output_state:bool):
        self.send_cmd('OUTP {}'.format('ON' if output_state else 'OFF'))

    def set_voltage(self,channel:int,voltage:float):
        self.sel_channel(channel)
        self.send_cmd('SOUR:VOLT {}'.format(voltage))
    
    def set_current(self,channel:int,current:float):
        self.sel_channel(channel)
        self.send_cmd('SOUR:CURR {}'.format(current))

    def disable_all(self):
        self.set_output_enable(False)    
