# -*- coding: utf-8 -*-
#
# grid_iaf_irr.py
#
# This file is part of NEST.
#
# Copyright (C) 2004 The NEST Initiative
#
# NEST is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# NEST is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with NEST.  If not, see <http://www.gnu.org/licenses/>.

'''
NEST Topology Module Example
Create layer of 12 freely placed iaf_neurons, visualize
BCCN Tutorial @ CNS*09
Hans Ekkehard Plesser, UMB
'''

import nest
import pylab
import random
import nest.topology as topo
import numpy as np
import matplotlib.pyplot as plt

pylab.ion()

nest.ResetKernel()

# generate list of 12 (x,y) pairs
pos = [[random.uniform(-0.5,0.5), random.uniform(-0.5,0.5)]
       for j in range(2500)]

#l1 = topo.CreateLayer({'extent': [1.5, 1.5],
                       #'positions': pos, 
                       #'elements': 'iaf_neuron'})

l1 = topo.CreateLayer({'columns': 50, 'rows': 50, 
                           'extent': [1.5, 1.5],
                           'elements': 'iaf_neuron', 'edge_wrap': True}) # HHHHHHHH AAAAAAAAAAA LLLLLLLLLL OOOOOOOOOOO 



conndict_rect = { 'connection_type': 'divergent',
             'mask': {'rectangular': {'lower_left': [-.16,-.16],
                                      'upper_right': [.16,.16]},
                      'anchor': [.0,0.02]},'kernel':.2512362}# 0.2, 0,05, 0.52
                      
                                            
conndict_circ = { 'connection_type': 'divergent',
             'mask': {'circular': {'radius': .75},
                    'anchor': [.0,0.]}}



topo.ConnectLayers(l1, l1, conndict_rect)


conn = nest.GetConnections(source=None, target=None, synapse_model=None)

conn = np.array(conn)

#Conn_information = topo.DumpLayerConnections(l1,'static_synapse','conn.txt')

C = np.zeros([2500,2500])
conn2 = conn[:,1] - 2
conn1 = conn[:,0] - 2
C[conn1,conn2] = 1
np.savetxt('local_connectivity.txt', C)
plt.imshow(C[1225].reshape(50,50))





#nest.PrintNetwork()
#nest.PrintNetwork(2)
#nest.PrintNetwork(2, l1)
#fig = topo.PlotLayer(l1,nodesize=80)
#ctr = topo.FindCenterElement(l1)
#topo.PlotTargets(ctr,l1, fig=fig,mask=conndictRect['mask'],kernel=conndictRect['kernel'],src_size=250,tgt_color='red',tgt_size=20,kernel_color='green')


