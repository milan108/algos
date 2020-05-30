import math

def nearest_neighbour(unvisited):
    # visit first point
    visited = [unvisited[0]]
    unvisited.pop(0) 

    total,i = 0,0
    while len(unvisited) != 0:
        i = i + 1
        visited.append([0,0]) # so that visited[i] isnt out of range

        # select visited[i] as point nearest to visited[i - 1]
        closest = math.inf
        for j in unvisited:
            d = distance(j, visited[i - 1])
            if d < closest:                
                closest = d
                visited[i] = j

        total = total + closest
        unvisited.remove(visited[i]) 

    print("path: [", str(visited).strip('[]') + "], " + str(visited[0]))
    return total + distance(visited[0], visited[-1])

def closest_pair(chains):
    # param is a 3d array since we need 'distinct vertex chains'
    n = len(chains)
    total = 0
    for _ in range(0, n):
        d = math.inf
        sm, tm = [], []
        im, jm = -1, -1
        # find closest pair
        for i in range(0, n):
            for s in chains[i]:
                for j in range(0, n):
                    if i != j:
                        for t in chains[j]:
                            if distance(s,t) != 0 and distance(s,t) <= d:
                                d = distance(s,t)
                                sm, tm = s, t
                                im, jm = i, j
                                
        if d != math.inf:
            total += d
        if im != -1 and jm != -1:
            print(f"appending: {chains[jm]} to chain {chains[im]}")
            
            for x in chains[jm].copy():
                chains[im].append(x)
                chains[jm].remove(x)
    chains = [x for x in chains if x != []]   
    print(chains)
    return total + distance(chains[0][0], chains[0][-1])

def distance(p1, p2):
    return math.sqrt((p1[0] - p2[0])**2 + (p1[1] - p2[1])**2)    

def test_tsp():
    test_points = [[-1,-2], [8,9], [-11,-10], [6,1], [-6, -4]]
    actual_dist = distance([-1,-2],[-6,-4]) + distance([-6,-4],[-11,-10]) + distance([-11,-10], [6,1]) + distance([6,1],[8,9]) + distance([8, 9],[-1,-2])
    assert(nearest_neighbour(test_points.copy()) == actual_dist)
    test_points = [[[0,0]],[[0,1]],[[2,0]],[[4,0]],[[2,1]],[[4,1]]]
    actual_dist = distance([0,0],[0,1]) + distance([2,0],[2,1]) + distance([4,0],[4,1]) + distance([4,1],[2,1]) + distance([0,0], [2,0]) + distance([4,0], [0,1])
    # actual_dist = distance([0,0],[0,1]) + distance([2,0],[2,1]) + distance([4,0],[4,1]) + distance([4,1],[2,1]) + distance([0,0], [2,0])
    assert(closest_pair(test_points) == actual_dist)

def main():
    test_tsp()

if __name__ == '__main__':
    main()
