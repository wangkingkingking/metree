class Snode(object):

    def __init__(self, name, bbox):
        self.name = name
        self.cls = name2cls(name)
        self.bbox = bbox
        self.centroid = calcu_centroid()

    def calcu_centroid(self):
        pass
    
class Rnode(object):

    def __init__(self, label = 'EXPRESSION', snode_list = None):
        self.label = label
        self.snode_list = snode_list


RegionLabels = {
        'ABOVE',
        'BELOW',
        'SUPER',
        'SUBSC',
        'UPPER',
        'LOWER',
        'TLEFT',
        'BLEFT',
        'CONTAINS',
        'EXPRESSION'
        }


class bbox(object):
    
    def __init__(self, minx, miny, maxx, maxy):

        self.minx = minx
        self.miny = miny
        self.maxx = maxx
        self.maxy = maxy


class point(object):

    def __init__(self, x, y):
        self.x, self. y = x, y


def name2cls(name):
    pass 
