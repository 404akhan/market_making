Code in `osnova.ipynb`

`Simulator` class - Market simulator based on crypty (bitcoin, ethereum) market data. 
It has API to place and cancel order, process them with predefined latency, executes them as market orders, in case of
imediate match and places limit order otherwise. Every tick our simulator goes through new market data, and 
updates our limit orders if they get processed.

`Strategy` class - Basic market making strategy that can place orders at best ask or bid price, calculate position, balance
and PNL. Cancels old orders in case they get intact using saved order_id from the Simulator. 

`load_md_from_file` function - Prepares market data. Merges market orderbook snapshots with real time market order flows.
This is used by Simulator to determine execution of trades made by Strategy.