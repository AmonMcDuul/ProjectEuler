# In the United Kingdom the currency is made up of pound (£) and pence (p). There are eight coins in general circulation:
#     1p, 2p, 5p, 10p, 20p, 50p, £1 (100p), and £2 (200p).
# It is possible to make £2 in the following way:
#     1×£1 + 1×50p + 2×20p + 1×5p + 1×2p + 3×1p
# How many different ways can £2 be made using any number of coins?

result = 0

for tweehonderd in range(2):
    if(tweehonderd*200) > 200:
        break
    for honderd in range(3):
        if(tweehonderd*200+honderd*100) > 200:
            break
        for vijftig in range(5):
            if(tweehonderd*200+honderd*100+vijftig*50) > 200:
                break
            for twintig in range(11):
                if(tweehonderd*200+honderd*100+vijftig*50+twintig*20) > 200:
                    break
                for tien in range(21):
                    if(tweehonderd*200+honderd*100+vijftig*50+twintig*20+tien*10) > 200:
                        break
                    for vijf in range(41):
                        if(tweehonderd*200+honderd*100+vijftig*50+twintig*20+tien*10+vijf*5) > 200:
                            break
                        for twee in range(101):
                            if(tweehonderd*200+honderd*100+vijftig*50+twintig*20+tien*10+vijf*5+twee*2) > 200:
                                break
                            for een in range(201):
                                if(tweehonderd*200+honderd*100+vijftig*50+twintig*20+tien*10+vijf*5+twee*2+een*1) > 200:
                                    break
                                if(tweehonderd*200+honderd*100+vijftig*50+twintig*20+tien*10+vijf*5+twee*2+een*1) == 200:
                                    result+=1
print(result)