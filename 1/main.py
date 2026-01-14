class Invoice:
    def __init__(self, invoice_id, customer_name, amount, vat_rate, paid):
        self.invoice_id = invoice_id
        self.customer_name = customer_name
        self.vat_rate = vat_rate
        self.paid = paid
        self._amount = None
        self.amount = amount
        

    @property
    def amount(self):
        return self._amount

    @amount.setter
    def amount(self, value):
        if value < 0:
            raise ValueError("סכום חשבונית לא יכול להיות שלילי")
        self._amount = value

    def calculate_total_with_vat(self):
        return self.amount * (1 + self.vat_rate / 100)

    def mark_as_paid(self):
        self.paid = True

    def show_details(self):
        status = "שולמה" if self.paid else "לא שולמה"
        print(f"חשבונית מספר: {self.invoice_id}")
        print(f"לקוח: {self.customer_name}")
        print(f"סכום לפני מע\"מ: {self.amount}")
        print(f"שיעור מע\"מ: {self.vat_rate}%")
        print(f"סכום כולל מע\"מ: {self.calculate_total_with_vat()}")
        print(f"סטטוס: {status}")


def main():
    invoice_id = input("הכנס מספר חשבונית: ")
    customer_name = input("הכנס שם לקוח: ")
    amount = float(input("הכנס סכום לפני מע\"מ: "))
    vat_rate = float(input("הכנס שיעור מע\"מ באחוזים: "))
    paid_input = input("האם החשבונית שולמה? (y/n): ").lower()
    paid = paid_input == "y"

    invoice = Invoice(invoice_id, customer_name, amount, vat_rate, paid)

    invoice.show_details()
    invoice.mark_as_paid()
    invoice.show_details()


if __name__ == "__main__":
    main()
