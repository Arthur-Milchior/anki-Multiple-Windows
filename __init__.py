# -*- coding: utf-8 -*-
# Copyright: Arthur Milchior arthur@milchior.fr
# encoding: utf8
# License: GNU GPL, version 3 or later; http://www.gnu.org/copyleft/gpl.html
# Feel free to contribute to this code on https://github.com/Arthur-Milchior/anki-Multiple-Windows
import aqt
from aqt.browser import Browser


def debug(t):
    print(t)
    pass


def shouldBeMultiple(name):
    """Whether window name may have multiple copy.

    Ensure that ["multiple"] exsits in the configuration file. The default value being True.
    """
    debug(f"Calling shouldBeMultiple({name})")
    userOption = aqt.mw.addonManager.getConfig(__name__)
    if "multiple" not in userOption:
        userOption["multiple"] = {"default": True}
        aqt.mw.addonManager.writeConfig(__name__, userOption)
    multipleOption = userOption["multiple"]
    return multipleOption.get(name, multipleOption.get("default", True))


class DialogManagerMultiple(aqt.DialogManager):
    """Associating to a window name a pair (as a list...)

    The element associated to WindowName Is composed of:
    First element is the class to use to create the window WindowName.
    Second element is always None
    """
    # We inherits from aqt.DialogManager. Thus, if something is added to
    # its _dialogs, we have access to it.

    # Every method are redefined, they use the parent's method when it makes sens.

    def __init__(self, oldDialog=None):
        if oldDialog is not None:
            DialogManagerMultiple._dialogs = oldDialog._dialogs
        super().__init__()

    _openDialogs = dict()

    def open(self, name, *args):
        """Open a new window, with name and args. 

        Or reopen the window name, if it should be single in the
        config, and is already opened.
        """
        debug(f"Calling open({name},*args)")
        function = self.openMany if shouldBeMultiple(name) else super().open
        return function(name, *args)

    def openMany(self, name, *args):
        """Open a new window whose kind is name.

        keyword arguments:
        args -- values passed to the opener. 
        name -- the name of the window to open
        """
        debug(f"Calling openMany({name},{args})")
        (creator, _) = self._dialogs[name]
        instance = creator(*args)
        if name not in self._openDialogs:
            self._openDialogs[name] = set()
        self._openDialogs[name].add(instance)
        return instance

    def markClosed(self, name):
        """Window name is now considered as closed. 

        Don't check whether it is actually true."""
        debug(f"Calling markClosed({name})")
        self._openDialogs[name] = set()
        super().markClosed(name)

    def allClosed(self):
        """
        Whether all windows (except the main window) are marked as
        closed.
        """
        debug(f"Calling allClosed()")
        for name in self._openDialogs:
            if self._openDialogs[name]:
                return False
        return super().allClosed()

    def closeAll(self, onsuccess):
        """Close all windows (except the main one). Call onsuccess when it's done.

        Return True if some window needed closing.
        None otherwise

        Keyword arguments:
        onsuccess -- the function to call when the last window is closed.
        """
        debug(f"Calling closeAll({onsuccess})")

        def callback():
            """Call onsuccess if all window (except main) are closed."""
            if self.allClosed():
                onsuccess()
            else:
                # still waiting for others to close
                pass
        if self.allClosed():
            onsuccess()
            return

        # ask all windows to close and await a reply
        for (name, instances) in self._openDialogs.items():
            for instance in instances:
                if isValid(instance):
                    if getattr(instance, "silentlyClose", False):
                        instance.close()
                        callback()
                    else:
                        instance.closeWithCallback(callback)

        return super().closeAll(onsuccess)


aqt.DialogManager = DialogManagerMultiple
aqt.dialogs = DialogManagerMultiple(oldDialog=aqt.dialogs)
debug("Changing dialog manager")
