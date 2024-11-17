def cmyk2rgba(colors):
    C,M,Y,K = colors
    r =  (1-C/100)*(1-K/100)
    g =  (1-M/100)*(1-K/100)
    b =  (1-Y/100)*(1-K/100)
    return [r,g,b,1]

def get_colors():
    colors = {}
    # Whites
    colors['Prototipo_Scocca_Esterna.stl'] = [0,0,0,0]
    colors['Prototipo_Scocca_Staffe.stl'] = [0,0,0,0]
    colors['Prototipo_Scocca_Supporto_Posteriore.stl'] = [0,0,0,0]
    colors['Prototipo_Vertebre_Supporti.stl'] = [0, 0, 0, 0]
    colors['Prototipo_Scocca_Interna.stl'] = [0, 0, 0, 0]
    colors['Prototipo_Scocca_Supporto_Muscoli.stl'] = [0, 0, 0, 0]

    # Discs
    colors['Prototipo_Disco_Intervertebrale_C2-3.stl'] = [46, 33, 14, 0]
    colors['Prototipo_Disco_Intervertebrale_C3-4.stl'] = [46, 33, 14, 0]
    colors['Prototipo_Disco_Intervertebrale_C4-5.stl'] = [46, 33, 14, 0]
    colors['Prototipo_Disco_Intervertebrale_C5-6.stl'] = [46, 33, 14, 0]
    colors['Prototipo_Disco_Intervertebrale_C6-7.stl'] = [46, 33, 14, 0]

    # Vertebraz
    colors['Prototipo_Vertebra_C1.stl'] = [19, 13, 44, 0]
    colors['Prototipo_Vertebra_C2.stl'] = [19, 13, 44, 0]
    colors['Prototipo_Vertebra_C3.stl'] = [19, 13, 44, 0]
    colors['Prototipo_Vertebra_C4.stl'] = [19, 13, 44, 0]
    colors['Prototipo_Vertebra_C5.stl'] = [19, 13, 44, 0]
    colors['Prototipo_Vertebra_C6.stl'] = [19, 13, 44, 0]
    colors['Prototipo_Vertebra_C7.stl'] = [19, 13, 44, 0]

    colors['Prototipo_Osso_Ioide.stl'] = [14, 19, 43, 0]

    # Muscles color
    colors['Prototipo_Muscoli_DX.stl'] = [15, 86, 69, 3]
    colors['Prototipo_Vena_Giugulare_SX.stl'] = [15, 86, 69, 3]
    colors['Prototipo_Muscolo_Stern_SX.stl'] = [15, 86, 69, 3]
    colors['Prototipo_Vene-Arterie_Vertebrali_DX.stl'] = [15, 86, 69, 3]
    colors['Prototipo_Muscolo_Miloioideo_DX.stl'] = [15, 86, 69, 3]
    colors['Prototipo_Muscolo_Stern_DX.stl'] = [15, 86, 69, 3]
    colors['Prototipo_Vene-Arterie_Vertebrali_SX.stl'] = [15, 86, 69, 3]
    colors['Prototipo_Vena_Giugulare_DX.stl'] = [15, 86, 69, 3]
    colors['Prototipo_Flessori_Spinali.stl'] = [15, 86, 69, 3]
    colors['Prototipo_Muscoli_SX.stl'] = [15, 86, 69, 3]
    colors['Prototipo_Muscolo_Miloioideo_SX.stl'] = [15, 86, 69, 3]

    # Medulla
    colors['Prototipo_Nervo_Vago_DX.stl'] = [13, 20, 72, 0]
    colors['Prototipo_Midollo_Parte_Interna.stl'] = [13, 20, 72, 0]
    colors['Prototipo_Midollo_Parte_Esterna.stl'] = [13, 20, 72, 0]
    colors['Prototipo_Nervo_Vago_SX.stl'] = [13, 20, 72, 0]


    # Black
    colors['Prototipo_Membrana_Giugulare-Carotide_DX.stl'] = [0, 0, 0, 100]
    colors['Prototipo_Membrana_Giugulare-Carotide_SX.stl'] = [0, 0, 0, 100]

    # Others
    colors['Prototipo_Esofago.stl'] = [23, 89, 92, 15]
    colors['Prototipo_Tiroide.stl'] = [23, 89, 92, 15]

    colors['Prototipo_Pacchetto_Tessuti.stl'] = [0,11,4,0]

    colors['Prototipo_Legamenti.stl'] = [13, 16, 31, 0]

    colors['Prototipo_Pacchetto_Laringe-Trachea.stl'] = [29,14,10,0]

    colors['Prototipo_Arteria_Carotide_DX.stl'] = [0, 100, 99, 0]
    colors['Prototipo_Arteria_Carotide_SX.stl'] = [0, 100, 99, 0]

    nu_colors = {}
    for key in colors:
        nu_colors[key] = cmyk2rgba(colors[key])

    return nu_colors


