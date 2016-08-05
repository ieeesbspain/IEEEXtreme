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

# Arguments of fswebcam:
#   --device:    input device, edit as your needs.
#   --loop:      take a screenshot each X seconds.
#   --r:         resolution.
#   --S:         skip X frames. It helps to avoid corrupted frames.
#   --font:      font family and size for the bottom banner, increased.
#   --title:     banner title.
#   --timestamp: time format for the banner.
#   --underlay:  overlay an imagen in the frame.
#   filename:    the frame file name support time format variables.
fswebcam --device /dev/video1 --loop 60 -r 1280x1024 -S 5 --font sans:20 \
         --title "IEEE Student Branch of Granada" --timestamp "%d/%m/%Y %H:%M (%Z)" \
         --underlay logo_ieeesb.png "frames/frame_%d_%m_%Y_%H_%M_%S.jpg"
