from Misc.costExplorer.entity.plan import Plan


class ProductSubscription(object):
    def __init__(self, name, monthNum: int, plan: Plan):
        self.name = name
        self.monthNum = monthNum
        self.plan = plan
