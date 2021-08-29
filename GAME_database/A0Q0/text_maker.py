import pandas as pd
import numpy as np
from random import choice as rnd_choice
r_int = np.random.randint 


def maker(file_path=None):
    inputs = input_maker(file_path)
    tex = tex_maker(file_path, inputs)
    return inputs, tex

def input_maker(file_path):

    ival=int(np.random.uniform(0,3,1))
    if (ival >= 3):
        print("E1Q4 error ival random number.")
        print(ival)
        exit()
    sigl=-9999
    if (ival == 0):
        sigl=1
    if (ival == 1):
        sigl=5
    if (ival == 2):
        sigl=10
    if (sigl < 0):
        print("E1Q4 error assigning significance level.")
        print(sigl)
        print(ival)
        exit()
    
    n1=r_int(16,28)
    n2=n1
    while (abs(n2-n1) < 2):
        n2=r_int(17,26)
    mean1=r_int(2100,2400)/10.
    std1=r_int(50,110)/10.
    mean2=mean1
    std2=std1+r_int(10,50)/10.

    A = [sigl, mean1, std1, mean2, std2, n1, n2]
    B = ['sigl', 'mean1', 'std1', 'mean2', 'std2', 'n1', 'n2']
    inputs = pd.DataFrame(A, B)    

    return inputs

def save_inputs(inputs, savingPath):
    inputs.to_csv(path_or_buf=savingPath,sep=',')

def tex_maker(file_path, inputs):
        
    sigl=int(inputs.loc['sigl'].values[0])
    mean1=inputs.loc['mean1'].values[0]
    std1=inputs.loc['std1'].values[0]
    mean2=inputs.loc['mean2'].values[0]
    std2=inputs.loc['std2'].values[0]
    n1=int(inputs.loc['n1'].values[0])
    n2=int(inputs.loc['n2'].values[0])

    tex=[]
    t1='For a biology experiment, a generator needs to deliver a current of\n'
    t2=str(mean1)+' ampere as constantly as possible.\n'
    t3='The lab technician is asked to test two different generators,\n'
    t4='more specifically generator A and generator B.\n'
    t5='After '+str(n1)+' tests, generator A is found to deliver an average flow\n'
    t6='of '+str(round(mean1,4))+' ampere, with a calculated standard\n'
    t7='deviation of '+str(round(std1,4))+' ampere.\n'
    t8='After '+str(n2)+' tests, generator B is found to deliver an average flow\n'
    t9='of '+str(round(mean2,4))+' ampere, with a calculated standard\n'
    t10='deviation of '+str(round(std2,4))+' ampere.\n'
    t11='With a significance level of '+str(round(sigl,4))+'\%, can this\n'
    t12='technician conclude that generator A is better than\n'
    t13='generator B?'

    tout=t1+t2+t3+t4+t5+t6+t7+t8+t9+t10+t11+t12+t13

    tex.append(tout)

    return tex    
