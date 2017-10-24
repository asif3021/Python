def cheeseshop(kind, *argument, **keywords):
    print("-- Do you have any", kind,"??")
    print("-- I'm sorry, we're all out of",kind)
    for arg in argument:
        print(arg)
    print("-"*40)
    for kw in keywords:
        print(kw,":",keywords[kw])




# cheeseshop("Limburger","It's very runny,sir",
# 	   "it's really VERY runny,sir",
# 	   shopkeeper="Michael Palin",
# 	   Clint="John Cleese",
# 	   Sketch="Cheese shop sketch")
