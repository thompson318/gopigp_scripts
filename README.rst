Some basic scripts for the gopigo
https://www.dexterindustries.com/raspberry-pi-robots/

Commands to stream from the camera with gstreamer

On the pi:
gst-launch-1.0 rpicamsrc bitrate = 1000000 ! video/x-raw, width=640, height=480, framerate=30/1 ! videoconvert ! jpegenc ! rtpjpegpay ! udpsink host=10.124.1.170 port=5200

On the host:
gst-launch-1.0 -v udpsrc port=5200 ! application/x-rtp, media=video, clock-rate=90000, payload=96 ! rtpjpegdepay ! jpegdec ! videoconvert ! autovideosink

