import re
mail="chenhuanying@leedarson.com"
# mail="bill.gates@microsoft.com"
comp1=re.compile(r'^\w+\@\w+\.com$|\w+.\w+\@\w+\.com$')
print(comp1.match(mail))


#案例2
comp2 = re.compile(r'(<\w+\s\w+>)\s(\w+)@(\w+.\w+)')
m2 = comp2.match(r'<Tom Paris> tom@voyager.org')
print(m2.groups())