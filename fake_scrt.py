"""
A skeleton/mock-up of the SecureCRT API, so you can write SecureCRT Python script
logic in an IDE, without having to actually install SecureCRT.

How to use:
1. copy to the directory w/ your SecureCRT scripts
2. In your scripts that make 'crt' calls, do this at the top, just after imports:

# load fake SecureCRT API when not actually running in SecureCRT
if "crt" not in globals():
    from fake_scrt import SecureCRT
    crt = SecureCRT()

"""
import os
import random
import time


class Container(object):
    """Just a dummy container class."""
    def __init__(self):
        pass


class SessionConfig(object):
    def __init__(self):
        self._options = dict()

    def ConnectInTab(self):
        return Tab()

    def GetOption(self, opt_name):
        """Gets the value of the specified option."""
        return self._options.get(opt_name, '')

    def Save(self):
        return True

    def SetOption(self, opt_name, opt_value):
        option = {opt_name, opt_value}
        self._options.update(option)
        return option


class Screen:
    """The Screen object provides access to SecureCRT's terminal screen."""
    MatchIndex = 1
    Selection = "Selection"
    Synchronous = True
    #
    Columns = 80
    Rows = 24
    CurrentColumn = 1
    CurrentRow = 1
    #
    _ignorecase = False

    def __init__(self):
        pass

    def Clear(self):
        msg = "Screen cleared."
        print msg
        return msg

    def Get(self, row1, col1, row2, col2):
        """Returns a string of characters read for a portion of the screen. Returns a string containing
        the characters on the screen rectangle defined by the numeric values row1,col1 (upper-left)
        and row2,col2 (lower-right)."""
        msg = "Got text within coordinates: {} {} {} {}".format(row1, col1, row2, col2)
        print msg
        return msg

    def Get2(self, row1, col1, row2, col2):
        """Returns the characters on each row requested with a \n, so the rows can be split by looking
        for \n. This allows the rows to be different lengths as required by the contents of the rows."""
        msg = "Got text within coordinates: {} {} {} {}".format(row1, col1, row2, col2)
        print msg
        return msg

    def IgnoreCase(self, boolean):
        """Provides a global method to set case insensitivity. In addition, case insensitivity can be
        set per-function as described below in the WaitForStrings, WaitForString, and ReadString methods."""
        self._ignorecase = boolean

    def Print(self):
        """Prints the screen. If no printer is defined on your machine, an error will be returned."""
        msg = "Print Screen."
        print msg
        return msg

    def ReadString(self, string_array=(), timeout_seconds=0, case_insensitive=False):
        """Captures data as it is received from the remote.

        Args:
            string_array (list): list of strings
            timeout_seconds (int): how long to wait
            case_insensitive (bool): Enable case-insensitive match
        """
        msg = "\n".join([
            "ReadString",
            "strings: {}".format(string_array),
            "timeout: {}".format(timeout_seconds),
            "case_insensitive: {}".format(case_insensitive)])
        print msg
        return msg

    def Send(self, string="Send String", send_to_screen_only=False):
        """Sends a string of characters. Attempting to send a string while no connection is open returns an error.

        Args:
            string (str): Text to send
            send_to_screen_only (bool): If True, send only to local screen, and not to remote.
        """
        msg = "\n".join([
            "Send",
            "string: {}".format(string),
            "send_to_screen_only: {}\n".format(send_to_screen_only)])
        print msg
        return msg

    def SendKeys(self):
        """Sends key strokes to the active window."""
        raise Exception("Not currently supported in Python.")

    def SendSpecial(self, string):
        """Sends a built-in SecureCRT command. SendSpecial can send any of the Menu, Telnet, and
        VT functions listed on the Map Selected Key dialog (accessed by selecting a key in the Keymap
        Editor and clicking on the Map Selected Key... button).
        e.g. "MENU_PASTE", "TN_BREAK", "VT_PF1" """
        msg = "SendSpecial: {}".format(string)
        print msg
        return msg

    def WaitForCursor(self, timeout=0):
        """Wait for the cursor to change position. An error will be returned if there is no connection open.

        Args:
            timeout (int): number of seconds to wait for the change.
        """
        if timeout > 0:
            return True
        return False

    def WaitForKey(self, timeout):
        """Wait for a keypress event. An error will be returned if there is no connection open.

        Args:
            timeout (int): number of seconds to wait for a key event
        """
        if timeout > 0:
            return True
        return False

    def WaitForString(self, string="String to wait for", timeout=0, case_insensitive=False):
        """Wait for a string. An error will be returned if there is no connection open.

        Args:
            string (str): string to wait for
            timeout (int): number of seconds to wait for a string
            case_insensitive (bool): Enable case-insensitive match
        """
        if timeout > 0:
            return True
        return False

    def WaitForStrings(self, string_array=(), timeout=0, case_insensitive=False):
        """Wait for one of several strings to appear in the input. If any are seen, returns
        the list index of the string seen (first string is index=1). If none are seen, returns 0.
        An error will be returned if there is no connection open.

        Args:
            string_array (list): A list of strings to wait for
            timeout (int): number of seconds to wait for a string
            case_insensitive (bool): Enable case-insensitive match
        """
        if timeout > 0:
            return 1
        return 0


