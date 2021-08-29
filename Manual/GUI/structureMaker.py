from GAME.utiles import GuiStructure
savingPath = 'structure.yaml'
gui = GuiStructure()

row = 0
gui.addElement('vl1', 'vl', [row,0], 'vl1',options=[10],withTitle=False)

row += 1
gui.addElement('dfa', 'textBox', [row,1], 'DF Among Columns')
gui.addElement('ssa', 'textBox', [row,3], 'SSA')
gui.addElement('sa2', 'textBox', [row,5], 'SA^2')
gui.addElement('fcalc', 'textBox', [row,7], 'Fcalc')

row += 1
gui.addElement('dfw', 'textBox', [row,1], 'DF Within Columns')
gui.addElement('ssw', 'textBox', [row,3], 'SSW')
gui.addElement('sw2', 'textBox', [row,5], 'SW^2')

row += 1
gui.addElement('dft', 'textBox', [row,1], 'Total DF')
gui.addElement('sst', 'textBox', [row,3], 'SST')

row += 1
gui.addElement('vl1', 'vl', [row,0], 'vl1',options=[10],withTitle=False)
gui.addElement('fcrit1', 'textBox', [row,1], 'Crit. Val. at 90% Conf.')
gui.addElement('fcrit2', 'textBox', [row,3], 'Crit. Val. at 99% Conf.')

row += 1
gui.addElement('concl1', 'dropDown', [row,1], 'Concl. at 90% Conf.',options=['Means are all Equal', 'Not all Means are Equal'])
gui.addElement('concl2', 'dropDown', [row,3], 'Concl. at 99% Conf.',options=['Means are all Equal', 'Not all Means are Equal'])

row += 1
gui.addElement('qalpha', 'textBox', [row,1], 'Qalpha')
gui.addElement('tkcrit', 'textBox', [row,3], 'T-K Crit. Val. at 90% Conf.')

row += 1
gui.addElement('diff12', 'dropDown', [row,1], 'Concl. at 90% Conf.',options=['Means Fert. 1 and 2 are Equal', 'Means for Fert. 1 and 2 Differ'])
gui.addElement('diff13', 'dropDown', [row,3], 'Concl. at 90% Conf.',options=['Means Fert. 1 and 3 are Equal', 'Means for Fert. 1 and 3 Differ'])
gui.addElement('diff14', 'dropDown', [row,5], 'Concl. at 90% Conf.',options=['Means Fert. 1 and 4 are Equal', 'Means for Fert. 1 and 4 Differ'])

row += 1
gui.addElement('diff15', 'dropDown', [row,1], 'Concl. at 90% Conf.',options=['Means Fert. 1 and 5 are Equal', 'Means for Fert. 1 and 5 Differ'])
gui.addElement('diff16', 'dropDown', [row,3], 'Concl. at 90% Conf.',options=['Means Fert. 1 and 6 are Equal', 'Means for Fert. 1 and 6 Differ'])
gui.addElement('diff23', 'dropDown', [row,5], 'Concl. at 90% Conf.',options=['Means Fert. 2 and 3 are Equal', 'Means for Fert. 2 and 3 Differ'])

row += 1
gui.addElement('diff24', 'dropDown', [row,1], 'Concl. at 90% Conf.',options=['Means Fert. 2 and 4 are Equal', 'Means for Fert. 2 and 4 Differ'])
gui.addElement('diff25', 'dropDown', [row,3], 'Concl. at 90% Conf.',options=['Means Fert. 2 and 5 are Equal', 'Means for Fert. 2 and 5 Differ'])
gui.addElement('diff26', 'dropDown', [row,5], 'Concl. at 90% Conf.',options=['Means Fert. 2 and 6 are Equal', 'Means for Fert. 2 and 6 Differ'])

row += 1
gui.addElement('diff34', 'dropDown', [row,1], 'Concl. at 90% Conf.',options=['Means Fert. 3 and 4 are Equal', 'Means for Fert. 3 and 4 Differ'])
gui.addElement('diff35', 'dropDown', [row,3], 'Concl. at 90% Conf.',options=['Means Fert. 3 and 5 are Equal', 'Means for Fert. 3 and 5 Differ'])
gui.addElement('diff36', 'dropDown', [row,5], 'Concl. at 90% Conf.',options=['Means Fert. 3 and 6 are Equal', 'Means for Fert. 3 and 6 Differ'])

row += 1
gui.addElement('diff45', 'dropDown', [row,1], 'Concl. at 90% Conf.',options=['Means Fert. 4 and 5 are Equal', 'Means for Fert. 4 and 5 Differ'])
gui.addElement('diff46', 'dropDown', [row,3], 'Concl. at 90% Conf.',options=['Means Fert. 4 and 6 are Equal', 'Means for Fert. 4 and 6 Differ'])
gui.addElement('diff56', 'dropDown', [row,5], 'Concl. at 90% Conf.',options=['Means Fert. 5 and 6 are Equal', 'Means for Fert. 5 and 6 Differ'])

row += 1
gui.addElement('vl1', 'vl', [row,0], 'vl1',options=[10],withTitle=False)

gui.save(savingPath)
