
day= input ('date:-')
mon = input('month:-')
year= input ('year:-')
monind=  int(mon) - 1
months= ['jan', 'feb', 'mar' ,'apr' ,'may','jun','jul','aug','sep','oct','nov','dec']
dayin= int(day)-1
monaph= months[monind]
prefix =['st','nd','rd'] + 17*['th'] + ['st','nd','rd'] +7 *['th']+['st']
daypre = prefix[dayin]
print('date entered is %s%s  %s %s' %(day,daypre, monaph, year))
