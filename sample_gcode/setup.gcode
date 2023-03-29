;FLAVOR:Marlin
;TIME:206
;Filament used: 0.0980038m
;Layer height: 0.1
;MINX:95.2
;MINY:95.2
;MINZ:0.3
;MAXX:104.8
;MAXY:104.8
;MAXZ:3
;Generated with Cura_SteamEngine 5.0.0
M140 S60
M105
M190 S60
M104 S200
M105
M109 S200
M82 ;absolute extrusion mode
G21 ;metric values
G90 ;absolute positioning
M82 ;set extruder to absolute mode
M107 ;start with the fan off
G28 X0 Y0 ;move X/Y to min endstops
G28 Z0 ;move Z to min endstops
G1 Z15.0 F9000 ;move the platform down 15mm
G92 E0 ;zero the extruded length
G1 F200 E3 ;extrude 3mm of feed stock
G92 E0 ;zero the extruded length again
G1 F9000
;Put printing message on LCD screen
M117 Printing...
G92 E0
G92 E0
G1 F1500 E-6.5
;LAYER_COUNT:28
;LAYER:0
M107
;MESH:small_box.stl
G0 F3600 X95.2 Y95.2 Z0.3
;TYPE:WALL-OUTER
G1 F1500 E0
G1 F1800 X95.2 Y104.8 E0.47895
G1 X104.8 Y104.8 E0.95789
G1 X104.8 Y100 E1.19736
G1 X104.8 Y95.2 E1.43684
G1 X95.2 Y95.2 E1.91578
G0 F3600 X95.2 Y95.4
G0 X95.6 Y95.6
;TYPE:WALL-INNER
G1 F1800 X95.6 Y104.4 E2.35482
G1 X104.4 Y104.4 E2.79385
G1 X104.4 Y100 E3.01337
G1 X104.4 Y95.6 E3.23289
G1 X95.6 Y95.6 E3.67192
G0 F3600 X95.98 Y95.98
;TYPE:SKIN
G1 F1800 X95.98 Y104.02 E4.07304
G1 X104.02 Y104.02 E4.47415
G1 X104.02 Y100 E4.67471
G1 X104.02 Y95.98 E4.87527