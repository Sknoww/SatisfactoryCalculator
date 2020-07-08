#!/usr/bin/python
from pprint import pprint


def printMenu():
    print("===================================================")
    print("===== Welcome to the Satisfactory Calculator! =====")
    print("===================================================")
    print("\n")
    print("==================================================")
    print("======= For the Recipe Generator type 'rg' =======")
    print("======= For the main program type 'start'  =======")
    print("==================================================")
    print("\n")


def printRecipeNames(recipes):
    recipeNames = []
    for recipe in recipes["recipes"]["standard"]:
        recipeNames.append(recipe["name"])
    pprint(recipeNames)
