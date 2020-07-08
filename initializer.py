#!/usr/bin/python
import csv
import json

recipes = {}
nodeTypes = None
globalConfigs = None


# Reads Node Types from nodeTypes.csv
def readGlobalConfigs():
    global globalConfigs
    with open("resources/globalConfigs.json") as f:
        globalConfigs = json.load(f)
    # print(json.dumps(globalConfigs, indent=2, separators=(",", ":")))


def readNodeTypes():
    global nodeTypes
    with open("resources/nodeTypes.csv") as csvfile:
        reader = csv.reader(csvfile)
        nodeTypes = reader.__next__()


def readRecipes():
    global recipes
    with open("resources/recipes.json", "r+") as file:
        recipes = json.load(file)
        file.close()
    # print(json.dumps(recipes, indent=2, separators=(",", ":")))


def main():
    readGlobalConfigs()
    readNodeTypes()
    readRecipes()


if __name__ == "__main__":
    main()
