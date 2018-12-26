"""
Name:Drishak Mohan
University: University Of Toronto
"""

from typing import List

def get_average_elevation(m: List[List[int]]) -> float:
    """
    Returns the average elevation across the elevation map m.

    Examples
    >>> get_average_elevation([])
    0
    >>> m = [[1,2,3],[4,5,6],[7,8,9]]
    >>> get_average_elevation(m)
    5.0
    >>> m = [[1,2,2,5],[4,5,4,8],[7,9,9,1],[1,2,1,4]]
    >>> get_average_elevation(m)
    4.0625
    """
    count=0
    sum=0
    if m!=[] and m[0] != 0 and m[1]!=0:
        for i in m:
            if type(i)==list:
                for j in i:
                    if type(j)==int:
                        sum+=j
                        count+=1 
            else:
                return 0.0
        if sum/count !=0:
            return sum/count
        else:
            return 0.0
    else:
        return 0.0
    

def find_peak(m: List[List[int]]) -> List[int]:
    """
    Given an non-empty elevation map m, returns the cell of the
    highest point in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [9,8,7],
             [5,4,6]]
    >>> find_peak(m)
    [1,0]
    >>> m = [[6,2,3],
             [1,8,7],
             [5,4,9]]
    >>> find_peak(m)
    [2,2]
    """
    i=0
    a=[]
    while i<len(m):
        a+=[max(m[i])]
        i+=1   
    return [a.index(max(a)),m[a.index(max(a))].index(max(a))]
    

def is_sink(m: List[List[int]], c: List[int]) -> bool:
    """
    Returns True if and only if c is a sink in m.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> is_sink([[1,2,3],
             [2,3,3],
             [5,4,3]], [0,0])
    True
    >>> is_sink(m, [2,2])
    True
    >>> is_sink(m, [3,0])
    False
    >>> m = [[1,2,3],
             [2,1,3],
             [5,4,3]]
    >>> is_sink(m, [1,1])
    True
    """
    if c[0]> len(m)-1 or c[1] > len(m)-1:
        return False
    
    elif (c[0] in range(0,len(m)-1)) and (c[1]!=0 and c[1]!=len(m)-1):
        for i in range(c[0]-1,c[0]+2):
            for j in range(c[1]-1,c[1]+2):
                if abs((c[0]- i) <= 1) and abs((c[1] - j) <= 1):
                    if m[c[0]][c[1]]>m[i][j]:
                        return False
        return True
    
    elif c[0] in range(0,len(m)-1) and c[1]==0: 
        for i in range(c[0],c[0]+2):
            for j in range(c[1]-1,c[1]+2):
                if abs((c[0]- i) <= 1) and abs((c[1] - j) <= 1):
                    if m[c[0]][c[1]]>m[i][j]:
                        return False
        return True
    
    elif c[0] in range(0,len(m)-1) and c[1]==len(m)-1: 
        for i in range(c[0]-1,c[0]+2):
            for j in range(c[1]-1,c[1]+1):
                if abs((c[0]- i) <= 1) and abs((c[1] - j) <= 1):
                    if m[c[0]][c[1]]>m[i][j]:
                        return False
        return True
    
    elif c[0]==len(m)-1 and c[1]!=len(m)-1: 
        for i in range(c[0]-1,c[0]+1):
            for j in range(c[1]-1,c[1]+2):
                if abs((c[0]- i) <= 1) and abs((c[1] - j) <= 1):
                    if m[c[0]][c[1]]>m[i][j]:
                        return False
        return True
    
    elif c[0]==len(m)-1 and c[1]==len(m)-1: 
        for i in range(c[0]-1,c[0]+1):
            for j in range(c[1]-1,c[1]+1):
                if abs((c[0]- i) <= 1) and abs((c[1] - j) <= 1):
                    if m[c[0]][c[1]]>m[i][j]:
                        return False
        return True

