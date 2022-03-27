<font size=3>**xlm_amm**</font>
 Automated Market Maker on Stellar Network (XLM)

**Description:**
The end goal of this project is to provide liquidity to the stellar network while simultaneously make money in the process.

order_book.py will be used to query the most popular liquidity pool to try and beat their exchange rate to increase my own pool's usage.
price.py is another reference point using CoinMarketCap's price of XLM.
acc_balance.py is used to verify transactions and balances.
buyer.py and seller.py will be used to balance the two assets in the liquidity pool. It's undetermined how they will be used to turn a profit.

Installation:

**Roadmap:**
 1) Set up buyer and seller bots on cron schedule within CMC limit of 300 API calls a day
 2) Implement market making algo. Potentially taking advantage of open source [kelp](https://github.com/stellar/kelp)
