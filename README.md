# Spine-Phantom
MuJoCo Scene for Surgical Spine Phantom. Read "Operational Report" for more info.
## Contents of this repository and brief User's Guide
### Operational Report
Read for more info on this project.
### Spine Report Folder
Conrains .tex file and all figures used to generate Operational Report
### Python Scripts Folder
Contains the Python Scripts necessary to build the scene. User can run the "create_xml.py" scipt, specifying the directory to the .stl files and to the "base_model.xml" file. The script will create a new .xml file (with a chosen name) that contains the MuJoCo scene. Otherwise, use one of the available scenes.
### XML Files Folder
Contains the same pahntom scene in 3 different scales: mm (1:1), cm (10:1), dm (100:1). Also contains "base_model.xml" that is used by "create_xml.py" scipt.

### Meshes Folder  (remeshed .stl files)
Files are available in four scales (mm, cm, dm, m) and are too heavy for uploading on GitHub.\hyperref{} Click [here](https://drive.google.com/drive/folders/1_14Bji2TzGfnqww6hvkoo7rMVDzPE0qM?usp=drive_link)  to access the Google Drive folder containing them.
Also contains "phantom.blend" Blender File: the Blender scene with all the remeshed geometries. 

