<font size=3>**xlm_amm**</font>
 Automated Market Maker on Stellar Network (XLM)

**Description:**
The end goal of this project is to provide liquidity to the stellar network while simultaneously make money in the process.

-order_book.py will be used to query the most popular liquidity pool to try and beat their exchange rate to increase my own pool's usage.

-price.py is another reference point using CoinMarketCap's price of XLM.

-acc_balance.py is used to verify transactions and balances.

-buyer.py will validate the trading account contains assets, retrieve the order_book, and attempt to beat the current exchange rate by depositing pool shares for liquidity.

-seller.py will be called on a cron scheduled time period or when the trading account has no assets to deposit. It will check if the exchange rates used by the buying bot are lower than the current exchange rate for the two assets. If the exchange rate for the two assets has increased by a pre-determined percent, it will pull all of the pool shares to replenish the trading account's funds.
    
    -Should implement a sqlite db to record the buyer.py exchange rates to be used by seller.py

-liquidity_pool.py is how the liquidity pool is initialized and how buyer.py and seller.py grab its ID.

-test_acc.py was used to generate test account keypairs

**Installation:**

pip install -r requirements.txt

**Roadmap:**
 1) Set up buyer and seller bots on cron schedule within CMC limit of 300 API calls a day
 2) Implement market making algo. Potentially taking advantage of open source [kelp](https://github.com/stellar/kelp)
