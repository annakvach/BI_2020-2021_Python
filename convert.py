print("Converter program. ")
print("Based on '...Для конвертера можно взять любые величины, но выберите что-то интереснее метров и километров...' and D&D 5e. ")
print("(https://5thsrd.org/adventuring/equipment/coins/)")
print()
print("You have tons of coins that you earned in dangerous adventures and you want to exchange them.")
print("So you are in bank.")
print("(Goblin Bankerycharm pepe may be disrespectful if he doesn't know what to do.)")
print()

# make dictionary for coin exchange
coin_dict = {
    'coppertosilver': '10',
    'coppertoelectrum': '50',
    'coppertogold': '100',
    'coppertoplatinum': '1000',
    'silvertocopper': '0.1',
    'silvertoelectrum': '5',
    'silvertogold': '10',
    'silvertoplatinum': '100',
    'electrumtocopper': '0.02',
    'electrumtosilver': '0.5',
    'electrumtogold': '2',
    'electrumtoplatinum': '20',
    'goldtocopper': '0.01',
    'goldtosilver': '0.1',
    'goldtoelectrum': '0.5',
    'goldtoplatinum': '10',
    'platinumtocopper': '0.001',
    'platinumtosilver': '0.01',
    'platinumtoelectrum': '0.05',
    'platinumtogold': '0.1',
}


# for type control
def isDigit(x):
    try:
        float(x)
        return True
    except ValueError:
        return False


