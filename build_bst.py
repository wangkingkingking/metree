

from node import Rnode, Snode

def build_bst(snode_list):
    
    if snode_list is None or len(snode_list) == 0:
        return Rnode()
    
    snode_list = sort_snode(snode_list)
    root = Rnode(snode_list=snode_list)
    
    return extract_baseline(root)


def extract_baseline(root):

    snode_list = root.snode_list

    if len(snode_list) == 1:
        return root
    
    start_snode = start(snode_list)
    baseline_snodes = hor(start_snode, snode_list)
    baseline_snodes = collect_regions(baseline_snodes)
    pass


def start(snode_list):

    tmp_list = snode_list
    
    while len(tmp_list) > 1:
        sn1, sn2 = tmp_list[-2:]
        if overlap(sn1, sn2) or contain(sn1, sn2) or
            (sn1.cls == 'VariableRange' and adjacent(s1, s2)):
            tmp_list.remove(sn2)
        else:
            tmp_list.remove(sn1)

    return tmp_list[0]

def hor()

def overlap(snode1, snode2):

