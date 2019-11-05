#GI stands for genetic identifiers
'''This script searches for identifiers using taxon names and genes, and uses those 
identifiers later to download the sequences from NCBI into an specified folder'''

#The name of your taxon and genes here
gene='ND1'
taxon='Phidippus'

from Bio import Entrez
Entrez.email='example@gmail.com'#Specify your email
handle= Entrez.esearch(db='nucleotide', term='%s'%taxon+'[ORGN] AND %s'%gene, idtype='acc')
record=Entrez.read(handle)
handle.close()
for keys, values in record.items():
    if keys=='IdList':#If the category in the dictionary contains the GIs, then put each GI in a list
        GIs=[x for x in values]


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


'''For each of the GIs retrieved by the esearch(), download them and 
put them into a fasta file, then export name it, then export it'''
for gi in GIs:
    handleII=Entrez.efetch(db='nuccore', id= gi, rettype= 'fasta', retmode='text')
    first=True
    for line in handleII:
        if first:
            name_file=line.split(' ')
            export=open(r'/home/uriel/Desktop/NCBI/test_bIOSTAR/%s'%(gene+'_'+ProcName(line)),'w')
            first=False
#        print(line.strip())
        export.write(line)
    export.close()
