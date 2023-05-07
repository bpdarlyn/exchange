# Usage
```
python3 main.py -q 1500 -t 1500 -p zinli  -c usd

python3 main.py -q 3500 -t 500 -p wise  -c usd

python3 main.py -q 3500 -t 500 -p zinli  -c bob

```

## options
**-q**: quantity

**-t**: target in usd

**-p**: platform (zinli | wise)

**-c**: currency should do match with `quantity` currency allowed values (`usd` | `bob`)

## results

```bash
i: 1, USD_USDT: 1501.502, USDT_BOB: 11231.231, BOB_USD: 1613.683, platform_commission_bob_to_usd: 1582.197, USD_USDT_1: 1583.781, USDT_BOB_1: 11846.680, BOB_USD_1: 1509.131, BOB_USD_CASH: 1509.131
```

### results example 2

```bash
# python3 main.py -q 3500 -t 500 -p zinli  -c bob
i: 1, BOB_USD: 502.874, platform_commission_bob_to_usd: 493.062, USD_USDT: 493.555, USDT_BOB: 3691.793, BOB_USD_CASH: 470.292
i: 2, BOB_USD: 530.430, platform_commission_bob_to_usd: 520.080, USD_USDT: 520.601, USDT_BOB: 3894.096, BOB_USD_CASH: 496.063
i: 3, BOB_USD: 559.496, platform_commission_bob_to_usd: 548.580, USD_USDT: 549.129, USDT_BOB: 4107.484, BOB_USD_CASH: 523.246

```
the most important is the latest value `BOB_USD_CASH: 1509.131`

