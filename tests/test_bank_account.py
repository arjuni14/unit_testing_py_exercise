import pytest
from bank_account.bank_account import BankAccount


@pytest.fixture
def start_account():
    return BankAccount(100)
    
def test_init():
    with pytest.raises(ValueError, match="Initial balance cannot be negative"):
        BankAccount(-100)
        
def test_positive_deposit(start_account):
    start_account.deposit(50)
    assert start_account.balance == 150

def test_negative_deposit(start_account):
    with pytest.raises(ValueError, match="Deposit amount must be positive"):
        start_account.deposit(-100)
        
def test_positive_withdraw(start_account):
    start_account.withdraw(30)
    assert start_account.balance == 70
    
def test_insufficient_withdraw(start_account):
    with pytest.raises(ValueError, match="Insufficient funds"):
        start_account.withdraw(150)
        
def test_positive_transfer_to(start_account):   
    new = BankAccount(0)
    start_account.transfer_to(new, 50)
    assert start_account.balance == 50
    assert new.balance == 50
    
def test_wrong_transfer_target(start_account):
    with pytest.raises(ValueError, match="Target must be a BankAccount"):
        start_account.transfer_to("Account Wrong", 10)