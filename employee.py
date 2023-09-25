"""Employee pay calculator."""
"""ENTER YOUR SOLUTION HERE!"""


class Employee:
    def __init__(self, name):
        self.contract_rate = 0
        self.hours = 0
        self.salary = 0
        self.contracts = 0
        self.commission_rate = 0
        self.commission_bonus = 0
        self.name = name

    def set_salary(self, salary):
        self.salary = salary

    def set_contract(self, contract_rate, hours):
        self.contract_rate = contract_rate
        self.hours = hours

    def set_commission(self, commission_rate, contracts):
        self.commission_rate = commission_rate
        self.contracts = contracts

    def set_commission_bonus(self, commission_bonus):
        self.commission_bonus = commission_bonus

    def get_pay(self):
        return self.get_salary_pay() + self.get_commission_pay()

    def get_salary_pay(self):
        return self.salary + self.contract_rate * self.hours

    def get_commission_pay(self):
        return self.commission_bonus + self.commission_rate * self.contracts

    def __str__(self):
        if self.salary != 0:
            salary_contract = 'monthly salary of ' + str(self.get_salary_pay())
        else:
            salary_contract = 'contract of ' + str(self.hours) + ' hours at ' + str(self.contract_rate) + '/hour'

        commission = ''
        if self.commission_rate != 0:
            commission = ' and receives a commission for ' + str(self.contracts) + ' contract(s) at ' + str(
                self.commission_rate) + '/contract'
        if self.commission_bonus != 0:
            commission = ' and receives a bonus commission of ' + str(self.commission_bonus)
        total = '. Their total pay is ' + str(self.get_pay()) + '.'
        return self.name + ' works on a ' + salary_contract + commission + total


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie')
billie.set_salary(4000)

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie')
charlie.set_contract(25, 100)

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee')
renee.set_salary(3000)
renee.set_commission(200, 4)
# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan')
jan.set_contract(25, 150)  #
jan.set_commission(220, 3)

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie')
robbie.set_salary(2000)
robbie.set_commission_bonus(1500)

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel')
ariel.set_contract(30, 120)
ariel.set_commission_bonus(600)
