
from gi.repository import Gst, GLib,GstApp
import gi 
gi.require_version("Gst","1.0")
from utils.bus_call import bus_call

_=GstApp

Gst.init(None)
main_loop = GLib.MainLoop()
input_file = 'videos/input2.mp4'
output_file = 'videos/output/output1.mp4'     
config_file = '/opt/nvidia/deepstream/deepstream-6.1/sources/project/models/yolov4/model_yolo4.txt'  #<your model config file>
tracker_file= '/opt/nvidia/deepstream/deepstream/lib/libnvds_nvmultiobjecttracker.so'

launch = " ".join([
"filesrc location=%s" % input_file,
"! parsebin",
"! nvv4l2decoder",
"! mux.sink_0",
"nvstreammux width=1280 height=720 batch-size=1 name=mux",
"! nvinfer name = pgie config-file-path=%s" % config_file,
"! nvtracker ll-lib-file =%s" % tracker_file,
"! nvstreamdemux name=demux",
"demux.src_0",
"! nvvideoconvert",
"! nvdsosd name =nvosd",
"! nvvideoconvert",
"! nvv4l2h264enc",
"! h264parse",
"! mp4mux",
"! filesink location=%s" % output_file
])

print(launch)
pipeline = Gst.parse_launch(launch)
assert pipeline
bus = pipeline.get_bus()
bus.add_signal_watch()
bus.connect ("message", bus_call, main_loop)
pipeline.set_state(Gst.State.PLAYING)
main_loop.run()
print("?")
#cleaning things up
pipeline.set_state(Gst.State.NULL)