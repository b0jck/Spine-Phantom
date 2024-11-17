from dm_control import mjcf
import os
import numpy as np
from lxml import etree
import build_phantom

# Path to base model
BASE_PATH = '/Users/bojack/Desktop/Report'
# Path to base model .xml
BASE_MODEL = '/Users/bojack/Desktop/Report/base_model.xml'

# Folder containing .stl files
ASSET_RELPATH = 'Phantom_Meshes_mm'

# Path to .stl Folder
ASSET_DIR = os.path.dirname(__file__) + '/' + ASSET_RELPATH

# Read base model
with open(BASE_MODEL, 'r') as f:
  model = mjcf.from_file(f)


meshdir = ASSET_DIR
model.compiler.meshdir = meshdir

meshes = []

# List all meshes names in folder
filenames = os.listdir(meshdir)

# Add meshes to the xml
for filename in filenames:
  # Skip non .stl files
  if not filename.endswith(".stl"):
    continue
  meshes.append(filename)
  model.asset.add('mesh', name=filename , file=filename)


geometries = []

# Add geometries to the xml
for geom in meshes:
  print(geom)
  geom = model.worldbody.add(
      'geom',
      name=geom,
      mesh=geom,
      type='mesh',
  )
  geometries.append(geom)


physics = mjcf.Physics.from_mjcf_model(model)


geom_position = {}
geom_size = {}



# 
for mesh in meshes:
  geom = model.find('geom', mesh)
  geom_position[mesh] = np.array(physics.bind(geom).pos)
  geom_size[mesh] = np.array(physics.bind(geom).rbound)
  geom.remove()

# Create Main phantom Body 
parent = model.worldbody.add("body",name = "phantom_body")


physics = mjcf.Physics.from_mjcf_model(model)
p_pos =  np.array(physics.bind(model.find('body', 'phantom_body')).xipos)

# Create phantom
palm = build_phantom.create_phantom(
    model,
    geom_position,
    parent=parent,
)

# 
print('Finalising and saving model.')
xml_string = model.to_xml_string('float', precision=4, zero_threshold=1e-7)
root = etree.XML(xml_string, etree.XMLParser(remove_blank_text=True))

print('Remove hashes from filenames')
assets = list(root.find('asset').iter())
for asset in assets:
  asset_filename = asset.get('file')
  if asset_filename is not None:
    name = asset_filename[:-4]
    extension = asset_filename[-4:]
    asset.set('file', name[:-41] + extension)
    
print('Add <compiler meshdir/>, for locally-loadable model')
compiler = etree.Element(
    'compiler', meshdir=ASSET_RELPATH, texturedir=ASSET_RELPATH
)
root.insert(0, compiler)

print('Remove class="/"')
default_elem = root.find('default')
root.insert(6, default_elem[0])
root.remove(default_elem)
xml_string = etree.tostring(root, pretty_print=True)
xml_string = xml_string.replace(b' class="/"', b'')

print('Insert spaces between top level elements')
lines = xml_string.splitlines()
newlines = []
for line in lines:
  newlines.append(line)
  if line.startswith(b'  <'):
    if line.startswith(b'  </') or line.endswith(b'/>'):
      newlines.append(b'')
newlines.append(b'')

# Final xml string
xml_string = b'\n'.join(newlines)

# Save to file.
XML_FILENAME = BASE_PATH + "/" +"spine_mm.xml"
f = open(XML_FILENAME, 'wb')
f.write(xml_string)
f.close()