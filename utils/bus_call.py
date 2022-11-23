import gi
import sys 
gi.require_version('Gst','1.0')
from gi.repository import Gst 
def bus_call(bus,message,loop):
    g = message.type
    if g == Gst.MessageType.EOS:
        sys.stdout.write("End of Stream\n")
        loop.quit()
    elif g== Gst.MessageType.WARNING:
        err, debug = message.parse_warning()
        sys.stdout.write("Warning: %s: %s\n" % (err,debug))
    elif g== Gst.MessageType.ERROR:
        err, debug = message.parse_error()
        sys.stdout.write("Warning: %s: %s\n" % (err,debug))
    return True

        