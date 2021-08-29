import os
import pandas as pd
import numpy as np
from scipy.stats import norm, expon
from scipy.stats.distributions import chi2
import math
import scipy
from GAME.utiles import checkValues


# =============================================================================

def check_res(feedbacks,mark_p,c_concl,sigl,mean1,mean2,N1,N2,std1,std2,Fcalc,Fcrit,results):

    r_testval=results['0']['calczort']
    r_concl=results['0']['conclusion']
    r_dist=results['0']['distributiontype']
    r_H0sign=results['0']['h0']
    r_H0val=results['0']['h0value']
    r_H0var=results['0']['h0variable']
    r_H1sign=results['0']['h1']
    r_H1val=results['0']['h1value']
    r_H1var=results['0']['h1variable']
    r_critval=results['0']['tablezort']

    if (type(r_H0sign) != int):
        if ( (r_H0sign != '=') and (r_H0sign != 'not equal to') and
                (r_H0sign != '<=') and (r_H0sign != '<') and
                (r_H0sign != '>=') and (r_H0sign != '>') ):
            if (math.isnan(r_H0sign) == True):
                r_H0sign='='
    if (type(r_H0sign) == int):
        if (r_H0sign == 0): 
            r_H0sign='='

    r_testval=check_str(r_testval)
    r_H0val=check_str(r_H0val)
    r_H1val=check_str(r_H1val)
    r_critval=check_str(r_critval)

    r_testval=float(r_testval)
    r_H0val=float(r_H0val)
    r_H1val=float(r_H1val)
    r_critval=float(r_critval)

    nq=10

    f,mark_p=mark_s('distribution type','F',r_dist,1./nq,mark_p)
    feedbacks.append(f)
    f,mark_p=mark_s('H0 hypothesized variable','sigma(A)/sigma(B)',r_H0var,1./nq,mark_p)
    feedbacks.append(f)
    f,mark_p=mark_s('H0 sign',">=",r_H0sign,1./nq,mark_p)
    feedbacks.append(f)
    f,mark_p=mark_f('H0 hypothesized value',1,r_H0val,1./nq,0.005,mark_p)
    feedbacks.append(f)
    f,mark_p=mark_s('H1 hypothesized variable','sigma(A)/sigma(B)',r_H1var,1./nq,mark_p)
    feedbacks.append(f)
    f,mark_p=mark_s('H1 sign',"<",r_H1sign,1./nq,mark_p)
    feedbacks.append(f)
    f,mark_p=mark_f('H1 hypothesized value',1,r_H1val,1./nq,0.005,mark_p)
    feedbacks.append(f)
    f,mark_p=mark_f('test value',Fcalc,r_testval,1./nq,0.005,mark_p)
    feedbacks.append(f)
    f,mark_p=mark_f('critical value',Fcrit,r_critval,1./nq,0.005,mark_p)
    feedbacks.append(f)
    if (Fcalc >= Fcrit):
        f,mark_p=mark_s('conclusion','Retain H0',r_concl,1./nq,mark_p)
    if (Fcalc < Fcrit):
        f,mark_p=mark_s('conclusion','Reject H0',r_concl,1./nq,mark_p)
    feedbacks.append(f)

    return(feedbacks,mark_p)

# =============================================================================
def check_str(string):

    string=str(string)
    string2=''
    L=len(string)
    for i in range(0,L):
        if ( (string[i] != ' ') and (string[i] != '\n') ):
            string2=string2+string[i]
    string=string2

    str2=string
    L=len(string)
    numdot=0
    if (L == 0):
        str2='-9999'
    for i in range(0,L):
        if (i == 0):
            if ( (string[i] != '0') and (string[i] != '1') and
                    (string[i] != '2') and (string[i] != '3') and
                    (string[i] != '4') and (string[i] != '5') and
                    (string[i] != '6') and (string[i] != '7') and
                    (string[i] != '8') and (string[i] != '9') and
                    (string[i] != '.') and (string[i] != '-') ):
                str2='-9999'
        if (i > 0):
            if ( (string[i] != '0') and (string[i] != '1') and
                    (string[i] != '2') and (string[i] != '3') and
                    (string[i] != '4') and (string[i] != '5') and
                    (string[i] != '6') and (string[i] != '7') and
                    (string[i] != '8') and (string[i] != '9') and
                    (string[i] != '.') ):
                str2='-9999'
        if (string[i] == '.'):
            numdot=numdot+1
            if (numdot > 1):
                str2='-9999'

    return(str2)

