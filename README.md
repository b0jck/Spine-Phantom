# Spine-Phantom
MuJoCo Scene for Surgical Spine Phantom. Read "Operational Report" for more info.
## Contents of this repository and brief User's Guide
### Operational Report
Read for more info on this project.
### Python Scripts Folder
Contains the Python Scripts necessary to build the scene. User can run the "create_xml.py" scipt, specifying the directory to the .stl files and to the "base_model.xml" file. The script will create a new .xml file (with a chosen name) that contains the MuJoCo scene. Otherwise, use one of the available scenes.
### XML Files Folder
Contains the same pahntom scene in 3 different scales: mm (1:1), cm (10:1), dm (100:1). Also contains "base_model.xml" that is used by "create_xml.py" scipt.
### phantom.bl Blender File
This file contains the Blender scene with all the remeshed geometries. 
### Meshes Folder  (remeshed .stl files)
Files are available in four scales (mm, cm, dm, m) and are too heavy for uploading on GitHub. Click here to access the Google Drive folder containing them