def find_local_sink(m: List[List[int]], start: List[int]) -> List[int]:
    """
    Given a non-empty elevation map, m, starting at start,
    will return a local sink in m by following the path of lowest
    adjacent elevation.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[ 5,70,71,80],
             [50, 4,30,90],
             [60, 3,35,95],
             [10,72, 2, 1]]
    >>> find_local_sink([[ 5,70,71,80],
             [50, 4,30,90],
             [60, 3,35,95],
             [10,72, 2, 1]], [0,0])
    [3,3]
    >>> m = [[ 5,70,71,80],
             [50, 4, 5,90],
             [60, 3,35, 2],
             [ 1,72, 6, 3]]
    >>> find_local_sink(m, [0,3])
    [2,3]
    >>> m = [[9,2,3],
             [6,1,7],
             [5,4,8]]
    >>> find_local_sink(m, [1,1])
    [1,1]
    """
    if start[0]<=len(m)-1 and start[1]<=len(m)-1 and len(m)!=1:  
        if len(m[0])!=1:
            pi=[start[0],start[1]]
            lp= m[start[0]][start[1]]
            for x in range(start[0],len(m)):
                for y in range(start[1],len(m)):
                    if lp > m[x][y]:
                        pi=[x,y]
                        lp=m[x][y]
            return pi
        else:
            l=min(m)
            return m.index(l)

def can_hike_to(m: List[List[int]], s: List[int], d: List[int], supplies: int) -> bool:
    """
    Given an elevation map m, a start cell s, a destination cell d, and
    the an amount of supplies returns True if and only if a hiker could reach
    d from s using the strategy dscribed in the assignment .pdf. Read the .pdf
    carefully. Assume d is always south, east, or south-east of s. The hiker
    never travels, north, west, nor backtracks. 

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,4,3],
             [2,3,5],
             [5,4,3]]
    >>> can_hike_to(m, [0,0], [2,2], 4)
    True
    >>> can_hike_to(m, [0,0], [0,0], 0)
    True
    >>> can_hike_to(m, [0,0], [2,2], 3)
    False
    >>> m = [[1,  1,100],
             [1,100,100],
             [1,  1,  1]]
    >>> can_hike_to([[1,  1,100],
             [1,100,100],
             [1,  1,  1]], [0,0], [2,2], 4)
    False
    >>> can_hike_to(m, [0,0], [2,2], 202)
    True
    """
    if (s[0]<=len(m)-1 and s[1]<=len(m)-1 and d[0]<=len(m)-1 and d[1]<=len(m)-1):
    
        while s != d:
            [x,y]=s 
            
            if s[0]==len(m)-1:
                supplies -= abs(m[x][y] - m[x][y+1])
                s=[x,y+1]
            
            elif s[0]==d[0] :
                supplies -= abs(m[x][y] - m[x][y+1])
                s=[x,y+1]

            elif s[1]==d[1] and s[0]!=d[0]:
                supplies -= abs(m[x][y] - m[x+1][y])
                s=[x+1,y] 

            elif abs(m[x][y]-m[x+1][y]) >= abs(m[x][y]-m[x][y+1]):
                supplies -= abs(m[x][y] - m[x][y+1])
                s=[x,y+1]
            
            elif abs(m[x][y]-m[x][y+1]) >  abs(m[x][y]-m[x+1][y]):
                supplies -= abs(m[x][y] - m[x+1][y])
                s=[x+1,y]
            
        if s==d and supplies>=0:
            return True 
        else:
            return False
    
    else:
        return False


def rotate_map(m: List[List[int]]) -> None:
    """
    Rotates the orientation of an elevation map m 90 degrees counter-clockwise.
    See the examples to understand what's meant by rotate.

    Examples (note some spacing has been added for human readablity)
    >>> m = [[1,2,3],
             [2,3,3],
             [5,4,3]]
    >>> rotate_map(m)
    >>> m
    [[3,3,3],
     [2,3,4],
     [1,2,5]]
    >>> m = [[5,9,1,8],
             [2,4,5,7],
             [6,3,3,2],
             [1,7,6,3]]
    >>> rotate_map(m)
    >>> m
    [[8,7,2,3],
     [1,5,3,6],
     [9,4,3,7],
     [5,2,6,1]]
    """
    r = len(m)
    if r == 0:
        return []
    c = len(m[0])
    L = []
    for i in range(c):
        Lr = []
        for j in range(r):
            Lr.append(m[j][i])
        L.append(Lr)
    m = L[::-1]
    return None

"""
You are not required to understand or use the code below. It is there for
curiosity and testing purposes.
"""
def create_real_map()-> List[List[int]]:
    """
    Creates and returns an elevation map from the real world data found
    in the file elevation_data.csv.

    Make sure this .py file and elevation_data.csv are in the same directory
    when you run this function to ensure it works properly.
    """
    data = open("elevation_data.csv")
    m = []
    for line in data:
        m.append(line.split(","))
    data.close()
    for i in range(len(m)):
        for j in range(len(m[i])):
            m[i][j] = int(m[i][j])
    return m
    
    










    
