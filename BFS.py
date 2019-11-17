import collections

costArray = []


def filterByCityID(cityId, graph):
    iteratingArray = list(filter(lambda person: person['cityID'] == cityId, graph))
    iteratingArray = iteratingArray[0]
    return iteratingArray


def new_bfs(graph, root):
    for i in range(len(graph)):
        costArray.append(0)

    visited, queue = set(), collections.deque([graph[root]["cityID"]])
    visited.add(graph[root]["cityID"])
    count = 0
    while queue:
        count += 1
        # print("Iterating over Index ->", graph.)
        vertex = queue.popleft()
        iteratingArray = filterByCityID(vertex, graph)
        print("From", iteratingArray["nameOfCity"])
        count = 0
        for neighbour in graph[vertex]["connectingCities"]:
            # neighbour = graph[vertex]["connectingCities"][count]
            eachNeighbour = filterByCityID(neighbour, graph)
            print("to ", eachNeighbour["nameOfCity"])
            print("cost = ", iteratingArray["costOfConnectingCities"][count])
            if neighbour not in visited:
                costArray[eachNeighbour["cityID"]] = costArray[iteratingArray["cityID"]] + \
                                                     iteratingArray["costOfConnectingCities"][count]
                visited.add(neighbour)
                # print("IF Condition -> Inside > " ,neighbour)
                queue.append(neighbour)
            count += 1

        print("", end="\n")

    print("Total Cost = ", costArray)


def input_map():
    nameConditionOfNodes = input("Do you want to enter city details? Yes/No (No for Default Map) ?")

    arrayOfDictionary = []
    if nameConditionOfNodes.lower() == "yes":
        numberOfNodes = input("How many City you want to take?")
        loopNumber = range(int(numberOfNodes))
        for i in loopNumber:
            tempDictionary = {"cityID": i}
            nameOfNodes = input("Enter name of node %s => " % i)
            # Name of Node is being intialized
            tempDictionary["nameOfCity"] = nameOfNodes.lower()
            neighbourNodes = input("Enter name/number of neighbour node [1,2,3,4,5]=> ")
            # Removing spaces from Node Name
            neighbourNodes.replace(" ", "")
            # Lower casing for not to conflict with other cases
            neighbourNodes.lower()

            tempDictionary["connectingCities"] = neighbourNodes.split(",")
            tempDictionary["connectingCities"] = list(map(int, tempDictionary["connectingCities"]))

            costOfNeighbourNodes = input("Enter cost of neighbour nodes in respective terms [1,2,3,4,5]=> ")
            # Removing spaces from Node Name
            costOfNeighbourNodes.replace(" ", "")
            # Lower casing for not to conflict with other cases
            costOfNeighbourNodes.lower()

            tempDictionary["costOfConnectingCities"] = costOfNeighbourNodes.split(",")
            tempDictionary["costOfConnectingCities"] = list(map(int, tempDictionary["costOfConnectingCities"]))

            arrayOfDictionary.append(tempDictionary)

        return arrayOfDictionary
    else:
        print("*********************Using Default City Map*********************")
        arrayOfDictionary = [
            {'cityID': 0, 'nameOfCity': 'Oradea', 'connectingCities': [1, 2], "costOfConnectingCities": [71, 151]},
            {'cityID': 1, 'nameOfCity': 'Zerind', 'connectingCities': [3], "costOfConnectingCities": [75]},
            {'cityID': 2, 'nameOfCity': 'Sibiu', 'connectingCities': [3], "costOfConnectingCities": [140]},
            {'cityID': 3, 'nameOfCity': 'Arad', 'connectingCities': [1, 2], "costOfConnectingCities": [75, 140]}]
    return arrayOfDictionary


def dfs_iterative(graph, start):
    startCity = filterByCityID(start, graph)
    print("From ", startCity["nameOfCity"])
    stack, path = [start], []
    while stack:
        vertex = stack.pop()
        if vertex in path:
            continue
        path.append(vertex)
        myData = filterByCityID(vertex, graph)
        for neighbor in myData["connectingCities"]:
            stack.append(neighbor)
        print("To", myData["nameOfCity"], " with ID = ", myData["cityID"], ", Costs", costArray[myData["cityID"]])
    return path


def organizingArray(graph):
    # adjacency_list = {
    #     'A': [('B', 1), ('C', 3), ('D', 7)],
    #     'B': [('D', 5)],
    #     'C': [('D', 12)]
    # }
    tempDictionary = {}
    for eachNode in graph:
        eachArray = []
        for combine in range(int(len(eachNode["connectingCities"]))):
            eachArray.append((str(eachNode["connectingCities"][combine]), eachNode["costOfConnectingCities"][combine]))
        tempDictionary[str(eachNode["cityID"])] = eachArray
    return tempDictionary


