class Payment:
    
    def __init__(self) -> None:
        self.__amount: float = None
    
    def setAmount(self, amount: float):
        self.__amount = amount

    def getAmount(self) -> float:
        return self.__amount

    def paymentDetail(self) -> None:
        print(f"The payment amount: {self.getAmount():.2f}€")

class CashPayment(Payment):

    def __init__(self, amount: float) -> None:
        super().__init__()
        self.setAmount(amount)

    def paymentDetail(self) -> None:
        print(f"Payment amount: {self.getAmount():.2f}€ in cash")
    
    def cashAmount(self) -> None:
        total: float = self.getAmount()
        amounts: list = [500,200,100,50,20,10,5,2,1,0.5,0.2,0.1,0.05,0.02,0.01]
        pieces: dict = {}
        print(f"{total:.2f}€ to be payed in cash with:")
        for amount in amounts:
            if total//amount >= 1:
                pieces[amount] = total//amount
                total -= amount*pieces[amount]
            if total <= 0:
                break
        for amount in pieces:
            print(f"{pieces[amount]:.0f} "+("banknotes of" if amount>=5 else "cents of")+f" {amount}€")
                
class CreditCardPayment(Payment):

    def __init__(self, amount: float, name_holder: str, expiration_date: str, card_num: str) -> None:
        super().__init__()
        self.setAmount(amount)
        self.name_holder: str = name_holder
        self.expiration_date: str = expiration_date
        self.card_num: str = card_num

    def paymentDetail(self) -> None:
        print(f"Payment amount: {self.getAmount():.2f}€ with credit card")
        print(f"Card holder: {self.name_holder}")
        print(f"Card expiration date: {self.expiration_date}")
        print(f"Card number: {self.card_num}")
