import pytest
import pytest_asyncio
from unittest.mock import patch
from bank_system import Account, Bank, InsufficientFundsError


def test_account_deposit():
    account = Account("123", "Omik Omikenski", 100.0)
    account.deposit(50.0)
    assert account.balance == 150.0


def test_account_withdraw():
    account = Account("123", "Omik Omikenski", 100.0)
    account.withdraw(50.0)
    assert account.balance == 50.0


@pytest_asyncio.fixture
async def accounts():
    acc1 = Account("123", "Chomik", 200.0)
    acc2 = Account("456", "Bob", 100.0)
    return acc1, acc2


@pytest.mark.asyncio
async def test_account_transfer(accounts):
    acc1, acc2 = accounts
    await acc1.transfer(acc2, 50.0)
    assert acc1.balance == 150.0
    assert acc2.balance == 150.0


@pytest.mark.asyncio
async def test_account_transfer_insufficient_funds(accounts):
    acc1, acc2 = accounts
    with pytest.raises(InsufficientFundsError):
        await acc1.transfer(acc2, 300.0)



def test_bank_create_account():
    bank = Bank()
    bank.create_account("123", "Omik Omikenski", 100.0)
    account = bank.get_account("123")
    assert account.owner == "Omik Omikenski"
    assert account.balance == 100.0


def test_bank_create_account_duplicate():
    bank = Bank()
    bank.create_account("123", "Omik Omikenski", 100.0)
    with pytest.raises(ValueError):
        bank.create_account("123", "Omik Omikenski", 200.0)


def test_bank_get_account_not_found():
    bank = Bank()
    with pytest.raises(ValueError):
        bank.get_account("999")


@pytest.mark.asyncio
async def test_bank_process_transaction():
    bank = Bank()
    bank.create_account("123", "Chomik", 200.0)
    bank.create_account("456", "Bob", 100.0)

    acc1 = bank.get_account("123")
    acc2 = bank.get_account("456")

    async def transaction():
        await acc1.transfer(acc2, 50.0)

    await bank.process_transaction(transaction)
    assert acc1.balance == 150.0
    assert acc2.balance == 150.0


@pytest.mark.asyncio
async def test_account_transfer_with_mock():
    acc1 = Account("123", "Chomik", 200.0)
    acc2 = Account("456", "Bob", 100.0)

    with patch.object(acc2, 'deposit', wraps=acc2.deposit) as mock_deposit:
        await acc1.transfer(acc2, 50.0)
        mock_deposit.assert_called_once_with(50.0)
        assert acc1.balance == 150.0
        assert acc2.balance == 150.0
