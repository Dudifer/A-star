from visualizer import *
class Node:

    
    def __init__(self,pos,f,g,h,np):
        self.pos = pos
        self.f = f
        self.g = g
        self.h = h
        self.np = np
#returns distance between position and end
def diff(pos1,pos2):
    d1 = abs(pos1[0]-pos2[0])
    d2 = abs(pos1[1]-pos2[1])
    return d1+d2
#returns valid neighbors of current node position
def neighborfinder (pos,map):
    maprows=len(map)
    mapcols=len(map[0])
    n1 = [pos[0]+1,pos[1]]
    n2 = [pos[0]-1,pos[1]]
    n3 = [pos[0],pos[1]+1]
    n4 = [pos[0],pos[1]-1]
    possibleneighbors = [n1,n2,n3,n4]
    realneighbors = []
    for x in possibleneighbors:
        if x[0] >= 0 and maprows>x[0]:
            if x[1]>=0 and mapcols>x[1]:
                if map[x[0]][x[1]]!= -1:    
                    realneighbors.append(x)
    return realneighbors

def astar(grid):
    skipper = .001
    start = grid.start 
    end = grid.end
    map = grid.get_map()
    open_list = {}
    closed_list = {}
    starting = Node (start,0,0,0,0)
    h = diff(start, end)
    starting.pos = start
    starting.h = h
    starting.f = h
    
    ending = Node (end,100,0,0,0) 

    open_list[str(starting.pos)] = starting
    #open_list[str(ending.pos)] = ending - Assuming these lines are irrelevant but just in case

    #print(sorted(key_value.items(), key = lambda kv:(kv[1], kv[0])))
    while (len(open_list.keys())!=0):
        cur=sorted(open_list.items(), key = lambda kv:(kv[1].f))[0][1]
        closed_list[str(cur.pos)] = cur 
        del open_list[str(cur.pos)]
        if cur.pos == end:
            ending = cur
            break
        neighbors = neighborfinder(cur.pos, map) 

        
        for x in neighbors:
            if str(x) in closed_list:
                continue
            if str(x) in open_list:
                if open_list[str(x)].g>cur.g+1:
                    cg = cur.g+1
                    open_list[str(x)].f=cg+open_list[str(x)].h
                    open_list[str(x)].g=cg
                    open_list[str(x)].np=cur.pos

            else:
                nh = diff(x,end)
                ng = cur.g+1
                nf = nh+ng 
                nnp=cur.pos
                npos = x
                neighbor = Node(npos,nf,ng,nh,nnp)
                open_list[str(x)] = neighbor
        open_list_keys = list(open_list.keys())
        closed_list_keys = list(open_list.keys())
        #print("Open list keys are: "+(str)(open_list_keys))
        #print("Closed list keys are: "+(str)(closed_list_keys))
          

        
        grid.mark_open(open_list)
        grid.mark_closed(closed_list)
        worker=cur
        path = []
        while worker.np !=0:

            path.append(worker.np)  
            worker=closed_list[str(worker.np)]
            if worker.np == worker.pos:
                print(5/0)
            grid.mark_path(path)
        grid.draw_grid()        
    worker=ending
    working=ending
    if cur != ending:
            print("No possible path :(")
    else:
        print (ending.pos)
        while worker.np !=0:
            worker=closed_list[str(working.np)]
            if worker.np == worker.pos:
                print(5/0)
            print(worker.pos)
            working = worker
    while skipper>0:
        skipper+=.001
        end_program=input('Would you like to end program? y or n:')
        if end_program=='y':
            skipper=0
    
        
    




    

