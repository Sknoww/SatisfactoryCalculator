import json
from os import listdir

fileNames = []


def extractRecipe(fileName):
    recipe = {}
    with open("./generatedJson/" + fileName, "r+") as file:
        recipe = json.load(file)
        file.close()
    return recipe


def appendRecipe(recipe):
    with open("./resources/recipes.json", "r+") as file:
        data = json.load(file)
        data["recipes"]["standard"].append(recipe)
        file.close()
    return data


def writeJson(jsonRecipe):
    with open("./resources/recipes.json", "w+") as file:
        json.dump(jsonRecipe, file, indent=2, separators=(",", ":"))


def main():
    global fileNames
    fileNames = [f for f in listdir("./generatedJson")]
    for file in fileNames:
        writeJson(appendRecipe(extractRecipe(file)))


if __name__ == "__main__":
    main()
