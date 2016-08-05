#!/bin/bash
############################################################################
#  Copyright (C) 2015 IEEE Student Branch of Granada                       #
#                                                                          #
#  This program is free software: you can redistribute it and/or modcify   #
#  it under the terms of the GNU General Public License as published by    #
#  the Free Software Foundation, either version 2 of the License, or       #
#  (at your option) any later version.                                     #
#                                                                          #
#  This program is distributed in the hope that it will be useful,         #
#  but WITHOUT ANY WARRANTY; without even the implied warranty of          #
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the            #
#  GNU General Public License for more details.                            #
#                                                                          #
#  You should have received a copy of the GNU General Public License       #
#  along with this program. If not, see <http://www.gnu.org/licenses/>.    #
############################################################################
# Reference: https://www.timdejong.nl/blog/use-webcam-two-applications-under-linux-simultaneously-using-v4l2loopback

# You need to install v4l2loopback, in some distribution is in the default repos
# For others like Fedora install from repo:

# git submodule update --init --recursive
# cd v4l2loopback
# make && sudo make install
# cd ..

# Create two virtual video devices
sudo modprobe v4l2loopback devices=2

# If you are seeing your video flipped or rotate, could be fix with this:
export LD_PRELOAD=/usr/lib64/libv4l/v4l1compat.so

# Copy original video (/dev/video0) to the new two virtual videos (/dev/video1 and /dev/video2)
ffmpeg -f video4linux2 -s 1280x1024 -i /dev/video0 -codec copy -f v4l2 /dev/video1 -codec copy -f v4l2 /dev/video2