class Graph:
    # example of adjacency list (or rather map)
    # adjacency_list = {
    # 'A': [('B', 1), ('C', 3), ('D', 7)],
    # 'B': [('D', 5)],
    # 'C': [('D', 12)]
    # }

    def __init__(self, adjacency_list):
        self.adjacency_list = adjacency_list

    def get_neighbors(self, v):
        return self.adjacency_list[v]

    # heuristic function with equal values for all nodes
    def h(self, n):
        H = {
            '0': 1,
            '1': 1,
            '2': 1,
            '3': 1
        }
        return H[n]

    def a_star_algorithm(self, start_node, stop_node):
        # open_list is a list of nodes which have been visited, but who's neighbors
        # haven't all been inspected, starts off with the start node
        # closed_list is a list of nodes which have been visited
        # and who's neighbors have been inspected
        open_list = set([start_node])
        closed_list = set([])

        # g contains current distances from start_node to all other nodes
        # the default value (if it's not found in the map) is +infinity
        g = {}

        g[start_node] = 0

        # parents contains an adjacency map of all nodes
        parents = {}
        parents[start_node] = start_node

        while len(open_list) > 0:
            n = None

            # find a node with the lowest value of f() - evaluation function
            for v in open_list:
                if n == None or g[v] + self.h(v) < g[n] + self.h(n):
                    n = v;

            if n == None:
                print('Path does not exist!')
                return None

            # if the current node is the stop_node
            # then we begin reconstructin the path from it to the start_node
            if n == stop_node:
                reconst_path = []

                while parents[n] != n:
                    reconst_path.append(n)
                    n = parents[n]

                reconst_path.append(start_node)

                reconst_path.reverse()

                print('Path found: {}'.format(reconst_path))
                return reconst_path

            # for all neighbors of the current node do
            for (m, weight) in self.get_neighbors(n):
                # if the current node isn't in both open_list and closed_list
                # add it to open_list and note n as it's parent
                if m not in open_list and m not in closed_list:
                    open_list.add(m)
                    parents[m] = n
                    g[m] = g[n] + weight

                # otherwise, check if it's quicker to first visit n, then m
                # and if it is, update parent data and g data
                # and if the node was in the closed_list, move it to open_list
                else:
                    if g[m] > g[n] + weight:
                        g[m] = g[n] + weight
                        parents[m] = n

                        if m in closed_list:
                            closed_list.remove(m)
                            open_list.add(m)

            # remove n from the open_list, and add it to closed_list
            # because all of his neighbors were inspected
            open_list.remove(n)
            closed_list.add(n)

        print('Path does not exist!')
        return None


if __name__ == '__main__':
    # arrayOfDictionary = [
    #     {'cityID': 0, 'nameOfCity': 'Oradea', 'connectingCities': [1, 2], "costOfConnectingCities": [71, 151]},
    #     {'cityID': 1, 'nameOfCity': 'Zerind', 'connectingCities': [3], "costOfConnectingCities": [75]},
    #     {'cityID': 2, 'nameOfCity': 'Sibiu', 'connectingCities': [3], "costOfConnectingCities": [140]},
    #     {'cityID': 3, 'nameOfCity': 'Arad', 'connectingCities': [1, 2], "costOfConnectingCities": [75, 140]}]
    newarray = input_map()
    print("**********************************************************")
    print("Breadth First Search")
    print("**********************************************************")
    new_bfs(newarray, 0)
    print("**********************************************************")
    print("Depth First Search")
    print("**********************************************************")
    dfspath = dfs_iterative(newarray, 0)
    print("The Path Followed = ", dfspath)
    print("**********************************************************")
    print("A* Search Algorithm")
    print("**********************************************************")
    # adjacency_list = {
    #     '0': [('1', 71), ('2', 151)],
    #     '1': [('3', 75)],
    #     '2': [('3', 140)],
    #     '3': [('1', 75), ('2', 140)]
    # }
    # print("======================")
    # print(organizingArray(newarray))
    # print("======================")
    adjacency_list = organizingArray(newarray)
    graph1 = Graph(adjacency_list)
    # Please chnage the values to find after adding
    path = graph1.a_star_algorithm('0', '3')

    A_Star_Cost = 0
    for i in path:
        A_Star_Cost = A_Star_Cost + costArray[int(i)]

    print("Total Cost for A Star = " , A_Star_Cost)

    print("The best Algorithm is A* search")