def numSquares(n):
    # these edges, are every perfect square under our input number n
    # these are essentially the weighted edges that we traverse between children looking for n
    edges = [i * i for i in range(1, int(n ** 0.5) + 1)]
    # if we have visited the child, then don't reappend to our list of children
    visited = [False] * (n + 1)
    # how far are we from the root, thats how many steps away we are, and is what we return
    level = 0
    # our children.
    children = [0]
    while True:
        # everytime we step further away, we increment our level denoting what step of the search we are on (BFS)
        level += 1
        # the children become the parents the further away we go
        parents = children
        # we have to repopulate the children array, to know where to go
        children = []
        # iterate through our parents.
        # we need to know what our summations are
        for parent in parents:
            # the edge weights are what are finding the children for us.
            for edge in edges:
                # calculate the child that we are on, and place it into the array if it hasn't been visited.
                child = parent + edge
                # if we found the value, return
                if child == n:
                    return level
                # if we go over, then this path is useless, break and don't append
                if child > n:
                    break
                # if we have visited this sum before, then dont append to the children array.
                if visited[child]:
                    continue
                visited[child] = True
                children.append(child)


numSquares(4)