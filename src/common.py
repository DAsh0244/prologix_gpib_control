
import atexit
from enum import Enum
from typing import Optional
from abc import ABC, abstractmethod

import serial

__ver_info = (0,1,0)
__version__ = '.'.join(map(str, __ver_info))


BAUD = 9600
TIMEOUT = 1.0

class DeviceBase(ABC):
    ENCODING = 'ascii'
    EOL = '\n'
        
    @abstractmethod
    def send_cmd(self, cmd:str):
        pass

    @abstractmethod
    def read_response(self):
        pass

class PrologixSerialDecive(DeviceBase):
    def __init__(self, port:str, addr:int, baud:int=BAUD, timeout:float=TIMEOUT,
                 buf_clear:bool=True, init_prologix:bool=False, enforce_addr:bool=False, debug:bool=False):
        self._ser = serial.Serial(port,baud,timeout=timeout)
        atexit.register(self._ser.close)
        self._addr = addr
        self._debug = debug
        self._enforce_addr = enforce_addr
        if init_prologix:
            self.send_cmd('++mode 1')
            self.send_cmd('++auto 1')
            self.send_cmd('++addr {}'.format(self._addr))
            self.send_cmd('++ver')
            # resp = self._ser.readline().strip().decode(self.ENCODING)
            resp = self.read_response()
            if 'Prologix GPIB-USB Controller' not in resp:
                raise ValueError('Unable to verify interface is a Prologix GPIB-USB Controller')
        if buf_clear:
            self.clear_buffer()

    def get_id(self):
        self.send_cmd('*idn?')
        resp = self.read_response()
        return resp

    def prologix_set_mode(self,mode):
        self.send_cmd('++mode {}'.format(mode))
    
    def send_cmd(self, cmd):
        if self._enforce_addr:
            self.send_cmd('++addr {}'.format(self._addr))
        if self._debug:
            print((cmd.strip()+self.EOL).encode(self.ENCODING))
        self._ser.write((cmd.strip()+self.EOL).encode(self.ENCODING))
    
    def read_response(self):
        data = self._ser.readline().strip().decode(self.ENCODING)
        return data

    def clear_buffer(self):
        tmp = self._ser.readline()
        while tmp != b'':
            tmp = self._ser.readline()

