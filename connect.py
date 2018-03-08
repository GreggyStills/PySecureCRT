#$language = "Python"
#$interface = "1.0"
"""
SecureCRT script to establish an SSH connection, with a local SSH proxy listening on a random port.
"""
import subprocess
import shlex

# Detect if this script is being run by SecureCRT Python.  If not, then try to load my
# hacky mock SecureCRT "API", so that my PyCharm/iPython/IDE can help me w/ docstrings
# and auto-complete (because VanDyke's API doc kinda sucks).
try:
    assert "crt" not in globals()
    from fake_scrt import SecureCRT
    crt = SecureCRT()
except (AssertionError, ImportError):
    pass


def run_shell(cmd):
    """Run a shell command, and return the output."""
    output = subprocess.check_output(shlex.split(cmd), stderr=subprocess.STDOUT)
    return output


def main():
    l_lport = run_shell("python find_localport.py")
    crt.Screen.Synchronous = True
    hostname = crt.Dialog.Prompt("Enter Hostname:")
    # ssh_user = crt.Dialog.Prompt("Enter User:")
    # ssh_pw = crt.Dialog.Prompt("Enter Password:", isPassword=True)
    # l_lport = get_random_lport()
    cmdline_opts = [
        # "/S {}".format(session_name)  # name of SecureCRT session to use
        # "/T"  # open specified session (/S) in a separate tab
        "/SSH2",  # open the default session w/ SSH2 protocol
        "/LOCAL {}:127.0.0.1:80".format(l_lport),  # proxy <local port> to <remote host>:<remote port>
        # "/REMOTE {}:{}:{}".format(r_rport, r_lhost, r_lport),  # proxy <remote port> to <local host>:<local port>
        # "/I {}".format(ssh_key_file),  # use SSH private key file for authentication
        # "/L {}".format(ssh_user),  # SSH username
        # "/PASSWORD {}".format(ssh_pw),  # SSH password
        "/ACCEPTHOSTKEYS",  # auto-accept remote SSH host key
        # "/FORWARDX11PACKETS",  # enable X11 forawrding
    ]
    cmd = " ".join(cmdline_opts + [hostname])
    # crt.Dialog.MessageBox("\n".join(cmdline_opts))
    crt.Session.ConnectInTab(cmd)

    # save local proxy port in tab caption (seems like the best/only place to save per-session info)
    tab = crt.GetActiveTab()
    tab.Caption = "{} {}".format(hostname, l_lport)  # e.g. "myserver.example.com 53879"


main()
