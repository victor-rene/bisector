#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
MenuButton. An animated button.
"""

from kivy.animation import Animation
from kivy.uix.button import Button

__author__ = "Victor RENÉ"
__copyright__ = "Copyright 2015, bisector"
__credits__ = ["Kivy Team"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Victor RENÉ"
__email__ = "victor-rene@outlook.com"
__status__ = "Production"


class MenuButton(Button):
    
    def __init__(self, **kwargs):
        super(MenuButton, self).__init__(**kwargs)
        self.anims = []
        
    def on_parent(self, *args):
        self.base_w = self.size_hint[0]
        self.base_h = self.size_hint[1]
        flat = Animation(size_hint=(self.base_w * 1.2, self.base_h * .9), d=.5, t='in_back')
        tall = Animation(size_hint=(self.base_w * .9, self.base_h * 1.2), d=.5, t='out_back')
        self.anims.append(flat)
        self.anims.append(tall)
        self._do_anim()
        
    def _do_anim(self, *args):
        anim = self.anims[0] + self.anims[1]
        anim.repeat = True
        anim.start(self)
