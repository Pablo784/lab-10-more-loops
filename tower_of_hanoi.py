def move(f,t) :
    print("Move disc from {} to {}! ".format(f,t))


def moveVia(f,v,t):
    move(f,v)
    move(v,t)
moveVia("A", "B", "C")

def hanoi(n,f,h,t) :
    if n == 0 :
        pass
    else :
        hanoi(n-1,f,t,h)
        move(f,t)
        hanoi(n-1,h,f,t)
hanoi(4, "A", "B", "C")

# For this file, I was following along the video from the class webiste that had the source code. So I type out the code and try to figure out while I was only

# getting MOVE disc from A to B! & Move disc from B to C!

# I decided to try to debugg it a little but nothing so I asked on Slack if anyone could help figure out why I was only getting those two outputs

# So a classmate came along to help me out and she told to check my alingment on lines 10 & 17 and she was right.

# the reason why I wasn't getting the output that I wanted is because the code on lines 10 & 17 weren't aligned with each other.

# ALINGMENT IS VERY IMPORTANT WHEN CODING IN PYTHON!!! 
