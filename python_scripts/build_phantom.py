from dm_control import mjcf
import numpy as np
import trimesh
import phantom_colors
import os


def create_phantom(model, elem_positions, parent):
  phantom = parent.add('body', name='phantom')
  physics = mjcf.Physics.from_mjcf_model(model)
  phantom_pos = np.array(physics.bind(model.find('body', 'phantom')).xipos)
  phantom.pos = phantom_pos
    
  parent = phantom
  parent_pos = phantom_pos

# Group 1: Frame
  frame = ['Prototipo_Scocca_Esterna.stl', 'Prototipo_Scocca_Staffe.stl', 'Prototipo_Scocca_Supporto_Muscoli.stl',
           'Prototipo_Scocca_Interna.stl','Prototipo_Scocca_Supporto_Posteriore.stl', 'Prototipo_Vertebre_Supporti.stl', 
           'Prototipo_Pacchetto_Tessuti.stl']
  
# Group 2: Various
  various = ['Prototipo_Nervo_Vago_SX.stl', 
   'Prototipo_Membrana_Giugulare-Carotide_SX.stl',  
   'Prototipo_Legamenti.stl',   
   'Prototipo_Membrana_Giugulare-Carotide_DX.stl', 'Prototipo_Pacchetto_Laringe-Trachea.stl', 'Prototipo_Esofago.stl', 
    'Prototipo_Nervo_Vago_DX.stl', 'Prototipo_Osso_Ioide.stl', 'Prototipo_Tiroide.stl']
  
# Group 2: Various
  muscles = ['Prototipo_Muscoli_DX.stl', 'Prototipo_Muscolo_Stern_SX.stl', 'Prototipo_Muscolo_Miloioideo_DX.stl',
             'Prototipo_Muscoli_SX.stl', 'Prototipo_Muscolo_Stern_DX.stl', 'Prototipo_Muscolo_Miloioideo_SX.stl',
             'Prototipo_Flessori_Spinali.stl']
  
# Group 3: Veins
  veins = ['Prototipo_Vene-Arterie_Vertebrali_DX.stl', 'Prototipo_Arteria_Carotide_SX.stl', 'Prototipo_Vena_Giugulare_DX.stl',
           'Prototipo_Vena_Giugulare_SX.stl','Prototipo_Vene-Arterie_Vertebrali_SX.stl','Prototipo_Arteria_Carotide_DX.stl',]
  
# Group 4: Veins
  medulla = ['Prototipo_Midollo_Parte_Interna.stl', 'Prototipo_Midollo_Parte_Esterna.stl']
  
# Group 5: Veins
  spine = ['Prototipo_Vertebra_C1.stl', 'Prototipo_Vertebra_C2.stl', 'Prototipo_Disco_Intervertebrale_C2-3.stl', 'Prototipo_Vertebra_C3.stl', 
           'Prototipo_Disco_Intervertebrale_C3-4.stl','Prototipo_Vertebra_C4.stl', 'Prototipo_Disco_Intervertebrale_C4-5.stl',
            'Prototipo_Vertebra_C5.stl', 'Prototipo_Disco_Intervertebrale_C5-6.stl','Prototipo_Vertebra_C6.stl', 
            'Prototipo_Disco_Intervertebrale_C6-7.stl', 'Prototipo_Vertebra_C7.stl']
  

  phantom_bodies = []
  phantom_geo = []


  rgba_colors = phantom_colors.get_colors()

  # Frame
  child = parent.add('body' , name = "Frame", pos = phantom_pos)
  for i,elem in enumerate(frame):    
    r,g,b,a = rgba_colors[elem]
    colr = f"{r} {g} {b} {a}"      
    geom = child.add('geom',name=elem, mesh=elem, rgba = colr ,group="1")
    phantom_geo.append(geom)

  # Muscles
  child = parent.add('body' , name = "Muscles", pos = phantom_pos)
  for i,elem in enumerate(muscles):
    r,g,b,a = rgba_colors[elem]
    colr = f"{r} {g} {b} {a}"      
    geom = child.add('geom',name=elem, mesh=elem, rgba = colr ,group="2")
    phantom_geo.append(geom)

  
  # Various
  child = parent.add('body' , name = "Various", pos = phantom_pos)
  for i,elem in enumerate(various):
    r,g,b,a = rgba_colors[elem]
    colr = f"{r} {g} {b} {a}"
    geom = child.add('geom',name=elem, mesh=elem, rgba = colr ,group="2")
    phantom_geo.append(geom)
  

  # Veins
  child = parent.add('body' , name = "Veins", pos = phantom_pos)   
  for i,elem in enumerate(veins):
    r,g,b,a = rgba_colors[elem]
    colr = f"{r} {g} {b} {a}"      
    geom = child.add('geom',name=elem, mesh=elem,  rgba = colr ,group="3")
    phantom_geo.append(geom)

  # Medulla
  child = parent.add('body' , name = "Medulla", pos = phantom_pos)
  for i,elem in enumerate(medulla):
    r,g,b,a = rgba_colors[elem]
    colr = f"{r} {g} {b} {a}"      
    geom = child.add('geom',name=elem, mesh=elem,  rgba = colr ,group="4", conaffinity="5")
    phantom_geo.append(geom)

  spine_joints = []

  # Spine
  parent_pos = elem_positions[elem]
  parent = parent.add('body' , name = "Spine", pos = parent_pos, gravcomp="1")
  for i,elem in enumerate(spine):
    r,g,b,a = rgba_colors[elem]
    colr = f"{r} {g} {b} {a}"
    j_name = elem.replace('.stl','')
    elem_pos = elem_positions[elem]  
    child = parent.add('body' , name = elem, pos = elem_pos-parent_pos, gravcomp="1")
    joint = child.add('joint',name= j_name,
    type= "hinge",
    axis = [1 , 0 , 0],
    range= "-0.05 0.05",
    pos = [ 0 , 0 , 0])
    spine_joints.append(j_name)
    geom = child.add('geom',name=elem, mesh=elem, pos = -elem_pos,  contype="2", conaffinity="5", rgba = colr ,group="5")
    phantom_geo.append(geom)
    parent=child
    parent_pos=elem_pos

  # Movable capsule
  caps = model.worldbody.add('body', name="Capsule", pos = "0 0 .2")
  caps.add('freejoint')
  caps = caps.add('body')
  caps.add('geom', type="capsule", size=".1 .1", rgba=".8 .2 .1 1", contype="1", conaffinity="1")
  
  for i,elem in enumerate(spine_joints):
    if i==0:
      continue
  # Insert Tendons
    tendon = model.tendon.add("fixed",name="tendon" + str(i))
    tendon.add("joint", joint= spine_joints[i-1], coef=".05")
    tendon.add("joint", joint= spine_joints[i], coef=".05")


  model.equality.add("weld", body1="Prototipo_Vertebra_C7.stl", body2="world", solref="0.02 1", solimp="0.9 0.95 0.001")

# Insert Actuators
#Insert Sensors 
 # model.sensor.add("touch",site="forSensor",name="fingertip_sensor")
