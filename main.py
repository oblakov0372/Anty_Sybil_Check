import asyncio
from request import process_wallet_address_async
from utils import save_to_csv, save_to_json, get_empty_data, get_correct_data

CHAIN_MAPPING = {
    '1': {'id': 324, 'name': 'ZkSync'},
    '2': {'id': 59144, 'name': 'Linea'},
    '3': {'id': 23448594291968336, 'name': 'Starknet'},
}

async def main_async():
    print("-------------------------------------------")
    print("****************Oblakov_0372***************")
    print("Donate (any EVM) 0x5416dac94ef60a4a1b77f90d90dd148af8789b5b")
    print()
    
    chain_number = input("Select chain:\n1. ZkSync\n2. Linea\n3. Starknet\n")
    chain_id = CHAIN_MAPPING.get(chain_number)

    if chain_id is not None:
        print(f"Selected chain ID: {chain_id['id']}")
        chain_name = chain_id['name']
        print(f"Selected chain name: {chain_name}")
    else:
        print("Invalid chain number. Please select 1, 2, or 3.")
        return

    with open('./addresses.txt', 'r') as file:
        wallet_addresses = file.read().splitlines()

    all_data = []

    async with asyncio.Semaphore(10):  
        tasks = [process_wallet_address_async(address, chain_id['id']) for address in wallet_addresses]

        results = await asyncio.gather(*tasks)

    for result, address in zip(results, wallet_addresses):
        if result is not None:
            score_data, interaction_data, batch_data = result
            all_data.append(get_correct_data(score_data, interaction_data, batch_data, address))
        else:
            all_data.append(get_empty_data(address))

    save_as = input("How to save file? \n1 - Json\n2 - CSV\n3 - Both\n")
    if save_as == "1":
        save_to_json(all_data, chain_name)
        print("File saved in current folder")
    elif save_as == "2":
        save_to_csv(all_data, chain_name)
        print("File saved in current folder")
    elif save_as == "3":
        save_to_csv(all_data, chain_name)
        save_to_json(all_data, chain_name)
        print("Files saved in current folder")
    else:
        print("Incorrect format")

if __name__ == '__main__':
    asyncio.run(main_async())
