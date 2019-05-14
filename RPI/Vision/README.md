## Security Camera
A raspberry pi home security solution (lol). No, it's just a project
to work on a few different things tied together into one neat little 
system. 

First there's the Raspberry Pi, with a camera attached and pointed out
a street facing window. Then, there's the client-side control software
``control.py``, which allows you a few different modes of interacting 
with the camera. 
* `python control.py snap_img` will take a still frame from on the Pi
and transfer it to local machine using SFTP.

* `python control.py snap_vid ` will take a video on the pi and transfer
to local machine using SFTP.

* `python control.py live` will show a live stream video from the pi

* `python control.py run` will take still images over time and save a 
timestamped timelapse of the resulting frames. 

*Using `show` as an additional argument will show the transferred files* 


### Video 
Precursor to what would become the basis of security 
camera functionality. 
## Stills 