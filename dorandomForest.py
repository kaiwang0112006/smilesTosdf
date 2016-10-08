########################################################
#
#  use numeric data only
#
########################################################
import csv
import copy
ic50 = []
with open('minf_201500107_sm_479.txt') as fin:
    reader = csv.reader(fin, delimiter='\t')
    for eachline in reader:
        if reader.line_num  == 1:
            ic50.append(eachline[1])
        
        
fout = open('poutclean','w')
        
with open('pout') as fin:
    reader = csv.reader(fin, delimiter='\t')
    for eachline in reader:
        line = copy.deepcopy(eachline)
        if reader.line_num  == 1:
            line.append('IC50')
        else:
            line.append(ic50[reader.line_num-1])
        lineStr = ','.join(line) + '\n'
        fout.write(lineStr)
fout.close()