import math
from random import randint

from kivy.animation import Animation
from kivy.graphics import Color, Line, Rectangle
from kivy.graphics.instructions import InstructionGroup
from kivy.uix.image import Image
from kivy.uix.label import Label
from kivy.uix.screenmanager import Screen
from kivy.uix.stacklayout import StackLayout

from foobar import FooBar
from katana import Katana
from slash import Slash


class GameScreen(Screen):
    
    def __init__(self, root_widget, **kwargs):
        super(GameScreen, self).__init__(**kwargs)
        self.root_widget = root_widget
        self._initialized = False
        
        with self.canvas.before:
            Color(0, 0, 0, 1)
            self.rect = Rectangle() #source='img/game-background.png')
            Color(1, 1, 1, 1)
        self.foobar = FooBar(size_hint=(.1, .8),
            pos_hint={'center_x': .5, 'center_y':.5})
        self.add_widget(self.foobar)
        self.bind(pos=self._update_rect, size=self._update_rect)

        self.katanas = StackLayout(size_hint=(.4, .2),
            pos_hint={'x':.05, 'y':.05}, orientation='tb-lr')
        self.add_widget(self.katanas)
        
        self.lbl_level = Image(source='img/level.png', size_hint=(.3, .1),
            pos_hint={'center_x': .2, 'center_y': .9})
        self.lbl_level_num = Image(source='img/1.png', size_hint=(.3, .1),
            pos_hint={'center_x': .2, 'center_y': .8})
        self.add_widget(self.lbl_level)
        self.add_widget(self.lbl_level_num)
        self.set_level(1)
        
        self.lbl_high = StackLayout(pos_hint={'center_x': .8, 'center_y': .8},
            orientation='tb-lr', size_hint=(.4, .2))
            # Label(text='%03d' % self.bound_high,
            # pos_hint={'center_x': .75, 'center_y': .8},
            # markup=True)
        self.lbl_low = StackLayout(pos_hint={'center_x': .8, 'center_y': .2},
            orientation='tb-lr', size_hint=(.4, .2))
            # Label(text='%03d' % self.bound_low,
            # pos_hint={'center_x': .75, 'center_y': .2},
            # markup=True)
        self.add_widget(self.lbl_high)
        self.add_widget(self.lbl_low)
        
        self.touches = [None for i in range(4)]
        self.slash = Slash()
        self.ig_cut = InstructionGroup()
        self.canvas.after.add(self.ig_cut)

    def set_level(self, value, score=0):
        self.level = value
        self.score = score
        self.lbl_level_num.source = 'img/%s.png' % self.level
        self.bound_high = 99 + (50 * (value - 1))
        self.bound_low = 0
        self.number = randint(self.bound_low, self.bound_high)
        self.ammo = 11 - self.level
        self.update_ammo()

    def update_ammo(self, *args):
        self.katanas.clear_widgets()
        for i in range(self.ammo):
            ktn = Katana(size_hint=(.1, 1.))
            ktn.angle = -45
            self.katanas.add_widget(ktn)
        
    def _update_rect(self, *args):
        self.rect.pos = self.pos
        self.rect.size = self.size
        if not self._initialized:
            self.update_ammo()
            self._initialized = True
            
    # def black_text(self, s):
        # return '[color=#000000]' + s + '[/color]'
            
    def on_touch_down(self, touch):
        self.touches = [touch.x, touch.y, None, None]
        
    def on_touch_move(self, touch):
        self.touches[2] = touch.x
        self.touches[3] = touch.y
        self.draw_cut()
        force = self.touches[2] - self.touches[0]
        force = max(min(force, 50), -50)
        self.foobar.force = force
        
    def get_cut_value(self):
        if not all(self.touches):
            return None
        if self.touches[0] < self.center_x and self.touches[2] < self.center_x:
            return None
        if self.touches[0] > self.center_x and self.touches[2] > self.center_x:
            return None
        h = self.touches[3] - self.touches[1]
        w = self.touches[2] - self.touches[0]
        if w and h:
            dist_cx = self.touches[0] - self.center_x
            rx = dist_cx / w
            raw = self.touches[1] + (rx * h)
            value = (raw - self.foobar.y) / self.foobar.height * \
                (self.bound_high - self.bound_low) + self.bound_low
            return value
        return None
        
    def dec_ammo(self):
        self.ammo -= 1
        n_ktn = len(self.katanas.children)
        ktn = self.katanas.children[0]
        anim1 = Animation(angle=315, size_hint=(.2, 2.), d=.5, t='linear')
        anim2 = Animation(angle=675, size_hint=(.05, .5), d=.5, t='linear')
        anim = anim1 + anim2
        anim.bind(on_complete=self.update_ammo)
        anim.start(ktn)
        if self.ammo == 0:
            self.game_over()
            
    def game_over(self):
        self.set_level(1)
        self.root_widget.current = 'score'
            
    def remove_slash(self, *args):
        self.ig_cut.clear()
        self.slash.opacity = 1.
        self.slash.reset_color()
        
    def update_bounds(self):
        self.lbl_high.clear_widgets()
        self.lbl_low.clear_widgets()
        for c in str(self.bound_high):
            self.lbl_high.add_widget(Image(source='img/' + c + '.png', size_hint_x=.2))
        for c in str(self.bound_low):
            self.lbl_low.add_widget(Image(source='img/' + c + '.png', size_hint_x=.2))
            
    def remove_cut_number(self, *args):
        self.remove_widget(args[1])
            
    def show_cut_number(self):
        sl = StackLayout(pos_hint={'center_x': .5, 'center_y': .5},
            orientation='tb-lr', size_hint=(.4, .2))
        for c in str(self.cut_value):
            sl.add_widget(Image(source='img/' + c + '.png', size_hint_x=.2))
        self.add_widget(sl)
        anim1 = Animation(x=sl.x+100, t='in_circ')
        anim2 = Animation(y=sl.y+100, t='out_circ')
        anim = anim1 & anim2
        anim.bind(on_complete=self.remove_cut_number)
        anim.start(sl)
            
    def rebound(self):
        anim = Animation(opacity=0.)
        anim.bind(on_complete=self.remove_slash)
        anim.start(self.slash)
        
        anim2 = Animation(force=0., t='out_bounce')
        anim2.start(self.foobar)
        
        self.show_cut_number()
        
        if self.cut_value > self.number:
            self.bound_high = self.cut_value
            self.dec_ammo()
        elif self.cut_value < self.number:
            self.bound_low = self.cut_value
            self.dec_ammo()
        else:
            self.set_level(self.level + 1)
        self.update_bounds() # implicit, always called
        
    def on_touch_up(self, touch):
        value = self.get_cut_value()
        if value is not None:
            self.cut_value = int(round(value))
            rdist = abs(self.cut_value - self.number) / 250.
            self.slash.temperature = max(min(rdist, 1.), 0.)
            self.rebound()
        
    def draw_cut(self):
        self.ig_cut.clear()
        y = self.touches[3] - self.touches[1]
        x = self.touches[2] - self.touches[0]
        self.slash.height = math.sqrt(x*x + y*y)
        self.slash.width = self.slash.height / 10.
        self.slash.pos = self.touches[0] - self.slash.width/2., self.touches[1]
        self.slash.angle = math.atan2(y, x) / math.pi * 180 - 90
        self.ig_cut.add(self.slash.canvas)
