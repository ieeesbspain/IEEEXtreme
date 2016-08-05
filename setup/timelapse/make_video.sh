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
# Reference: https://www.raspberrypi.org/learning/webcam-timelapse-setup/worksheet.md

# Create the list of frames
ls frames/*.jpg > frames/stills.txt

# Create video. Arguments:
#  -nosound:  The video does not have any sound.
#  -ovc:      Codec used to encode. libavc: libavcodec.
#  -lavcopts: Codec options. Encode as MPEG4 and video bit-rate.
#  -o:        Output file name.
#  -mf:       Input frame files options. JPEG files at 24 fps rate from frames/stills.txt
mencoder -nosound -ovc lavc -lavcopts vcodec=mpeg4:vbitrate=8000000 -o timelapse.avi -mf type=jpeg:fps=24 mf://@frames/stills.txt
