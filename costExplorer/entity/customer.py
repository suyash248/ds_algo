from costExplorer.entity.product_subscription import ProductSubscription
from typing import List

class Customer(object):
    def __init__(self, name):
        self.name = name
        self.subscriptions: List[ProductSubscription] = []

    def subscribeToProduct(self, productSub: ProductSubscription):
        # TODO - validation
        self.subscriptions.append(productSub)


