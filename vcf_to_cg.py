import itertools
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is made in python 2.7
"""
i=0
linenr=0
control_byone_li=[0]

with open('GRC13292545_Ycap_rmdup_raw_v1.ann2.head1K.vcf','r') as filein, open(filein.name[:-4]+'.var', 'a') as fileout:
    fileout.write('#FILE_ID\t'+filein.name[:-4]+'\n')
    fileout.write('#GENOME_REFERENCE\tNCBI build 37\n')
    fileout.write('#GENERATED_BY_customscript\tvcf_to_cg.py\n')
    fileout.write('.\n')
    fileout.write('>locus\tploidy\tallele\tchromosome\tbegin\tend\tvarType\treference\talleleSeq\tvarScoreVAF\tvarScoreEAF\tvarQuality\thapLink\txRef\n')
    for line in filein:
        linenr+=1
        
        if line[:1]!='#': #or line[:1]!='#':
            i=i+1
            li=line.strip().split('\t')
            print(filein.tell())
            nextline_li=next(filein).strip().split('\t')
            fileout.write(str(i)+'\t'+'1'+'\t'+'.\t'+'chrY\t'+li[1]+'\n')
            control_byone_li.append(li[1])
            control_byone_li.append(nextline_li[1])
            
            print('*******'+li[1])
            print(control_byone_li[-1])
            print('!!!'+ str(int(control_byone_li[-1])-int(li[1])))
            
            
            #if control_byone_li[-2]
            #print int(li[1])-int(control_byone_li[-2])#==int(li[1])
            
            #if int(control_byone_li[-1])-int(li[1])!=1:
             #  print 'eurraaa'
              # print int(control_byone_li[-1])-int(li[1])
               #print linenr
               #print line
              # break
    
            if i==50:
                break
            
