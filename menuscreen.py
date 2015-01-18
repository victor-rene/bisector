#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Menu screen. Access to the game and scores screen.
"""

from kivy.core.audio import SoundLoader
from kivy.graphics import Rectangle
from kivy.uix.screenmanager import Screen

from katana import Katana
from menubutton import MenuButton
from stickman import StickMan

__author__ = "Victor RENÉ"
__copyright__ = "Copyright 2015, bisector"
__credits__ = ["Kivy Team"]
__license__ = "MIT"
__version__ = "0.1"
__maintainer__ = "Victor RENÉ"
__email__ = "victor-rene@outlook.com"
__status__ = "Production"


class MenuScreen(Screen):
    
    def __init__(self, root_widget, **kwargs):
        super(MenuScreen, self).__init__(**kwargs)
        with self.canvas:
            self.rect = Rectangle(source='img/menu-background2.png')
        self.bind(pos=self._update_rect, size=self._update_rect)
        
        sm1 = StickMan(pos_hint={'center_x': .8, 'center_y': .4},
            size_hint=(5/16.,.4))
        self.add_widget(sm1)
        sm1.flex()
        
        sm2 = StickMan(pos_hint={'center_x': .2, 'center_y': .4},
            size_hint=(5/16.,.4))
        self.add_widget(sm2)
        sm2.flex()
        
        self.btn_play = MenuButton(background_normal='img/button-play-up.png',
            background_down='img/button-play-down.png',
            size_hint=(.3, .15),
            pos_hint={'center_x': .5, 'center_y': .3})
        self.btn_play.bind(on_release=root_widget.newgame)
        self.add_widget(self.btn_play)
        
        self.btn_play = MenuButton(background_normal='img/button-scores-up.png',
            background_down='img/button-scores-down.png',
            size_hint=(.3, .15),
            pos_hint={'center_x': .5, 'center_y': .15})
        self.btn_play.bind(on_release=root_widget.show_scores)
        self.add_widget(self.btn_play)
        
        ktn = Katana(pos_hint={'center_x': .5, 'center_y': .6},
            size_hint=(.1, .8))
        ktn.angle = 90
        self.add_widget(ktn)
        
        snd = SoundLoader.load('music/comp-04-bis.ogg')
        if snd:
            snd.loop = True
            snd.play()
            
    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
