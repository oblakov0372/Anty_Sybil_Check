import aiohttp

params = {
    "account": "",
    "chainId": 0
}

headers = {
    'Authorization': 'TOKEN 567p6clw9uyosk3hn3l4q5pf1yuokyc1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
}

async def async_request_score(address, chain_id):
    url = "https://mp.trustalabs.ai/trustgo/score"

    params["account"] = address
    params["chainId"] = chain_id

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            if response.status == 200:
                response = await response.json()
                data = response["data"]
                score = data.get("score")
                rank = data.get("rank")
                sub_score = data.get("subScore", {})
                tenure = sub_score.get("tenure")
                monetary = sub_score.get("monetary")
                frequency = sub_score.get("frequency")
                diversity = sub_score.get("diversity")
                identity = sub_score.get("identity")
                sub_score_detail = data.get("subScoreDetail", {}).get("diversity", {})
                contracts_count = sub_score_detail.get("tic")
                protocols_count = sub_score_detail.get("tip")
                return score, rank, tenure, monetary, frequency, diversity, identity, contracts_count, protocols_count
            else:
                print(f"Error: {response.status} (Request Score)")
                return None

async def async_request_interaction_profile(address, chain_id):
    url = "https://mp.trustalabs.ai/trustgo/interaction-profile"

    params["account"] = address
    params["chainId"] = chain_id

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            if response.status == 200:
                response = await response.json()
                data = response["data"]
                total_ixn_cnt = data.get("total_ixn_cnt")
                total_ixn_amount = data.get("total_ixn_amount")
                days_gap = data.get("days_gap")
                return total_ixn_cnt, total_ixn_amount, days_gap
            else:
                print(f"Error: {response.status} (Request Interaction Profile)")
                return None

async def async_request_batch_query(address, chain_id):
    url = "https://mp.trustalabs.ai/trustgo/batch_query"

    params["account"] = address
    params["chainId"] = chain_id

    async with aiohttp.ClientSession() as session:
        async with session.get(url, params=params, headers=headers) as response:
            if response.ok:
                response = await response.json()
                data = response["data"]
                if data:
                    usdValue = data[0]["usdValue"]
                    activeDays = data[0]["activeDays"]
                    activeWeeks = data[0]["activeWeeks"]
                    activeMonths = data[0]["activeMonths"]
                    gas = data[0]["gas"]
                    return usdValue, activeDays, activeWeeks, activeMonths, gas
                else:
                    print("Error: No data in the response. (Request Batch Query)")
                    return None
            else:
                print(f"Error: {response.status} (Request Batch Query)")
                return None

async def process_wallet_address_async(address, chain_id):
    score_data = await async_request_score(address, chain_id)
    interaction_data = await async_request_interaction_profile(address, chain_id)
    batch_data = await async_request_batch_query(address, chain_id)
    
    if score_data is None or interaction_data is None or batch_data is None:
        print(f"Error processing data for wallet address: {address}")
        return None

    return score_data, interaction_data, batch_data

