#Inputs
stock_price = float(raw_input("Stock price: "))
strike_price = float(raw_input("Option strike price: "))
a,b = map(float,raw_input("Call price and volume, separated by a comma: ").split(","))
c,d = map(float,raw_input("Put price and volume, separated by a comma: ").split(","))

#Cost
initial_outlay = ((a*100) * b) + ((c*100) * d)

#Breakeven
up_break = strike_price + (initial_outlay / 100)
dn_break = strike_price - (initial_outlay / 100)
print "Cost: ", initial_outlay
print "Upside breakeven: ", up_break
print "Downside breakeven: ", dn_break

#Spread
print "Spread: ", (initial_outlay * (b+d)) / 100

#Keep cost and spread down, % spread
print "Upside delta: %s%%" % (round((up_break - stock_price) / stock_price,4)*100)
print "Downside delta: %s%%" % (round((dn_break - stock_price) / stock_price,4)*100)
