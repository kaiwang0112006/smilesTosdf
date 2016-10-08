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
        if reader.line_num  != 1:
            ic50.append(eachline[1])
 
        
fout = open('pouttransfer','w')
        
with open('pout') as fin:
    reader = csv.reader(fin, delimiter='\t')
    for eachline in reader:
        line = copy.deepcopy(eachline)
        if reader.line_num  == 1:
            line.append('IC50,class')
        else:
            bio = ic50[reader.line_num-2]
            if bio == '>1':
                c = 'NA'
            elif '>' in bio:
                c = 0
            elif float(bio) > 20:
                c = 0
            elif float(bio) <= 20:
                c = 1
            line.append("%s,%s" % (str(bio),str(c)))
        lineStr = ','.join(line) + '\n'
        fout.write(lineStr)

fout.close()