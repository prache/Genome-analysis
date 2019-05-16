#This it to get the final sequence. Step 1- it selects the key from profile result
# step 2- then this key will scan the amino acid seq and then in step3 it will fetch the whole amino acid seq.
#step 4- it will fill the output file with the selected amino acid seq.

#!/usr/bin/env python2
# -*- coding: utf-8 -*-
"""
Created on Mon Nov 26 15:34:01 2018
@author: pracheta
"""
import glob
import os
from Bio import SeqIO
#import Bio.SeqIO #from Bio

#file paths
AAseq_folderPath = "/home/pracheta/Documents/pracheta/phd2018/Data_comp_geno/titled_amino_acid_seq/" #to fetch AA seq, use of main files
# /home/pracheta/Documents/pracheta/phd2018/Data_comp_geno/titled_amino_acid_seq
hmmSearch_resultFolder = glob.glob("/home/pracheta/Documents/pracheta/phd2018/Data_comp_geno/hit_list_selected_results/*.txt")

 #using the profile results
Final_result_folderPath = "/home/pracheta/Documents/pracheta/phd2018/Data_comp_geno/try_seq_for_tree/"

#created output directory

'''Create the output directory if it does not exist'''
if not os.path.exists(Final_result_folderPath):
    os.mkdir(Final_result_folderPath)
    print("success")

'''Now
    1. Go through each file in hmm search folder
    2. Find ID from each file
    3. find the corresponding amino acid sequences from AAseq_file
    4. Write them to the file
'''
for hmmSearch_resultFile in hmmSearch_resultFolder:
    bareFile = os.path.basename(hmmSearch_resultFile).replace("_output.txt", "")
    #bareFile = hmmSearch_resultFile.replace('_output.txt', '')
    print("bareFile:"+bareFile)
    seqFile = glob.glob(AAseq_folderPath + bareFile + ".*")#get fasta file with any extension (index is missing in the end [0] but shows error if I add that on)
    print(seqFile)
    if len(seqFile) == 0 :
        print("There's no fasta file corresponding to "+ bareFile)
        continue #Do not further process this file. Go to next file
    elif

    AAseq_file = seqFile[0]
    print("AAseq_file:", AAseq_file) #I removed + instead ,
    #AAseq_file = AAseq_folderPath + bareFile + ".fsa"
    #print("AAseq_file:", AAseq_file)
    final_result_file = Final_result_folderPath+ bareFile + ".fsa"
    print("Final_result_folderPath:"+Final_result_folderPath)


    finalResult = "" #initialize finalResult with empty string for new file
    with open(hmmSearch_resultFile) as f:
        for line in f:
            if line.strip()[0] != '#':
                ID = line.split(" ")[0]
                print (ID)
                record_dict = SeqIO.index(AAseq_file, "fasta")
                #for seq_record in SeqIO.parse(AAseq_file, "fasta"):
                 #   if seq_record.id == ID:
                        #collectSequence = str(seq_record.seq)
                        #break #breaks  loop : for seq_record in SeqIO.parse(AAseq_file, "fasta"):
                collectSequence = record_dict[ID]
                entry = collectSequence.format("fasta")
                #entry = ">"+ ID+ "\n"+ collectSequence +"\n"
                print(entry)
                finalResult = finalResult + entry
                record_dict.close()

    outfile = open("final_result_file", 'w')
    outfile.write(finalResult)
    outfile.close()