import csv, json


nodeTypes = None
nodeConfigs = {}


# Reads Node Types from nodeTypes.csv
def readNodeTypes():
    global nodeTypes
    with open("resources/nodeTypes.csv") as csvfile:
        reader = csv.reader(csvfile)
        nodeTypes = reader.__next__()

def readNodeConfigs():
    global nodeTypes
    for nodeType in nodeTypes:
        filename = "resources/" + nodeType.strip() + ".json"
        with open(filename) as f:
            nodeConfigs[nodeType] = json.load(f)
        break
    print(nodeConfigs)

def main():
    readNodeTypes()
    readNodeConfigs()
    return 0

if __name__ == "__main__":
    main()