# =============================================================================
def mark_i(var_str,cor,res,mark,mark_p):

    if (abs(cor-res) < 0.01):
        f='The '+var_str+' is correct.\n'
        mark_p=mark_p+mark
    if (abs(cor-res) >= 0.01):
        f='The correct '+var_str+' is '+str(cor)+'.'

    return(f,mark_p)

def mark_f(var_str,cor,res,mark,tol,mark_p):

    if (abs(cor-res) < tol):
        f='The '+var_str+' is correct.\n'
        mark_p=mark_p+mark
    if (abs(cor-res) >= tol):
        f='The correct '+var_str+' is '+str(cor)

    return(f,mark_p)

def mark_s(var_str,cor,res,mark,mark_p):

    if (cor == res):
        f='The '+var_str+' is correct.\n'
        mark_p=mark_p+mark
    if (cor != res):
        cor_out=''
        L=len(cor)
        for i in range(0,L):
            if ( (cor[i] != '<') and (cor[i] != '>') ):
                cor_out=cor_out+cor[i]
            if ( (cor[i] == '<') or (cor[i] == '>') ):
                cor_out=cor_out+'$'
                cor_out=cor_out+cor[i]
                cor_out=cor_out+'$'
        f='The correct '+var_str+' is '+cor_out+'.'

    return(f,mark_p)

# =============================================================================
def input_loader(d_fn, verbous=False):
    inputs=pd.read_csv(d_fn)

    return inputs
# =============================================================================
def result_loader(r_fn, verbous=False):

    if (os.path.exists(r_fn)):
#        results = pd.read_excel(r_fn,sheet_name=0, index_col=0, header =[0]).to_dict()
        results = pd.read_csv(r_fn, index_col=0, header =[0]).to_dict()
    else:
        results = None
        if verbous: print('The result file is not found (%s)' % r_fn)


    return results

def marker(inputs, results):
    '''
    inputs and results are dict.
    '''

    feedbacks = []
    mark_p = 0
    if inputs is None:
        mark_p = None
        feedbacks.append('Input file is not found.\n')
    if results is None:
        mark_p = None
        feedbacks.append('Result file is not found.\n')
    if mark_p is None:
        feedbacks.append('Mark = None\n')

    if inputs is not None  and results is not None:

        sigl=float(inputs['0'][0])/100.
        mean1=float(inputs['0'][1])
        std1=float(inputs['0'][2])
        mean2=float(inputs['0'][3])
        std2=float(inputs['0'][4])
        N1=int(inputs['0'][5])
        N2=int(inputs['0'][6])

        Fcalc=(std1*std1)/(std2*std2)
        Fcrit=scipy.stats.f.ppf(sigl,N1-1,N2-1)
        if (Fcalc < Fcrit):
            t1='in the rejection region'
            t2='reject the Null Hypothesis'
            t3='Generator A works significantly better than Generator B'
            c_concl='Reject the Null Hypothesis'
        if (Fcalc >= Fcrit):
            t1='not in the rejection region'
            t2='accept the Null Hypothesis'
            t3='Generator A does not work significantly better than Generator B'
            c_concl='Retain the Null Hypothesis'

        feedbacks,mark_p=check_res(feedbacks,mark_p,c_concl,sigl,mean1,mean2,N1,N2,std1,std2,Fcalc,Fcrit,results)
        feedbacks.append('\n\n')
        feedbacks.append('-----------------------------\n')
        f='The question states that we need a flow that is consistently as close as possible to '+str(round(mean1,3))+' ampere, so we are testing for variances.  We need to do an F-test, and the hypotheses are :'
        feedbacks.append(f)
        f='H$_0:\\sigma_A/\\sigma_B \\geq 1$'
        feedbacks.append(f)
        f='H$_1:\\sigma_A/\\sigma_B < 1$'
        feedbacks.append(f)
        f='We calculate the test value as follows:\\begin{equation}F_{calc}=\\displaystyle \\frac{\\sigma_1^2}{\\sigma_2^2} = \displaystyle \\frac{('+str(round(std1,4))+')^2}{('+str(round(std2,4))+')^2}='+str(round(Fcalc,4))+'\\end{equation}'
        feedbacks.append(f)
        f='We have a left-tail test, so we need $\\alpha$ of the mass in the left tail.  In Excel (or Open Office Calc) f.inv('+str(round(sigl,4))+','+str(N1-1)+','+str(N2-1)+') results in a critical value of '+str(round(Fcrit,4))+'.  This means that we are '+t1+', and we '+t2+'.  The conclusion is that the '+t3+'.'
        feedbacks.append(f)

    return mark_p, feedbacks



# =============================================================================
def get_paths(base_path,Student_id,questionID):
    pass
# =============================================================================
# Helper ======================================================================

