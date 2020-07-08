#!/usr/bin/python


class Recipe(object):
    name: ""
    machine: ""
    components: {}
    consumptionRates: {}
    products: {}
    productionRates: {}

    def __init__(self):
        self.name: ""
        self.machine: ""
        self.components: {}
        self.consumptionRates: {}
        self.products: {}
        self.productionRates: {}

    def asDict(self):
        return {
            "name": self.name,
            "machine": self.machine,
            "components": self.components,
            "consumptionRates": self.consumptionRates,
            "products": self.products,
            "productionRates": self.productionRates,
        }
