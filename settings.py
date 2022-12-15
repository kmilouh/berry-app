# -*- encoding: utf-8 -*-
"""
app settings
"""

import os
from decouple import config

LOG_FOLDER= config('LOG_FOLDER', default="./logs/" ) 

SLICER_EXEC = config('SLICER_EXEC', default="/programs/Slicer-4.8.1-linux-amd64/Slicer" ) 
EMSEGMENTCOMMANDLINE = config('EMSEGMENTCOMMANDLINE', default=os.path.join(os.path.dirname(SLICER_EXEC).rstrip(os.path.sep),os.path.normpath("lib/Slicer-4.8/cli-modules/EMSegmentCommandLine").lstrip(os.path.sep)) )
MRML= config('MRML', default=os.path.join(os.path.dirname(SLICER_EXEC).rstrip(os.path.sep),os.path.normpath("share/Slicer-4.8/qt-loadable-modules/EMSegment/Tasks/MRI-Human-Brain-Hemisphere.mrml").lstrip(os.path.sep)) )

DCM2NIIX=config('DCM2NIIX', default="/programs/dcm2niix" )

MODEL1 = config('MODEL1', default="/models/lym_current" )
MODEL2 = config('MODEL2', default="/models/gbmet_current" )

DEBUG = config('DEBUG', default=False, cast=bool)
