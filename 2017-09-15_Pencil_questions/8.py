from pencil import *

def query03(p):
    num = p.getNumLeads()
    clen = p.getCurrentLeadLength()

    total = MAX_LEAD_LENGTH * num
    total += clen

    return total

p = Pencil(0)
print(query03(p))

p1 = Pencil(1)
print(query03(p1))

p2 = Pencil(4)
for i in range(11):
    p2.click()
print(query03(p2) == 39)