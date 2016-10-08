from rdkit import Chem
from rdkit.Chem import AllChem

suppl = Chem.SmilesMolSupplier('minf_201500107_sm_479.txt')
w = Chem.SDWriter('out.sdf')
with open('minf_201500107_sm_479.txt') as fin:
    count = 0
    for eachline in fin:
        if count !=0:
            line = eachline.strip().split()
            mol = Chem.MolFromSmiles(line[0])
            if not mol: 
                print "skip molecules the rdkit doesn't read......"
                continue
            mol.SetProp("IC50",str(line[1]))
            mol.SetProp("cmpdNO",str(line[2]))
            AllChem.Compute2DCoords(mol)
            w.write(mol)
        count += 1


w.flush()