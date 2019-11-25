#GI stands for genetic identifiers
'''This script searches for identifiers using taxon names and genes, and uses those 
identifiers later to download the sequences from NCBI into an specified folder'''

#The name of your taxon and genes here
gene='18s'
taxon='Habronattus'

from Bio import Entrez
Entrez.email='example@gmail.com'#Specify your email
handle= Entrez.esearch(db='nucleotide', retmax=100000, term='%s'%taxon+'[ORGN] AND %s'%gene, idtype='acc')
record=Entrez.read(handle)
print(record)
handle.close()
for keys, values in record.items():
    if keys=='IdList':#If the category in the dictionary contains the GIs, then put each GI in a list
        GIs=[x for x in values]

print(GIs)

'''this function edits the first line of each fasta file to structure the name of the file
in the specified directory'''
def ProcName(firlin):
    new_firlin=firlin.split(' ')
    finalstring=''
    for k in range(len(new_firlin)):
        if k== 0:
            finalstring+=new_firlin[0].replace('>','')+' '
        if k==2:
            if 'cf' in new_firlin[k]:
                finalstring+=new_firlin[2].replace('.','')+'_'+new_firlin[3]
            else:
                finalstring+=new_firlin[2].replace('.','')
        if k==1:
            finalstring+=new_firlin[k]+' '
    return (finalstring)

'''####################################################################################'''

'''For each of the GIs retrieved by the esearch(), download them and 
put them into a fasta file, then export name it, then export it'''
#for gi in GIs:
#    handleII=Entrez.efetch(db='nuccore', id= gi, rettype= 'fasta', retmode='text')
#    first=True
#    for line in handleII:
#        if first:
#            name_file=line.split(' ')
#            export=open(r'/home/uriel/Desktop/NCBI/test_bIOSTAR/%s'%(gene+'_'+ProcName(line)),'w')
#            first=False
##        print(line.strip())
#        export.write(line)
#    export.close()


'''Alternatively, you can put everything in the same file, named after the 
taxon and the gene name into a fasta file.'''

'''With the sequences separated into tabs'''
#
#export=open(r'/home/uriel/Desktop/NCBI/test_bIOSTAR/%s_'%taxon+"%s"%gene+".fasta",'w')
#for gi in GIs:
#    handleII=Entrez.efetch(db='nuccore', id= gi, rettype= 'fasta', retmode='text')
#    for line in handleII:
#        export.write(line)
#export.close()


'''or as a single giant string (I recommend this one for aTRAM)'''

export=open(r'/home/uriel/Desktop/NCBI/test_bIOSTAR/%s_'%taxon+"%s"%gene+".fasta",'w')
for gi in GIs:
    handleII=Entrez.efetch(db='nuccore', id= gi, rettype= 'fasta', retmode='text')
    newstring=""
    First=True
    for line in handleII:
#        print(line)
        if not First:
            newstring+=line.strip()
        else:
            newstring+=line.strip()+"\n"
            First=False
    newstring+='\n'
    export.write(newstring)
export.close()
