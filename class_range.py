# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 22:30:29 2020

@author: D-pc
"""

class Range(object):
    '''range class '''
    def __init__(self, start, stop = None, step=1):
        ''' Initialize args'''
        if step == 0:
            raise ValueError('step cannot be 0')
        if stop is None:
            start, stop = 0, start
        self._length = max(0, (stop-start+step-1)//step)
        self._start = start
        self._step = step
    
    def __len__(self):
        '''Return number of entries in the range '''
        return self._length
    
    def __getitem__(self, k):
        '''Return entry at index k '''
        if k < 0:
            k += self._length
        if not 0 <= k < self._length:
            raise IndexError('index out of range')
        return self._start + k * self._step
    
    
    