bisector v 0.1
==============
are you a true samurai?

Done in two days, for the 2015 january monthly Kivy contest. I practiced new
techniques, like importing and modifying a mesh, with various animations, and
image rotations. I also included a self-made sound track.

<img src="https://github.com/victor-rene/bisector/raw/master/img/sc_02.png" style="height:100px">
<img src="https://github.com/victor-rene/bisector/raw/master/img/sc_03.png" style="height:100px">

Download
--------
![bisector.zip](https://github.com/victor-rene/bisector/raw/master/bin/bisector.zip "bisector.zip")

The idea
--------
One of the first tutorial I give to students has always been a bisection
application where the player must find a number between 0 and 999. It was done
in console mode, in C or Delphi (Pascal Object). The application also used
a color system to indicate how far off the cut was from the target number.

This particular app follows different rules, because after some playtests, it
became obvious that not much is going on, and you need some luck to score a 7,
with big numbers. Mostly likely you need 14 tries and that can be a bit too
much. Also, since we're in the touch device era, it made sense to propose
something more dynamic than typing a number on a console.

Therefore, I reduced the range to 0-99, and added levels. This also made the
scoring system really straightforward to implement. Just level * 10 + katanas
left. And about katanas... well katanas and samurais are cool. =P

Last word
---------
Try to enjoy the game (despite the weird music lol). It's gonna get published
on Google Playstore for Android devices very soon. Most likely I will need to
change the orientation of the window and account for different screen sizes...
and that's some more work left.
