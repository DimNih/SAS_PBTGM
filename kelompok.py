class FinanceCalculator:
    def __init__(self,income):
        self.income = income
        self.expenses = 0
        self.savings = 0
        self.investment = 0


    def set_expenses(self,expenses):
        self.expenses = expenses

    def calculate_savings(self):
        self.savings = self.income - self.expenses
        return self.savings
    
    def set_invesment(self, investment):
        self.investment = investment

    def calculate_investment(self):
        return self.investment
    1
    def get_financial_status(self):
        return {
            'income': self.income,
            'expenses': self.expenses,
            'savings': self.calculate_savings(),
            'investment': self.calculate_investment()
        }    

def main():
    income = float(input("Masukan penghasilan bulanan Anda: RP "))
    finance = FinanceCalculator(income)

    expenses = float(input("Masukan pengeluaran bulanan anda: RP "))
    finance.set_expenses(expenses)

    investment = float(input("Masukan jumlah investasi bulanan Anda: RP "))
    finance.set_invesment(investment)

    financial_status = finance.get_financial_status()


    print("\nStatus Keuangan Anda:")
    print(f"Penghasilan: RP {financial_status['income']:,}")
    print(f"Pengeluaran: RP {financial_status['expenses']:,}")
    print(f"Tabungan: RP {financial_status['savings']:,}")
    print(f"Investasi: RP {financial_status['investment']:,}")
    
if __name__ == "__main__":
    main()   
    