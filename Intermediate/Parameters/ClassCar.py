class car(object) :
    def __init__ (self,make,model,year,condition, kms = 0):
        self.make= make;
        self.model = model;
        self.year = year;
        self.condition = condition;
        self.kms = kms;

    def display(self, showAll=True):
        if showAll:
            print("This car is a %s from %s, it is %s and has %s kms." % (self.make, self.model, self.year, self.condition))
        else:
            print("this car is missing data in the database")

whip = car('Ford', 'Fusion', 2012, "Mint Condition", 0);
whip.display();