class Session:
    """The Session object provides access to the state and properties that exist for the current
    connection or session."""
    LocalAddress = "127.0.0.1"
    LogFileName = "logfile"
    Path = "."

    def __init__(self):
        self._last_error = 1
        self._status_text = "Status text"
        self.Connected = True
        self.Logging = False
        self.RemoteAddress = "1.1.1.1"
        self.RemotePort = 22

    Config = SessionConfig()

    def Connect(self, arguments="command line arguments", wait_for_auth=True, suppress_popups=False):
        """Connects to a session. e.g.
        Connect("/SSH2 /PASSWORD password username@hostname")

        Args:
            arguments (str): arguments to pass to connect, as if running SecureCRT from the command line.
            wait_for_auth (bool): Whether to wait for authentication before proceeding.
            suppress_popups (bool): Whether to suppress popups.
        """
        self._last_error = 0
        return Tab()

    ConnectInTab = Connect  # essentially same method

    def Disconnect(self):
        """Disconnects the current session."""
        self.Connected = False

    def Log(self, log_boolean):
        """Enables or disables logging.  True=enabled, False=disabled"""
        self.Logging = log_boolean

    def LogUsingSessionOptions(self):
        """Turns on logging using the logging options for the current session. If the session is an
        ad hoc session, the Default session's logging options will be used."""
        return

    def Print(self, print_boolean):
        """Starts or stops autoprint. Starts or stops autoprint depending on the Boolean start parameter."""
        return print_boolean

    def SetStatusText(self, status_text):
        """Allows you to set the text within the status bar for a specific session."""
        self._status_text = status_text
        return status_text

    def Send(self, text):
        msg = "Sent to remote: {}".format(text)
        print msg
        return msg

    def WaitForStrings(self, list_of_strings, timeout):
        saw = random.choice(list_of_strings)
        index = list_of_strings.index(saw)
        if timeout < 1000:
            print "Prompt seen: {}".format(saw)
            return index + 1  # SecureCRT starts list index at 1
        else:
            print "Timed out waiting for prompt."
            return 0  # SecureCRT returns 0 when it times out


class Tab(Session):
    Caption = "Tab Caption"
    Index = 1
    Screen = Screen()
    Session = Session()

    def Activate(self):
        """Brings the tab or tiled session window referenced by object to the foreground."""
        return True

    def Clone(self):
        """Returns a reference to a tab object cloned from the specified object tab reference."""
        return self

    def Close(self):
        """Closes the tab or tiled session window referenced by object."""
        return True

    def ConnectSftp(self):
        """Creates an SFTP tab based on this tab. When in tiled mode, creates an SFTP session
        window based on this tiled session."""
        return self


