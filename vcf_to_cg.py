from itertools import tee, zip_longest
# -*- coding: utf-8 -*-
"""
Spyder Editor

This is made in python 2.7
"""
def writqual(lis,filename):
    if li[6]=='REJECTED':
        filename.write('1\t'+'1\n')
        return 
    elif li[6]=='PASS':
        filename.write('100\t'+'100\n')
        return
    else:
        filename.write('CHECKCHEKCHECK\n')
        return 
            
                        


    
def pairwise(iterable):
    "s -> (s0,s1), (s1,s2), (s2, s3), ..."
    a, b = tee(iterable)
    next(b, None)
    return zip_longest(a, b)
i=1
linenr=0
temp=[]
firstline=True

with open('GRC14392020_customer_variants.LF_moskva.vcf','r') as filein, open(filein.name[:-4]+'.var', 'a') as fileout:
    fileout.write('#FILE_ID\t'+filein.name[:-4]+'\n')
    fileout.write('#GENOME_REFERENCE\tNCBI build 37\n')
    fileout.write('#GENERATED_BY_customscript\tvcf_to_cg.py\n')
    fileout.write('#ALL INDELS to ins')
    fileout.write('.\n')
    fileout.write('>locus\tploidy\tallele\tchromosome\tbegin\tend\tvarType\treference\talleleSeq\tvarScoreVAF\tvarScoreEAF\tvarQuality\thapLink\txRef\n')
    for line, nextline in pairwise(filein):
        if line==None:
            break
        linenr+=1
            
        
        if line[:1]!='#':
            i=i+1
            if nextline==None:#misjuhtub faili l6puskontrollida??
                break
            li=line.strip().split('\t')
            #nextline_li=nextline.strip().split('\t')
            #diff=int(nextline_li[1])-int(li[1])

            if firstline==True:
                fileout.write('1\t'+'1\t'+'1\t'+'chrY\t'+'0\t'+str(int(li[1])-1)+'\t'+'no-call\t'+'=\t'+'?\n')
                fileout.write('2\t'+'1\t'+'1\t'+'chrY\t'+str(int(li[1])-1)+'\t'+str(int(li[1]))+'\t')
                if li[4]=='.':
                    fileout.write('ref\t'+'=\t'+'=\t')
                    writqual(li, fileout)
                        
                        
                else:
                    fileout.write('snp\t'+li[3]+'\t'+li[4]+'\t')
                    writqual(li, fileout)
                
                    
                firstline=False
                temp=[li[1]]
                continue

            diff=int(li[1])-int(temp[0])
                
        
            if diff>1:
                fileout.write(str(i)+'\t'+'1\t'+'1\t'+'chrY\t'+str(temp[0])+'\t'+str(int(li[1])-1)+'\t'+'no-call\t'+'=\t'+'?\n')
                i=i+1
                fileout.write(str(i)+'\t'+'1\t'+'1\t'+'chrY\t'+str(int(li[1])-1)+'\t'+str(li[1])+'\t')
                if li[4]=='.':
                    fileout.write('ref\t'+'=\t'+'=\t')
                    writqual(li, fileout)
                    temp=[li[1]]
                    continue
                        
                        
                else:
                    fileout.write('snp\t'+li[3]+'\t'+li[4]+'\t')
                    writqual(li, fileout)
                    temp=[li[1]]
                    continue
           if (diff==1):
               fileout.write('APPI_1\n')
                
#            if diff==0:
#                fileout.write('APPI_0\n')
                
                
            
                
                 
            
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
            
