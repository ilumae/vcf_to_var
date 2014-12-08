from itertools import tee, zip_longest
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is made in python 2.7
"""
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip_longest(a, b)
i=0
linenr=0
control_byone_li=[]

with open('GRC13292545_Ycap_rmdup_raw_v1.ann2.head1K.vcf','r') as filein, open(filein.name[:-4]+'.var', 'a') as fileout:
    fileout.write('#FILE_ID\t'+filein.name[:-4]+'\n')
    fileout.write('#GENOME_REFERENCE\tNCBI build 37\n')
    fileout.write('#GENERATED_BY_customscript\tvcf_to_cg.py\n')
    fileout.write('.\n')
    fileout.write('>locus\tploidy\tallele\tchromosome\tbegin\tend\tvarType\treference\talleleSeq\tvarScoreVAF\tvarScoreEAF\tvarQuality\thapLink\txRef\n')
    for line, nextline in pairwise(filein):
        linenr+=1
        
        if line[:1]!='#': #or line[:1]!='#':
            i=i+1
            li=line.strip().split('\t')
            if nextline==None:
                break
        
            nextline_li=nextline.strip().split('\t')
            fileout.write(str(i)+'\t'+'1\t'+'.\t'+'chrY\t'+li[1]+'\t'+nextline_li[1]+'\t')

            if (int(nextline_li[1])-int(li[1])==1) and li[4]=='.':
                 fileout.write('ref'+'\n')
            if (int(nextline_li[1])-int(li[1])==1) and li[4]!='.':
                fileout.write('snp\t'+li[3]+'\t'+li[4]+'\n')
                 
            
            #control_byone_li.append(li[1])
            #control_byone_li.append(nextline_li[1])
            
            #print('*******'+li[1])
            #print(control_byone_li[-1])
            #print('!!!'+ str(int(control_byone_li[-1])-int(li[1])))
            
        
            
            #if li[6]=='PASS':
                #fileout.write(li[8]
            #else
             #  print 'eurraaa'
              #print(int(nextline_li[1])-int(li[1]))
                  #print(linenr)
                  #print(line)
              # break
    
            #if i==50:
#                print(control_byone_li)
#                break
            
