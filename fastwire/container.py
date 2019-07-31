# -*- coding: utf-8 -*-
"""
Created on Wed Jul 31 12:59:51 2019

@author: Reuben
"""

class Container(dict):
    ''' A dictionary-like collection of Signal instances '''
    
    def __init__(self, signal_cls):
        self._signal_cls = signal_cls
    
    def new(self, name=None, doc=None, **kwargs):
        ''' Get a new Signal instance 
        
        Args:
            name (str): A name of the wire [optional]
            doc (str): A documentation string for the wire [optional]
        '''
        name = len(self) if name is None else name
        s = self._signal_cls(name=name, doc=doc, **kwargs)
        self[name] = s
        return s
    
    def mute_all(self):
        ''' Mute all signals in the container '''
        for key, signal in self.items():
            signal.mute()

    def unmute_all(self):
        ''' Unmute all signals in the container '''
        for key, signal in self.items():
            signal.unmute()

    def reset_all(self):
        ''' Reset all wires in the contain '''
        for key, signal in self.items():
            signal.reset()
    
    def __getitem__(self, name):
        ''' Get or create a Signal instance 
        
        Args:
            key: The name of the signal
        '''
        if name in self:
            return super().__getitem__(name)
        else:
            s = s = self._signal_cls(name=name)
            super().__setitem__(name, s)
            return s
            