# cycle start
start = input("Start? (y/n) ")
print()
while start == "y":
    print()
    goblin_or = input("Do you want to talk with goblin? (y/n) ")
    print()
    # interact with goblin or not
    if goblin_or == "y":
        print("Goblin Banker: Do you want to exchange a specific denomination (1)")
        print("or simply exchange all your savings for coins of a larger denomination?? (2)")
        print()
        choose_exchange = input("Input 1 or 2 to choose the type of operation: ")
        # exchange mode = exchange_1
        if choose_exchange == "1":
            denomination_1 = input(
                'Goblin Banker: What denomination of coins do you want to exchange? (copper/silver/electrum/gold/platinum): ')
            # choose first denomination
            if (denomination_1 == "copper") or (denomination_1 == "silver") or (denomination_1 == "electrum") or (
                    denomination_1 == "gold") or (denomination_1 == "platinum"):
                n_den_1 = input('Goblin Banker: How many ' + denomination_1 + 's' + ' ' + 'do you want to exchange? ')
                # CHECK amount of coins
                if float(n_den_1) > 0:
                    # Check amount of coins
                    if isDigit(n_den_1):
                        denomination_2 = input(
                            'Goblin Banker: And what the denomination of the coins do you want to get? (copper/silver/electrum/gold/platinum): ')
                        # CHECK second denomination
                        if denomination_1 == denomination_2:
                            print(
                                "Goblin Banker: Go away weirdo! These are the same denominations! Do not waste my time! ")
                        # create a key for dictionary
                        elif (denomination_2 == "copper") or (denomination_2 == "silver") or (
                                denomination_2 == "electrum") or (denomination_2 == "gold") or (
                                denomination_2 == "platinum"):
                            for_dic = str(denomination_1 + 'to' + denomination_2)
                            # if all is ok - catch a value from dictionary
                            value_dic = coin_dict.get(for_dic)
                            # equal exchange
                            if (int(float(n_den_1) / float(value_dic))) > 1:
                                print('Goblin Banker: I can give you', ' ', float(n_den_1) / float(value_dic), ' ',
                                      denomination_2, 's', sep="")
                                # exchange with the remainder
                                if (int(float(n_den_1) % float(value_dic))) > 1:
                                    print('Goblin Banker: But keep your pitiful', ' ',
                                          (float(n_den_1) % float(value_dic)), ' ', denomination_1, 's', ' ',
                                          'for yourself..', sep="")
                            # negative numbers or just not enough money
                            else:
                                print("Goblin Banker: HAHAHAHA! Come back when you have more coins!")
                        # wrong input in denomination_2
                        else:
                            print("Goblin Banker: What the hell are ", denomination_2, "s", "?!!", sep="")
                            print("Goblin Banker: I am not a ", denomination_2, "s", " seller", "!", sep="")
                    # wrong input in n_den_1
                    else:
                        print("Goblin Banker: What the hell are ", n_den_1, "s", "?!! Learn numbers!!!", sep="")
                else:
                    print("Goblin Banker: HAHAHAHA! Come back when you have more coins!")
            # wrong input in denomination_1
            else:
                print("Goblin Banker: What the hell are ", denomination_1, "s", "?!!", sep="")
                print("Goblin Banker: I am not a ", denomination_1, "s", " seller", "!", sep="")
        # exchange mode = exchange_2
        elif choose_exchange == "2":
            start_2 = input("Do you want to exchange all your savings for coins of a larger denomination? (y/n)")
            while start_2 == "y":
                # input for exchange_2 and check is it number
                # my_copper_input
                my_copper_input = input("How much coppers do you have? : ")
                if isDigit(my_copper_input) and (float(my_copper_input) >= 0):
                    my_copper = int(my_copper_input)
                else:
                    print("Goblin Banker: What the hell are ", my_copper_input, "s",
                          "?!! Learn numbers!!! And input only positive values!", sep="")
                    continue
                # my_silver_input
                my_silver_input = input("How much silvers do you have? : ")
                if isDigit(my_silver_input) and (float(my_silver_input) >= 0):
                    my_silver = int(my_silver_input)
                else:
                    print("Goblin Banker: What the hell are ", my_silver_input, "s",
                          "?!! Learn numbers!!! And input only positive values!", sep="")
                    continue
                # my_electum_input
                my_electum_input = input("How much electrums do you have? : ")
                if isDigit(my_electum_input) and (float(my_electum_input) >= 0):
                    my_electum = int(my_electum_input)
                else:
                    print("Goblin Banker: What the hell are ", my_electum_input, "s",
                          "?!! Learn numbers!!! And input only positive values!", sep="")
                    continue
                # my_gold_input
                my_gold_input = input("How much golds do you have? : ")
                if isDigit(my_gold_input) and (float(my_gold_input) >= 0):
                    my_gold = int(my_gold_input)
                else:
                    print("Goblin Banker: What the hell are ", my_gold_input, "s",
                          "?!! Learn numbers!!! And input only positive values!", sep="")
                    continue
                # my_platinum_input
                my_platinum_input = input("How much platinums do you have? : ")
                if isDigit(my_platinum_input) and (float(my_platinum_input) >= 0):
                    my_platinum = int(my_platinum_input)
                else:
                    print("Goblin Banker: What the hell are ", my_platinum_input, "s",
                          "?!! Learn numbers!!! And input only positive values!", sep="")
                    continue

                my_coins: int = my_copper + my_silver * 10 + my_electum * 50 + my_gold * 100 + my_platinum * 1000

                Platinums = 0
                Golds = 0
                Electums = 0
                Silvers = 0

                while my_coins >= 10:
                    if my_coins // 1000 >= 1:
                        Platinums += my_coins // 1000
                        my_coins -= Platinums * 1000
                    if (my_coins // 100) >= 1:
                        Golds += my_coins // 100
                        my_coins -= Golds * 100
                    if my_coins // 50 >= 1:
                        Electums += my_coins // 50
                        my_coins -= Electums * 50
                    if my_coins // 10 >= 1:
                        Silvers += my_coins // 10
                        my_coins -= Silvers * 10

                print("I can give you: ")
                print("Platinums: ", Platinums)
                print("Golds: ", Golds)
                print("Electums: ", Electums)
                print("Silvers: ", Silvers)
                print("Coppers: ", my_coins)

                start_2 = input("Goblin Banker: Do you want to do it again (y/n)")
    elif goblin_or == "n":
        print("Goodbye!")
        start = input("Do you want to continue? (y/n) ")
else:
    print("Goodbye!")
