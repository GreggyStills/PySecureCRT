#$language = "Python"
#$interface = "1.0"
"""
SecureCRT script to open a webbrowser to a local port which is proxied to a
remote host through this SSH session.
"""
import webbrowser

# Detect if this script is being run by SecureCRT Python.  If not, then try to load my
# hacky mock SecureCRT "API", so that my PyCharm/iPython/IDE can help me w/ docstrings
# and auto-complete (because VanDyke's API doc kinda sucks).
try:
    assert "crt" not in globals()
    from fake_scrt import SecureCRT
    crt = SecureCRT()
except (AssertionError, ImportError):
    pass


tab = crt.GetActiveTab()
# get SSH local proxy port from tab caption
# (should have been set there by connect.py)
l_lport = tab.Caption.split()[-1]

webbrowser.open("http://127.0.0.1:{}".format(l_lport))
