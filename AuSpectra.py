#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat Nov 17 15:00:19 2018

@author: salwanbutrus


At a minimum, there should be two options that the user can choose to control the output of the program. 
    1) No plot: type in file name to get info on spectrum (e.g. "sample A aggregated or is 58 nm based on correlation."
     can get the info as a table output. 
    2) Do #1 above AND plot all the spectra and label them. 
         a) normalized to highest value
         b) not normalized 
The info in #1 can just be attached to each spectrum rather than in a table, or both. 


Testing: 
    1) opening file
    2)


"""

import numpy as np
import matplotlib.pyplot as plt
import xlrd



#read file: this should eventually be an input from user


#path = ('/Users/salwanbutrus/Desktop/Desktop_Organized/ChE696/Project/TemplateDataSt400.xlsx')
#path = ('TemplateDataSt400.xlsx')
path = input("Enter a file name (e.g. data.xlsx): ")
wb = xlrd.open_workbook(path)
sheet1 = wb.sheet_by_index(0)

r = sheet1.nrows
c = sheet1.ncols



''' NEXT COMMIT: user should enter their x range and code should adapt: ask "what's the lower and upper limit if your lambdas" '''

xLimLflt = sheet1.cell(1,0).value
xLimL = int(xLimLflt)

xLimUflt = sheet1.cell(r-1,0).value
xLimU = int(xLimUflt)


#for loop that plots/analyzes based on how many columns
for x in range(1,c):
    
    #299 is the number of data points minus 2
    lambdas = sheet1.col_values(colx = 0,start_rowx = (xLimU - 299)-xLimL,end_rowx = r) #x-vals
    abso = sheet1.col_values(colx = x,start_rowx = (xLimU - 299)-xLimL,end_rowx = r) #y-vals loop cycles thru
    
    #400 is the lambda we start plotting at
    print("{} has a lambdaMax of {} at {} absorbance".format(sheet1.cell(0,x).value,  abso.index(max(abso)) + 400  ,  max(abso)  )   ) 
    
    plt.plot(lambdas, abso ,linewidth=2,label= sheet1.cell(0,x).value)
    plt.xlabel(sheet1.cell(0,0).value)
    plt.ylabel('Absorbance')
    plt.legend()
    plt.title('Not Normalized' )
    axes = plt.gca()
    axes.set_ylim([0 , 1.5])




#to normalize: 
#for x in range(0,r-1):
 #   abso1log.append(abso1[x]/max(abso))






#plt.savefig('testfig.png', format='png', dpi=1000)


#--Hardcode learning---#
#lambdas = sheet1.col_values(colx = 0,start_rowx = r-301,end_rowx = r) #x-vals

#abso1 = sheet1.col_values(colx = 1,start_rowx = r-301,end_rowx = r)
#abso2 = sheet1.col_values(colx = 2,start_rowx = r-301,end_rowx = r) 
#abso3 = sheet1.col_values(colx = 3,start_rowx = r-301,end_rowx = r) 

#xLabel = sheet1.cell(0,0).value
#yLabel1 = sheet1.cell(0,1).value
#yLabel2 = sheet1.cell(0,2).value
#yLabel3 = sheet1.cell(0,3).value


#plt.plot(lambdas,abso2,linewidth=2,label=yLabel2)
#plt.plot(lambdas,abso3,linewidth=2,label=yLabel3)
#plt.xlabel(xLabel)
#plt.ylabel('Absorbance')







    





