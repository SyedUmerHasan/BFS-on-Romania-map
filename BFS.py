import collections


def new_bfs(graph, root):
    totalCost = 0
    visited, queue = set(), collections.deque([graph[root]["cityID"]])
    visited.add(graph[root]["cityID"])
    count = 0
    while queue:
        count += 1
        vertex = queue.popleft()
        for neighbour in graph[vertex]["connectingCities"]:
            if neighbour not in visited:
                visited.add(neighbour)
                print(neighbour)
                print(neighbour)
                queue.append(neighbour)
    print(visited)


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

            arrayOfDictionary.append(tempDictionary)

        print(arrayOfDictionary)
    else:
        print("*********************Using Default City Map*********************")
        arrayOfDictionary = [
            {'cityID': 0, 'nameOfCity': 'umer', 'connectingCities': [1, 2], "costOfConnectingCities": [10, 15]},
            {'cityID': 1, 'nameOfCity': 'saba', 'connectingCities': [0], "costOfConnectingCities": [10, 15]},
            {'cityID': 2, 'nameOfCity': 'sara', 'connectingCities': [3], "costOfConnectingCities": [10, 15]},
            {'cityID': 3, 'nameOfCity': 'Huzaifa', 'connectingCities': [1, 2], "costOfConnectingCities": [10, 15]}]
    return arrayOfDictionary


if __name__ == '__main__':
    # newarray = [{'cityID': 0, 'nameOfCity': 'umer', 'connectingCities': [1, 2]},
    #             {'cityID': 1, 'nameOfCity': 'saba', 'connectingCities': [0]},
    #             {'cityID': 2, 'nameOfCity': 'sara', 'connectingCities': [3]},
    #             {'cityID': 3, 'nameOfCity': 'Huzaifa', 'connectingCities': [1,2]}]
    newarray = input_map()
    new_bfs(newarray, 0)
