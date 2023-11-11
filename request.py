import requests


params = {
    "account": "",
    "chainId": 0
}

headers = {
    'Authorization': 'TOKEN 567p6clw9uyosk3hn3l4q5pf1yuokyc1',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
    'Accept-Language': 'en-US,en;q=0.5',
}


def request_score(address, chain_id):
    url = "https://mp.trustalabs.ai/trustgo/score"
    
    params["account"] = address
    params["chainId"] = chain_id
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json().get("data", {})
        if data:
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
            print("Error: No data in the response. (Request Score)")
            return None
    else:
        print(f"Error: {response.status_code} (Request Score)")
        return None
    
def request_interaction_profile(address, chain_id):
    url = "https://mp.trustalabs.ai/trustgo/interaction-profile"
    
    params["account"] = address
    params["chainId"] = chain_id
    response = requests.get(url, params=params, headers=headers)
    
    if response.status_code == 200:
        data = response.json().get("data", {})
        if data:
          total_ixn_cnt = data.get("total_ixn_cnt")
          total_ixn_cnt_rank = data.get("total_ixn_cnt_rank")
          total_ixn_cnt_rank_pctl = data.get("total_ixn_cnt_rank_pctl")
          total_ixn_amount = data.get("total_ixn_amount")
          total_ixn_amount_rank = data.get("total_ixn_amount_rank")
          total_ixn_amount_rank_pctl = data.get("total_ixn_amount_rank_pctl")
          active_weeks = data.get("active_weeks")
          active_weeks_rank = data.get("active_weeks_rank")
          active_weeks_rank_pctl = data.get("active_weeks_rank_pctl")
          days_gap = data.get("days_gap")
          days_gap_rank = data.get("days_gap_rank")
          days_gap_rank_pctl = data.get("days_gap_rank_pctl")
          return total_ixn_cnt, total_ixn_amount, days_gap
        else:
            print("Error: No data in the response. (Request Interaction Profile)")
            return None
    else:
        print(f"Error: {response.status_code} (Request Interaction Profile)")
        return None

def request_batch_query(address, chain_id):
    url = "https://mp.trustalabs.ai/trustgo/batch_query"
    
    params["account"] = address
    params["chainId"] = chain_id
    response = requests.get(url, params=params, headers=headers)
    
    if response.ok:
        data = response.json()["data"]
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
        print(f"Error: {response.status_code} (Request Batch Query)")
        return None



def process_wallet_address(address, chain_id):
    score_data = request_score(address, chain_id)
    interaction_data = request_interaction_profile(address, chain_id)
    batch_data = request_batch_query(address, chain_id)
    
    if score_data is None or interaction_data is None or batch_data is None:
        print(f"Error processing data for wallet address: {address}")
        return None

    return score_data, interaction_data, batch_data