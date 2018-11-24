# Open multiple instances of the same window
## Rationale
May be you want to have a "add" window for each type of Note, so you
won't have to regularly change note type.

Maybe you want to see simultaneusly the result of multiple searchs in
the browser.

May be you started a note. Then you have an idea for another note, but
don't want to submit the first note already. Thus you need to note
adders.

May be you want to see multiple time the about window (even if I must
confess I don't understand why you would want that). Anyway, this
add-on allow you to open most windows multiple time.
## Usage
To open a new window of a kind, just do what you need to open the
window.

If you want that some kind of window is opened only once, read section
"configuration".


## Configuration
In the map "multiple", add «, "windowName" : false», where windowName
is the name of the window you want to see open only once.

## Warnings
It may be the case that when you change the configuration about a
window which is already opened, you'll see a message error. It should
not create real trouble. Please report otherwise.

All opened «AddCards» must have the same note type. This is a big
restriction, which I hope to be able to solve.

## Internal
This add-on redefined aqt.__init__'s class DialogManager. It should
behave similarly, even if add-on changed it, at least for windows
which should be open a single time.

This may only works with windows which uses aqt's dialog manager. In
general, they are big windows, whose have no direct effect on the
window calling it. I.e. it won't work with a prompt asking you to
confirm/cancel something, or to say «ok». It should work with the
browser.


## Advice
The most standard windows name are:
* AddCards
* Browser
* EditCurrent
* DeckStats
* About
* Preferences
## TODO
* Allowing multiple edit windows containing different content.
* Allowing distinct note type in different add windows.

## Version 2.0
Please use add-on [Multiple 'Add' and 'Browser' Windows, with addon
numbers](https://ankiweb.net/shared/info/969743069) instead.
## Links, licence and credits

Key         |Value
------------|-------------------------------------------------------------------
Copyright   | Arthur Milchior <arthur@milchior.fr>
Based on    | Anki code by Damien Elmes <anki@ichi2.net>
Requested by| ijgnord on [reddit](https://www.reddit.com/r/Anki/comments/9z4fuv/do_you_want_miss_some_addons_you_loved_in_anki_20/ea6f2lw/)
Original idea by | Webventure, addon number [969743069](https://ankiweb.net/shared/info/969743069)
License     | GNU AGPL, version 3 or later; http://www.gnu.org/licenses/agpl.html
Source in   | https://github.com/Arthur-Milchior/anki-Multiple-Windows
Addon number| [354407385](https://ankiweb.net/shared/info/354407385)

