# @version ^0.3.0

beneficiary: address
amount: uint256


@external
def __init__(_beneficiary: address, _amount: uint256):
    self.beneficiary = _beneficiary
    self.amount = _amount
    send(self.beneficiary, self.amount)


@external
def payBill():

    # Pay the bill!
    send(self.beneficiary, self.amount)
