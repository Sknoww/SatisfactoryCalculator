#!/usr/bin/python
import json
import touch

from Helpers.recipe import Recipe


def checkInt(string):
    good = False
    first = True
    while not good:
        if first:
            try:
                value = float(string)
                return value
            except ValueError:
                first = False
                continue
        else:
            try:
                value = float(input("Invalid integer, re-input value: "))
                return value
            except ValueError:
                continue


def main():
    started = False
    first = True
    count = 0

    filenameBase = "./generatedJson/" + input(
        "Enter a filename prefix (.json will be appended automatically): "
    )
    filename = filenameBase + ".json"
    print()

    while True:
        if started:
            print("Creating next recipe...")
        else:
            print("Creating recipe...")
            started = True
        recipe = Recipe()
        recipe.components = {}
        recipe.consumptionRates = {}
        recipe.products = {}
        recipe.productionRates = {}
        recipe.name = input("Name: ").title()
        recipe.machine = input("Machine: ").title()
        numComponents = checkInt(input("Number of components: "))
        numProducts = checkInt(input("Number of products: "))
        for i in range(0, int(numComponents)):
            component = input("Component Name: ").title()
            componentAmount = checkInt(input("Component Amount: "))
            recipe.components[component] = componentAmount
        for key in recipe.components:
            recipe.consumptionRates[key] = checkInt(
                input("Consumption rate of " + str(key) + ": ")
            )
        for i in range(0, int(numProducts)):
            if i == 0:
                product = recipe.name.title()
                print("Main Product: " + product)
                productAmount = checkInt(input("Product Amount: "))
                recipe.products[product] = productAmount
            else:
                product = input("Product Name: ").title()
                productAmount = checkInt(input("Product Amount: "))
                recipe.products[product] = productAmount
        for key in recipe.products:
            recipe.productionRates[key] = checkInt(
                input("Production rate of " + str(key) + ": ")
            )

        jsonRecipe = json.dumps(recipe.asDict(), indent=2)
        print(jsonRecipe)
        check = input("Does this look right? (y/n): ")
        if check == "y":
            if first:
                touch.touch(filename)
                print("Printing to file: " + filename)
                with open(filename, "w+") as file:
                    json.dump(recipe.asDict(), file, indent=2, separators=(",", ":"))
                count += 1
                first = False
            else:
                filename = filenameBase + str(count) + ".json"
                touch.touch(filename)
                print("Printing to file: " + filename)
                with open(filename, "w+") as file:
                    json.dump(recipe.asDict(), file, indent=2, separators=(",", ":"))
                count += 1
        else:
            continue


if __name__ == "__main__":
    main()
