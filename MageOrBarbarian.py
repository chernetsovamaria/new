class Fighter:
    def attack(self):
        print(f'{self._class} attacks!')


class Barbarian(Fighter):
    def __init__(self, name):
        self.name = name
        self._class = 'barbarian'


class Mage(Fighter):
    def __init__(self, name):
        self.name = name
        self._class = 'mage'


b_name = input('Your barbarian name: ')
m_name = input('Your mage name: ')
barbarian = Barbarian(b_name)
mage = Mage(m_name)

process = True
while process:
    ch = input('Choose your character to attack or type exit: '.lower())
    if ch == barbarian._class or ch == barbarian.name:
        barbarian.attack()
    elif ch == mage._class or ch == mage.name:
        mage.attack()
    elif ch == 'exit':
        process = False
