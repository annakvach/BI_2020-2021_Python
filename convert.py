print("Introduction. converter in dnd style .....")
print("You are in bank. You must currency exchange because dragon")

coin_dict={
    'coppertosilver':'10',
    'coppertoelectrum':'50',
    'coppertogold':'100',
    'coppertoplatinum':'1000',
    'silvertocopper':'0.1',
    'silvertoelectrum':'5',
    'silvertogold':'10',
    'silvertoplatinum':'100',
    'electrumtocopper':'0.02',
    'electrumtosilver':'0.5',
    'electrumtogold':'2',
    'electrumtoplatinum':'20',
    'goldtocopper':'0.01',
    'goldtosilver':'0.1',
    'goldtoelectrum':'0.5',
    'goldtoplatinum':'10',
    'platinumtocopper':'0.001',
    'platinumtosilver':'0.01',
    'platinumtoelectrum':'0.05',
    'platinumtogold':'0.1',
}
#choose between: you can exchange coins of one denomination for another///you can exchange small coins for larger ones//

# you can exchange coins of one denomination for another/
denomination_1 = input('What denomination of the coins do you want to exchange? (copper/silver/electrum/gold/platinum): ')
n_den_1 = input('How many ' + denomination_1 + 's' + ' ' + 'do you want to exchange? ')
denomination_2 = input('And what the denomination of the coins do you want to get? (Copper/Silver/Electrum/Gold/Platinum): ')

for_dic = str(denomination_1 + 'to' + denomination_2)

if (dic.get(for_dic) != None):
    value_dic = dic.get(for_dic)
    print('You will get', ' ', int(n_den_1) / int(value_dic), ' ', denomination_2, 's', sep="")



    print('This denomination is unknown to us.')
elif (denomination_1 == denomination_2):
    print('This is a joke? It does not make sense. Try again.')

