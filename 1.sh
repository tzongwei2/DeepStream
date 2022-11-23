#Make yolov4
cp -r /opt/nvidia/deepstream/deepstream/sources/project/DeepStream-Yolo/ /opt/nvidia/deepstream/deepstream/sources/yolo
cd /opt/nvidia/deepstream/deepstream/sources/yolo
CUDA_VER=11.7 make -C nvdsinfer_custom_impl_Yolo

#Python bindings
apt install python3-gi python3-dev python3-gst-1.0 python-gi-dev git python-dev \
python3 python3-pip python3.8-dev cmake g++ build-essential libglib2.0-dev \
libglib2.0-dev-bin libgstreamer1.0-dev libtool m4 autoconf automake libgirepository1.0-dev libcairo2-dev

cd /opt/nvidia/deepstream/deepstream-6.1/sources/
git clone https://github.com/NVIDIA-AI-IOT/deepstream_python_apps
cd deepstream_python_apps/
git submodule update --init
apt-get install -y apt-transport-https ca-certificates -y
update-ca-certificates

cd 3rdparty/gst-python/
./autogen.sh
make
make install

cd ../../bindings
mkdir build
cd build
cmake ..
make

pip3 install ./pyds-1.1.4-py3-none-linux_x86_64.whl
pip3 install matplotlib opencv-python numpy

# The following is how to run the DeepStream App. Refer to the txt file for more info 
#cd /opt/nvidia/deepstream/deepstream/sources/project  
#deepstream-app -c configs//yolov4/deepstream_yolo.txt -t

