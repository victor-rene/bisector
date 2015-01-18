#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Score screen. Score list and button to navigate to main menu.
"""

from kivy.core.audio import SoundLoader
from kivy.graphics import Rectangle
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.stacklayout import StackLayout

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


class ScoreScreen(Screen):
    
    def __init__(self, root_widget, **kwargs):
        super(ScoreScreen, self).__init__(**kwargs)
        with self.canvas:
            self.rect = Rectangle(source='img/score-background.png')
        self.bind(pos=self._update_rect, size=self._update_rect)
        
        self.sl_left = StackLayout(size_hint=(.3, .3),
            pos_hint={'center_x': .25, 'center_y': .3})
        self.sl_right = StackLayout(size_hint=(.3, .3),
            pos_hint={'center_x': .75, 'center_y': .3})
        self.add_widget(self.sl_left)
        self.add_widget(self.sl_right)
                
        self.btn_play = MenuButton(background_normal='img/button-menu-up.png',
            background_down='img/button-menu-down.png',
            size_hint=(.3, .2),
            pos_hint={'center_x': .5, 'center_y': .3})
        self.btn_play.bind(on_release=root_widget.menu)
        self.add_widget(self.btn_play)
        
        ktn = Katana(pos_hint={'center_x': .5, 'center_y': .5},
            size_hint=(.1, .8))
        ktn.angle = 90
        self.add_widget(ktn)
        
        self.load_scores()
        
    def black_text(self, text):
        return '[color=#000000]' + text + '[/color]'
        
    def load_scores(self):
        import os
        curr_dir = os.path.dirname(os.path.realpath(__file__))
        score_file = os.path.join(curr_dir, 'scores.txt')
        try:
            with open(score_file) as f:
                self.sl_left.clear_widgets()
                self.sl_right.clear_widgets()
                i = 0
                for line in f:
                    self.sl_left.add_widget(Label(text=self.black_text(line),
                        markup=True, size_hint=(1., .2)))
                    i += 1
                    if i == 5: break;
                for line in f:
                    self.sl_right.add_widget(Label(text=self.black_text(line),
                        markup=True, size_hint=(1., .2)))
                    i += 1
                    if i == 10: break;
        except:
            import traceback
            print traceback.format_exc()
            
    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
