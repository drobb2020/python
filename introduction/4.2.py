tmp = """
(-60, -30) REALLY COLD!
(-30, 0)   cold
0          zero
(0, 20)    perfect
(20, 40)   hot
(40, 100)  REALLY HOT!"""
print(tmp)

t = int(input())

if (t <= -30):
    print("REALLY COLD!")
if (t < 0):
    if (t > -30):
        print("Cold")
if (t == 0):
    print("Zero")
if (t > 0):
    if (t <= 20):
        print("Perfect!")
if (t >= 20):
    if (t < 40):
        print("Hot!")
if (t >= 40):
    print("REALLY HOT!")