class SecureCRT(Container):
    """Top-level object. Provides access to all of SecureCRT's properties and methods.
    When running a Python script in SecureCRT, this is accessed through a global variable named 'crt'."""
    ActivePrinter = "ActivePrinter"

    #####
    @staticmethod
    def ClearLastError():
        """Resets the response from GetLastError and GetLastErrorMessage to ERROR_SUCCESS
        and 'The operation completed successfully.' """
        return

    @staticmethod
    def GetActiveTab():
        """Returns the Tab object associated with the tab or tiled session window
        that is currently selected in the GUI."""
        return Session()

    @staticmethod
    def GetScriptTab():
        """Returns the tab or tiled session window from which the script was started."""
        return Session()

    @staticmethod
    def GetLastError():
        """Returns the error code of the script exception that most recently happened."""
        return "ERROR_SUCCESS"

    @staticmethod
    def GetLastErrorMessage():
        """Returns the error text of the script exception that most recently happened."""
        return "The operation completed successfully."

    @staticmethod
    def GetTab(tab_index):
        """Returns the tab object of the specified index.
        This does not bring the tab or tiled session window to the foreground.
        When sessions are tabbed, the index for each tab object matches its position in the tab bar.
        When sessions are tiled, the indexes of the tab objects may not match the indexes when tabbed,
        but will remain consistent while the sessions are tiled."""
        return Session()

    @staticmethod
    def GetTabCount():
        """Returns the number of tabs or tiled session windows (connected or not) that exist in
        the current SecureCRT window.  Return value will always be greater than 0 (zero)."""
        return 1

    @staticmethod
    def OpenSessionConfiguration(session_path):
        """Loads the configuration for the specified session.
        SessionPath is a string parameter that is the relative path of the session.
        Returns a Config object. If SessionPath is not specified, the Default session's configuration
        object is returned. To access the session configuration associated with an active connection,
        use crt.Session.Config or objTab.Session.Config."""
        return True

    @staticmethod
    def Quit():
        """Causes SecureCRT to exit."""
        raise SystemExit("Quitting!")

    @staticmethod
    def Sleep(sleep_milliseconds):
        """Specifies the time (in milliseconds) to pause the script's execution."""
        time.sleep(sleep_milliseconds/1000.0)


    ####
    class Arguments(Container):
        """The Arguments object allows scripts to access arguments that are passed to the script
        by one or more SecureCRT /ARG command-line options.
        """
        Count = 0  # number of arguments passed

        @staticmethod
        def GetArg(arg_index):
            """Returns the argument data associated with each /ARG command-line option passed to SecureCRT."""
            return str(arg_index)

    class Clipboard(Container):
        """The Clipboard object provides access to the application's clipboard.
        Possible formats on Windows are: CF_TEXT, CF_OEMTEXT, CF_UNICODETEXT, and VDS_TEXT.
        Possible formats on Mac are: CF_UNICODETEXT and VDS_TEXT."""
        DEFAULTFORMAT = "CF_UNICODETEXT"
        Format = "CF_UNICODETEXT"
        Text = "Clipboard text"

    class CommandWindow(Container):
        """Provides access to the Command window."""
        SendCharactersImmediately = True
        SendToAllSessions = False
        Text = "Command Window Text"
        Visible = True

        def Send(self):
            """Sends the current text in the Command window to the remote machine."""
            msg = "crt.CommandWindow.Send: {}".format(self.Text)
            print msg
            return msg

    class Dialog(Container):

        @staticmethod
        def FileOpenDialog(*args):
            """Display a file browse dialog from which the user can select a single file.
            If the defaultFilename parameter is simply a filename (no path provided), the file dialog browser
            will open in current working directory.  If the defaultFilename parameter specifies an absolute path
            to a file, the file dialog browser will open in the parent directory of the file. The filename
            filter is in the following format:
            <Name of Filter> (*.<extension>)|*.<extension>||
            e.g. 'Text Files (*.txt)|*.txt||' OR  'Text Files (*.txt)|*.txt|Log File (*.log)|*.log||' """
            msg = "crt.Dialog.FileOpenDialog: {}".format(" ".join(*args))
            print msg
            return msg

        @staticmethod
        def MessageBox(message, title=None, buttons=None):
            """The MessageBox function displays a message string to the user. The optional title string sets
            the title or caption of the MessageBox. The buttons that appear on the MessageBox can be configured by
            passing a combination of numeric values in the optional 'buttons' parameter. By default MessageBox will
            display the message string with an OK button. However, many possibilities exist for displaying message
            boxes with different icons, and buttons. The MessageBox function returns a numeric value that can be
            used to identify which button was clicked.
            e.g.:
            crt.Dialog.MessageBox("Login Failed, Retry?", "Error", ICON_QUESTION | BUTTON_YESNO | DEFBUTTON2 )"""
            return 1

        @staticmethod
        def Prompt(message, title=None, default="enter stuff: ", isPassword=False):
            """The Prompt function displays a simple dialog that has message and an edit field for the user to
            enter a string. The message parameter is an informational string displayed in the prompt dialog.
            Optionally the title of the prompt dialog may be set by passing a title string. By default the edit
            field is empty, but the initial contents of the edit field may be set with the optional default string.
            Finally, if the text entered in the edit field is to be obscured as it is entered (such as when entering
            a password) then the Boolean isPassword field should be set to True.  If the user clicks OK, Prompt
            returns the entered string; whereas, if the user clicks Cancel, Prompt returns an empty string."""
            return message

    class FileTransferObject(Container):
        """The FileTransfer object provides methods for performing file transfers initiated by scripts.
        SecureCRT's FileTransfer object is accessed through the top-level object's FileTransfer property.
        The FileTransfer object is not supported with with sessions that use TN3270 emulation."""
        DownloadFolder = "Downloads"
        ZmodemUploadAscii = False
        _upload_list = []

        def AddToUploadList(self, filename):
            """AddToUploadList places the specified file on a list of files that will be uploaded during the
            next Y/Zmodem or Kermit upload. Once one or more files have been added to the upload list, a
            Y/Zmodem or Kermit upload can be initiated by the script sending the appropriate command to the
            remote system."""
            self._upload_list.append(filename)
            return self._upload_list

        def ClearUploadList(self):
            """Clears the upload list."""
            self._upload_list = []
            return self._upload_list

        def ReceiveKermit(self):
            """Initiates file download via Kermit to download folder."""
            msg = "crt.FileTransferObject.ReceiveKermit To: {}".format(self.DownloadFolder)
            print msg
            return msg

        def ReceiveXmodem(self):
            """Initiates file download via Xmodem to download folder."""
            msg = "crt.FileTransferObject.ReceiveXmodem To: {}".format(self.DownloadFolder)
            print msg
            return msg

        def ReceiveYmodem(self):
            """Initiates file download via Ymodem to download folder."""
            msg = "crt.FileTransferObject.ReceiveYmodem To: {}".format(self.DownloadFolder)
            print msg
            return msg

        def SendKermit(self):
            """Initiates Kermit upload of files from upload list."""
            for f in self._upload_list:
                print "crt.FileTransferObject.SendKermit sending: {}".format(f)

        def SendXmodem(self):
            """Initiates Xmodem upload of files from upload list."""
            for f in self._upload_list:
                print "crt.FileTransferObject.SendXmodem sending: {}".format(f)

        def SendYmodem(self):
            """Initiates Ymodem upload of files from upload list."""
            for f in self._upload_list:
                print "crt.FileTransferObject.SendYmodem sending: {}".format(f)

    class GetScriptTab(Container):
        @staticmethod
        def Activate():
            msg = "crt.GetScriptTab"
            print msg
            return msg

        Session = Session()

    Screen = Screen()

    class Window(Container):
        Active = True
        Caption = "Window Caption"
        _states = {0: "hidden", 1: "visible (normal)", 2: "minimized", 3: "maximized"}
        State = 1

        def Activate(self):
            """Gives focus to the SecureCRT window, bringing the window to the top of the desktop."""
            return True

        def Show(self, state):
            """Shows, hides, minimizes, or maximizes SecureCRT's application window."""
            assert state in self._states, "You tried: {}.\nValid numbers: {}".format(state, self._states)
            self.State = state
            return "State set ({}: {})".format(state, self._states[state])
