from GAME.utiles import GuiStructure
savingPath = 'structure.yaml'
gui = GuiStructure()

options1 = ['mu','sigma',"mu(A) - mu(B)","sigma(A)/sigma(B)"]
options2 = ['>', '<','>=', '<=','=', 'not equal to']

row = 0
gui.addElement('vl1', 'vl', [row,0], 'vl1',options=[10],withTitle=False)

row = 1
gui.addElement('h0variable', 'dropDown', [row,1], 'H0',options=options1)
gui.addElement('h0','dropDown',[row,2], '',
               options=options2,
               withTitle=False)
gui.addElement('h0value', 'textBox', [row,3], 'H0_value',withTitle=False)



row +=1
gui.addElement('h1variable', 'dropDown', [row,1], 'H1',options=options1)

gui.addElement('h1','dropDown',[row,2], '',
               options=options2,
               withTitle=False)

gui.addElement('h1value', 'textBox', [row,3], 'H1_value',withTitle=False)


row +=1
gui.addElement('vl2', 'vl', [row,0], 'vl3',options=[10],withTitle=False)


row +=1
gui.addElement('distributiontype', 'dropDown', [row,1], 'Distribution type',options=['Z','t-student','F'])


row +=1
gui.addElement('calczort', 'textBox', [row,1], 'Test Z, t, or F')
gui.addElement('tablezort', 'textBox', [row,3], 'Critical Z, t, or F')


row +=1
gui.addElement('conclusion', 'dropDown', [row,3], 'Conclusion', options=['Retain H0','Reject H0'])


#row +=1
#gui.addElement('errortype', 'dropDown', [row,1], 'Error type', options=['Type 1','Type 2'])
#gui.addElement('x2rej', 'textBox', [row,3], 'Max or min X to reject')


#row +=1
#gui.addElement('zort2rej', 'textBox', [row,1], 'Max or min Z/T to reject')
#gui.addElement('errorchance', 'textBox', [row,3], 'Probability of wrong conclusion')

row +=1
gui.addElement('vl3', 'vl', [row,0], 'vl3',options=[10],withTitle=False)



#gui.addElement('Some discriptions!', 'text', [15,1], 'Some discriptions!', withTitle=False)

gui.save(savingPath)
