import sys
import argparse

# exchanges rates
BOB_USD = 1/6.96
USD_USDT = 1/0.999
USDT_BOB = 7.48

# platform commissions
WISE_BOB_TO_USD = 0.0456   # 4.56 %
ZINLI_BOB_TO_USD = 0.0199   # 1.99 %

BOB_USD_CASH = 1/7.85


rollers_from_bob_to_usd_bob = {
    'BOB_USD': BOB_USD,
    'platform_commission_bob_to_usd': None,
    'USD_USDT': USD_USDT,
    'USDT_BOB': USDT_BOB
}


rollers_from_usd_bob = {
    'USD_USDT': USD_USDT,
    'USDT_BOB': USDT_BOB,
    'BOB_USD': BOB_USD,
    'platform_commission_bob_to_usd': None,
    'USD_USDT_1': USD_USDT,
    'USDT_BOB_1': USDT_BOB,
    'BOB_USD_1': BOB_USD_CASH
}


def get_usd_from_bob_cash(amount_bob, target, rollers, iteration=1):
    roller_messages = []
    for roller_key, roller_value in rollers.items():
        amount_bob *= roller_value
        roller_messages.append(f'{roller_key}: {amount_bob:.3f}')
    possible_target_amount = amount_bob * BOB_USD_CASH

    print(f'i: {iteration}, {", ".join(roller_messages)}, BOB_USD_CASH: {possible_target_amount:.3f}')

    if possible_target_amount >= target:
        return amount_bob
    else:
        return get_usd_from_bob_cash(amount_bob, target, rollers, iteration + 1)


def get_usd_from_usd_cash(amount_usd, target, rollers, iteration=1):
    roller_messages = []
    for roller_key, roller_value in rollers.items():
        amount_usd *= roller_value
        roller_messages.append(f'{roller_key}: {amount_usd:.3f}')

    print(f'i: {iteration}, {", ".join(roller_messages)}, BOB_USD_CASH: {amount_usd:.3f}')

    if amount_usd >= target or round(amount_usd, 3) == 0:
        return amount_usd
    else:
        return get_usd_from_usd_cash(amount_usd, target, rollers, iteration + 1)


def input_args():
    parser = argparse.ArgumentParser(description=("Rollers in Bolivia"))
    parser.add_argument('-q', '--quantity',
                        type=float, help='Amount to change',
                        required=True
                        )
    parser.add_argument('-t', '--target',
                        type=float, help='target to get usd in cash',
                        required=True
                        )
    parser.add_argument('-p', '--platform',
                        type=str,
                        choices=['wise', 'zinli'],
                        required=True
                        )
    parser.add_argument('-c', '--currency_start',
                        type=str,
                        help='start from bob or from usd?',
                        choices=['usd', 'bob'],
                        required=True
                        )
    return parser.parse_args()


if __name__ == '__main__':
    args = input_args()
    target_rollers = None
    quantity = args.quantity
    target = args.target

    platform_commission = 0

    fn = None

    if args.platform == 'wise':
        platform_commission = 1 / (1 + WISE_BOB_TO_USD)
    elif args.platform == 'zinli':
        platform_commission = 1 / (1 + ZINLI_BOB_TO_USD)

    if args.currency_start == 'usd':
        fn = get_usd_from_usd_cash
        fn_kwargs = {
            'amount_usd': quantity,
            'target': target,
            'rollers': rollers_from_usd_bob
        }
    elif args.currency_start == 'bob':
        fn_kwargs = {
            'amount_bob': quantity,
            'target': target,
            'rollers': rollers_from_bob_to_usd_bob
        }
        fn = get_usd_from_bob_cash

    for k_tr in fn_kwargs['rollers']:
        if k_tr == 'platform_commission_bob_to_usd':
            fn_kwargs['rollers'][k_tr] = platform_commission

    fn(**fn_kwargs)
