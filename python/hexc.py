from conversion import Conversion

operators = None
nums = None

print('--help for list of commands')

def getcommand():
    global operators, nums
    usercommand = input()
    usercommandsplit = usercommand.split()
    operators = usercommandsplit[0]
    del usercommandsplit[0]
    nums = ' '.join(usercommandsplit)
    conv()
    
def conv():
    global operators, nums
    op = operators
    k = Conversion(nums)
    if op == '-bd':
        print(k.bd())
    elif op == '-bh':
        print(k.bh())
    elif op == '-db':
        print(k.db())
    elif op == '-dh':
        print(k.dh())
    elif op == '-hb':
        print(k.hb())
    elif op == '-hd':
        print(k.hd())
    else:
        print('error')

while True:
    getcommand()