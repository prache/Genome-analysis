
from subprocess import call
import os
import glob
#import Bio.SearchIO

defensin_path = ("/home/prana/Documents/pracheta/phd/2_phd2018/Data_comp_geno/pipeline_code/defensin_2.hmm")
#OwnPC address /home/pracheta/Documents/pracheta/phd2018/Data_comp_geno/pipeline_code
fileName_list = glob.glob("/home/prana/Documents/pracheta/phd/2_phd2018/Data_comp_geno/3_titled_amino_acid_seq/*")
#Own PC address /home/pracheta/Documents/pracheta/phd2018/Data_comp_geno/titled_amino_acid_seq

print(fileName_list, "## This is from my side ##")  # CONTAINS ALL THE FILES FROM THE FOLDER (fileName_list)

# read each file from the folder
def read_seq(inputfile):
    with open(inputfile, "r") as f:
        seq = f.read()
    return seq


outputFilePath = "/home/prana/Documents/pracheta/phd/2_phd2018/Data_comp_geno/4_hit_list_selected_results/"
#Own PC Address /home/pracheta/Documents/pracheta/phd2018/Data_comp_geno/hit_list_selected_results/

for filePath in fileName_list:
    filename = os.path.basename(filePath).split('.')[0]  # perhaps you can also use biopython library SeqI0.parse("filename.fas", "format")
    print("FileName (Full path)=" + filePath + ", just name:" + filename)
   # print("executing command:\n"+ hmmsearch -E 1e-10 --tblout "outputFilePath+filename+"_output.txt defensin_2.hmm "+ filePath+"\n")
    call(["hmmsearch", "-E", "1e-10", "--tblout", outputFilePath + filename + "_put.txt", defensin_path, filePath]) #need installed hmmer package on your machine