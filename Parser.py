#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sat May  4 00:24:52 2019

@author: avinash
"""

#import os
import xml.etree.ElementTree as et
import pandas as pd
tree = et.parse('GENIAcorpus3.02p/GENIAcorpus3.02.pos.xml')

root = tree.getroot()
#for child in root:
 #   print(child.tag)
#for child in root:
#    for element in child:
#            print(element.tag,":",element.text)
data_dict_title = {}
for child in root:
    for element in child:
        if element.tag=='articleinfo':
            for subelement in element:
                id = subelement.text
            print(id)
        if element.tag=='title':
            for subelement in element:
                disp=''
                for w_element in subelement:
                    disp=disp+w_element.text+' '
                print(disp)
                data_dict_title[id]=disp
final_l_title=[]
for id in data_dict_title:
    temp_dict={}
    temp_dict['Medline_No']=id
    temp_dict['Title']=data_dict_title[id]
    final_l_title.append(temp_dict)     

df_title = pd.DataFrame(final_l_title)
df_title = df_title[['Medline_No','Title']]
df_title.to_csv('title.csv',index=False)     

data_dict = {}            
for child in root:
    for element in child:
        if element.tag=='articleinfo':
            for subelement in element:
                id = subelement.text
            print(id)
        if element.tag=='abstract':
            for subelement in element:
                disp=''
                for w_element in subelement:
                    disp=disp+w_element.text+' '
                print(disp)
                if id in data_dict.keys():
                    data_dict[id]=data_dict[id] + disp + "/ "
                else:
                    data_dict[id]=disp
final_l=[]
for id in data_dict:
    temp_dict={}
    temp_dict['Medline_No']=id
    temp_dict['Abstract']=data_dict[id]
    final_l.append(temp_dict)
    
df = pd.DataFrame(final_l)
df = df[['Medline_No','Abstract']]
df.to_csv('abs.csv',index=False)

#data_dict = {}
#for child in root:
#    for element in child:
#        for subelement in element:
#            #print(subelement.tag,":",subelement.text)
#            if subelement.tag == 'bibliomisc':
#                id=id+subelement.text
#            print(id)
#            if subelement.tag == 'sentence':
#                disp=''
#                for w_element in subelement:
#                    disp=disp+w_element.text+' '
#                print(disp)
#                if id in data_dict.keys():
#                    data_dict[id]=data_dict[id] + disp + "/ "
#                else:
#                    data_dict[id]=disp
#                    
#df = pd.DataFrame(columns=list('MD'))
#for child in root:
#    for element in child:
#        for subelement in element:
#            #print(subelement.tag,":",subelement.text)
#            id=''
#            if subelement.tag == 'bibliomisc':
#                id=subelement.text
#            print(id)
#            if subelement.tag == 'sentence':
#                disp=''
#                for w_element in subelement:
#                    disp=disp+w_element.text+' '
#                print(disp)
#                df2 = pd.DataFrame([[id,disp]], columns=list('MD'))
#                df.append(df2, ignore_index=True)
#
#df = pd.DataFrame(columns=list('MD'))
#for child in root:
#    for element in child:
#        for subelement in element:
#            #print(subelement.tag,":",subelement.text)
#            id=''
#            list_dis = []
#            if subelement.tag == 'bibliomisc':
#                id=subelement.text
#            print(id)
#            if subelement.tag == 'sentence':
#                disp=''
#                for w_element in subelement:
#                    disp=disp+w_element.text+' '
#                list_dis.append(disp)
#            data_dict[id]=list_dis
#                    
#                
                
                