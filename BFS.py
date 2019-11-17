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
