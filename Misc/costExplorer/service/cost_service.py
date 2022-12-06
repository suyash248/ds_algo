from Misc.costExplorer.entity.customer import Customer
from typing import List
from datetime import date
from Misc.costExplorer.entity.product_subscription import ProductSubscription


class CostService(object):

    def __init__(self):
        self.customers: List[Customer] = []

    def addCustomer(self, customer: Customer):
        # TODO - Validation
        self.customers.append(customer)

    def subscribeToPlan(self, customerName: str, productSubscription: ProductSubscription):
        # TODO - Validation
        customer: Customer = list(filter(lambda cust: cust.name == customerName, self.customers))[0]
        customer.subscribeToProduct(productSubscription)


    def calculateMonthlyCost(self, customerName: str, productName: str) -> List[float]:
        customer: Customer = list(filter(lambda cust: cust.name == customerName, self.customers))[0]
        productSubscription: ProductSubscription = \
            list(filter(lambda sub: sub.name == productName, customer.subscriptions))[0]
        currMonth: int = date.today().month
        remainingMonths = 12 - (currMonth - productSubscription.monthNum) + 1
        return [0.0 for i in range(12-remainingMonths)] + [productSubscription.plan.monthlyCost for i in range(remainingMonths)]


    def annualCost(self, customerName: str, productName: str) -> float:
        totalCost = 0
        monthlyCost = self.calculateMonthlyCost(customerName, productName)
        for cost in monthlyCost:
            totalCost += cost
        return cost

    def combinedMonthlyCost(self, customerName):
        customer: Customer = list(filter(lambda cust: cust.name == customerName, self.customers))[0]

        totalCombinedCost: List[float] = [0.0 for i in range(12)]

        for sub in customer.subscriptions:
            prodMonthyCost: List[float] = self.calculateMonthlyCost(customerName, sub.name)

            for i, cost in enumerate(prodMonthyCost):
                totalCombinedCost[i] += cost

        return totalCombinedCost









