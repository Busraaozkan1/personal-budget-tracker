class BudgetTracker:
    def __init__(self):
        self.income = 0
        self.expenses = {}

    def set_income(self, income):
        self.income = income
        print(f"Gelir başarıyla kaydedildi: {self.income} TL")

    def add_expense(self, category, amount):
        if category in self.expenses:
            self.expenses[category] += amount
        else:
            self.expenses[category] = amount
        print(f"{category} kategorisine {amount} TL gider eklendi.")

    def total_expenses(self):
        return sum(self.expenses.values())

    def calculate_balance(self):
        return self.income - self.total_expenses()

    def display_summary(self):
        print("\n** Bütçe Özeti **")
        print(f"Gelir: {self.income} TL")
        print("Giderler:")
        for category, amount in self.expenses.items():
            print(f"{category}: {amount} TL")
        print(f"Toplam Gider: {self.total_expenses()} TL")
        print(f"Bakiye: {self.calculate_balance()} TL")

def main():
    print("Personel Bütçe Takip Uygulamasına Hoş Geldiniz!")
    
    budget_tracker = BudgetTracker()

    income = float(input("Aylık Gelirinizi Girin: "))
    budget_tracker.set_income(income)

    while True:
        print("\n1. Gider Ekle")
        print("2. Bütçe Özeti Görüntüle")
        print("3. Çıkış")
        choice = input("Seçiminizi yapın (1/2/3): ")

        if choice == '1':
            category = input("Gider kategorisini girin (Örn: Kira, Gıda, Ulaşım): ")
            amount = float(input(f"{category} giderini girin: "))
            budget_tracker.add_expense(category, amount)
        elif choice == '2':
            budget_tracker.display_summary()
        elif choice == '3':
            print("Çıkılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()

