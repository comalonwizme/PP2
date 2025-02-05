class Bank:
    def __init__(self, owner, balance):
        self.owner = owner
        self.balance = balance

    def deposit(self, summ):
        if summ < 0:
            raise ValueError("Error")
        self.balance += summ

    def withdraw(self, summ_w):
        if summ_w < 0:
            raise ValueError("Error")
        if summ_w > self.balance:
            raise ValueError("Error")
        self.balance -= summ_w

    def sh(self):
        return f'owner: {self.owner}, balance: {self.balance}'

while True:
    try:
        own = input("Owner: ")
        if own == '123':
            print("Exit...")
            break

        bal = 44500
        ok = Bank(own, bal)

        while True:
            try:
                s = input("d(eposit), w(ithdraw), s(how), q(uite)").lower()
                if s == 'd':
                    sm = int(input("sum for deposit"))
                    ok.deposit(sm)
                    
                elif s == 'w':
                    sm = int(input("sum for withdraw"))
                    ok.withdraw(sm)
                elif s == 's':
                    print(ok.sh())
                elif s == 'q':
                    print("Exit...")
                    break
                else:
                    print("Error")
            except ValueError as e:
                print(f"Error: {e}")
    except ValueError as e:
        print(f"Error: {e}")

