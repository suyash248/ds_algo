from costExplorer.entity.customer import Customer
from costExplorer.entity.plan import Plan
from costExplorer.entity.product_subscription import ProductSubscription
from costExplorer.service.cost_service import CostService

if __name__ == '__main__':
    costService: CostService = CostService()
    customer: Customer = Customer("cust1")

    costService.addCustomer(customer)
    costService.subscribeToPlan("cust1",
                                ProductSubscription("prod1", 2, Plan("BASIC", monthlyCost=10.0))
                                )

    costService.subscribeToPlan("cust1",
                                ProductSubscription("prod2", 2, Plan("BASIC", monthlyCost=20.0))
                                )

    print(costService.combinedMonthlyCost("cust1"))

    # annualCost = costService.annualCost("cust1", "prod1")
    # print(annualCost)
    #
    # monthlyCost = costService.calculateMonthlyCost("cust1", "prod1")
    # print(monthlyCost)
    #
    # annualCost = costService.annualCost("cust1", "prod2")
    # print(annualCost)
    #
    # monthlyCost = costService.calculateMonthlyCost("cust1", "prod2")
    # print(monthlyCost)




