#!/usr/bin/python
import Helpers.recipeGenerator
import Helpers.recipeCombiner
import Helpers.printers as printer
import initializer


def main():
    printer.printMenu()
    menuSelection = input("Enter 'rg' or 'start': ")
    Helpers.recipeGenerator.main() if menuSelection == "rg" else initializer.main()
    printer.printRecipeNames(initializer.recipes)


if __name__ == "__main__":
    main()
