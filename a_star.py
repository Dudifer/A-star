class Node:

    
    def __init__(self,pos,f,g,h,np):
        self.pos = pos
        self.f = f
        self.g = g
        self.h = h
        self.np = np
def diff(pos1,pos2):
    d1 = abs(pos1[0]-pos2[0])
    d2 = abs(pos1[1]-pos2[1])
    return d1+d2

def neighborfinder (pos,map):
    map = map
    print (map)
    maprows=len(map)
    mapcols=len(map[0])
    n1 = [pos[0]+1,pos[1]]
    n2 = [pos[0]-1,pos[1]]
    n3 = [pos[0],pos[1]+1]
    n4 = [pos[0],pos[1]-1]
    possibleneighbors = [n1,n2,n3,n4]
    realneighbors = []
    for x in possibleneighbors:

        if map[x[0]][x[1]]!= -1:
            if x[0] >= 0 and maprows>=x[0]:
                if x[1]>=0 and mapcols>=x[1]:
                    realneighbors.append(x)
    return realneighbors




def astar(start, end, map):
    open_list = {}
    closed_list = {}
    starting = Node (start,0,0,0,0)
    #ending = Node (end,1,0,0,0) - Assuming these lines are irrelevant but just in case

    open_list[str(starting.pos)] = starting
    #open_list[str(ending.pos)] = ending - Assuming these lines are irrelevant but just in case

    #print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))
    while (len(open_list.keys())!=0):
        cur=sorted(open_list.items(), key = lambda kv:(kv[1].f))[0][1]
        closed_list[str(cur.pos)] = cur 
        neighbors = neighborfinder(cur.pos, map) 
        print (neighbors)
        break
    pass




    

def diff(pos1,pos2):
    d1 = abs(pos1[0]-pos2[0])
    d2 = abs(pos1[1]-pos2[1])
    return d1+d2