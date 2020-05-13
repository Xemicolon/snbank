check_account = {'Account Number': 123456777}

customer_details = [[{
    "name": [
        {
            'Account Name': 'Light',
            'Account Number': 123456777,
            'Opening Balance': 200,
            'Account Type': 'Savings',
            'Account Email': 'ok@ok.com',
        }
    ],
}, ], ]

for keys in customer_details:
    for key in keys.keys():
        for ky in key[key]:
            if check_account['Account Number'] in ky.values():
                print(f' good')
