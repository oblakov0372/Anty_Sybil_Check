import csv
import json

def save_to_json(data, chain_name):
    filename = f'all_data_{chain_name}.json'
    with open(filename, 'w') as jsonfile:
        json.dump(data, jsonfile, indent=2)

def save_to_csv(data, chain_name):
    filename = f'all_data_{chain_name}.csv'

    with open(filename, 'w', newline='') as csvfile:
        fieldnames = [
            'wallet_address',
            'score',
            'rank',
            'tenure',
            'monetary',
            'frequency',
            'diversity',
            'identity',
            'contracts_count',
            'protocols_count',
            'total_ixn_cnt',
            'total_ixn_amount',
            'days_gap',
            'usdValue',
            'activeDays',
            'activeWeeks',
            'activeMonths',
            'gas_spent'
        ]

        writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
        writer.writeheader()

        for entry in data:
            writer.writerow({
                'wallet_address': entry['wallet_address'],
                'score': entry['score_data']['score'],
                'rank': entry['score_data']['rank'],
                'tenure': entry['score_data']['tenure'],
                'monetary': entry['score_data']['monetary'],
                'frequency': entry['score_data']['frequency'],
                'diversity': entry['score_data']['diversity'],
                'identity': entry['score_data']['identity'],
                'contracts_count': entry['score_data']['contracts_count'],
                'protocols_count': entry['score_data']['protocols_count'],
                'total_ixn_cnt': entry['interaction_data']['total_ixn_cnt'],
                'total_ixn_amount': entry['interaction_data']['total_ixn_amount'],
                'days_gap': entry['interaction_data']['days_gap'],
                'usdValue': entry['batch_data']['usdValue'],
                'activeDays': entry['batch_data']['activeDays'],
                'activeWeeks': entry['batch_data']['activeWeeks'],
                'activeMonths': entry['batch_data']['activeMonths'],
                'gas_spent': entry['batch_data']['gas_spent']
            })

def get_empty_data(wallet_address):
    return {
        'score_data': {
        'score': None,
        'rank': None,
        'tenure': None,
        'monetary': None,
        'frequency': None,
        'diversity': None,
        'identity': None,
        'contracts_count': None,
        'protocols_count': None,
    },
    'interaction_data': {
        'total_ixn_cnt': None,
        'total_ixn_amount': None,
        'days_gap': None,
    },
    'batch_data': {
        'usdValue': None,
        'activeDays': None,
        'activeWeeks': None,
        'activeMonths': None,
        'gas_spent': None,
    },
    'wallet_address': wallet_address  
    }

def get_correct_data(score_data, interaction_data, batch_data,wallet_address):
    return {
        'score_data': {
            'score': score_data[0],
            'rank': score_data[1],
            'tenure': score_data[2],
            'monetary': score_data[3],
            'frequency': score_data[4],
            'diversity': score_data[5],
            'identity': score_data[6],
            'contracts_count': score_data[7],
            'protocols_count': score_data[8],
        },
        'interaction_data': {
            'total_ixn_cnt': interaction_data[0],
            'total_ixn_amount': interaction_data[1],
            'days_gap': interaction_data[2],
        },
        'batch_data': {
            'usdValue': batch_data[0],
            'activeDays': batch_data[1],
            'activeWeeks': batch_data[2],
            'activeMonths': batch_data[3],
            'gas_spent': batch_data[4],
        },
        'wallet_address': wallet_address  
    }