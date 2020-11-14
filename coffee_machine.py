class CoffeeMachine:
    state = ''

    def __init__(self, water, milk, beans, cups, money):
        self.water = water
        self.milk = milk
        self.beans = beans
        self.cups = cups
        self.money = money

        self.choose_action()

    def choose_action(self):
        self.state = 'choosing action'
        print('Write action (buy, fill, take, remaining, exit):')

    def print_state(self):
        print(f'''
    The coffee machine has:
    {self.water} of water
    {self.milk} of milk
    {self.beans} of beans
    {self.cups} of cups
    ${self.money} of money
        ''')

    def make_espresso(self):
        if self.water < 250:
            print('Sorry, not enough water!')
        elif self.beans < 16:
            print('Sorry, not enough beans!')
        elif self.cups < 1:
            print('Sorry, not enough cups!')
        else:
            print('I have enough resources, making you a coffee!')
            self.water -= 250
            self.beans -= 16
            self.cups -= 1
            self.money += 4

    def make_latte(self):
        if self.water < 350:
            print('Sorry, not enough water!')
        elif self.milk < 75:
            print('Sorry, not enough milk!')
        elif self.beans < 20:
            print('Sorry, not enough beans!')
        elif self.cups < 1:
            print('Sorry, not enough cups!')
        else:
            print('I have enough resources, making you a coffee!')
            self.water -= 350
            self.milk -= 75
            self.beans -= 20
            self.cups -= 1
            self.money += 7

    def make_cappuccino(self):
        if self.water < 200:
            print('Sorry, not enough water!')
        elif self.milk < 100:
            print('Sorry, not enough milk!')
        elif self.beans < 12:
            print('Sorry, not enough beans!')
        elif self.cups < 1:
            print('Sorry, not enough cups!')
        else:
            print('I have enough resources, making you a coffee!')
            self.water -= 200
            self.milk -= 100
            self.beans -= 12
            self.cups -= 1
            self.money += 6

    def buy_coffee(self, selection):
        if selection == '1':
            self.make_espresso()
        elif selection == '2':
            self.make_latte()
        elif selection == '3':
            self.make_cappuccino()
        elif selection == 'back':
            pass
        self.choose_action()

    def take_money(self):
        print(f'I gave you ${self.money}')
        self.money = 0

    def process_query(self, query):
        if self.state == 'choosing action':
            if query == 'buy':
                self.state = 'choosing coffee type'
                print('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
            elif query == 'fill':
                self.state = 'filling machine water'
                print('Write how many ml of water do you want to add:')
            elif query == 'take':
                self.state = 'taking money'
                self.take_money()
                self.choose_action()
            elif query == 'remaining':
                self.state = 'printing state'
                self.print_state()
                self.choose_action()
            elif query == 'exit':
                exit()

        elif self.state == 'choosing coffee type':
            self.buy_coffee(query)

        elif self.state == 'filling machine water':
            self.water += int(query)
            self.state = 'filling machine milk'
            print('Write how many ml of milk you want to add:')
        elif self.state == 'filling machine milk':
            self.milk += int(query)
            self.state = 'filling machine beans'
            print('Write how many grams of coffee beans do you want to add:')
        elif self.state == 'filling machine beans':
            self.beans += int(query)
            self.state = 'filling machine cups'
            print('Write how many disposable cups of coffee do you want to add:')
        elif self.state == 'filling machine cups':
            self.cups += int(query)
            self.choose_action()


coffee_machine = CoffeeMachine(400, 540, 120, 9, 550)

while True:
    coffee_machine.process_query(input())