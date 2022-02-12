import pytest
import asyncio

from starkware.starknet.testing.starknet import Starknet

# Enables modules.
@pytest.fixture(scope='module')
def event_loop():
    return asyncio.new_event_loop()

# Reusable to save testing time.
@pytest.fixture(scope='module')
async def contract_factory():
    starknet = await Starknet.empty()
    contract = await starknet.deploy("contracts/balance_tracker.cairo")
    return starknet, contract

@pytest.mark.asyncio
async def test_contract(contract_factory):
    starknet, contract = contract_factory

    # Starting value == 0
    response = await contract.get_balance().call()
    assert response.result.value == 0

    # Increase 2x
    await contract.increase_balance().invoke()
    await contract.increase_balance().invoke()
    response = await contract.get_balance().call()
    assert response.result.value == 2