class DecisionTree:
    """The class implements a decision tree with conditional logic."""
    
    def __init__(self):
        """Constructor"""
        self.credit_score = 0
        self.result = False

    def setCreditScore(self, cs):
        """Set credit score value."""
        self.credit_score = cs

    def executeTree(self):
        """Conditional logic to execute decision tree."""
        if self.credit_score > 700:
            self.result = True
        else:
            self.result = False

    def printState(self):
        """Return assessment based on decision tree execution."""
        retval = "Based on a credit score of " + str(self.credit_score)
        if self.result:
            retval=retval+", the loan should be awarded."
        else:
            retval=retval+", the loan should NOT be awarded."
        return retval
