from time import sleep
from termcolor import colored
from simpleeval import simple_eval
import random


class Bot:
    
    wait = 1
    
    def __init__(self):
        self.q = ' '
        self.a = ' '
        
    def _think(self,s):
        return s
    
    def _format(self,s):
        return colored(s,'blue')

    def _say(self,s):
        sleep(Bot.wait)
        print(s)

    def run(self):
        self._say(self._format(self.q))
        self.a = input()
        self._say(self._format(self._think(self.a)))


class HelloBot(Bot):
    
    def __init__(self):
        self.q = "Hi , What is your name?"
    
    def _think(self,s):
        return f'Hello ,{s}'


class feelingBot(Bot):
    
    def __init__(self):
        self.q = 'How do you do?'
        
    def _think(self,s):
        if 'good' in s.lower() or 'fine' in s.lower():
            return "I'm good too!"
        else:
            return 'Sorry to hear that.'


class FavcolorBot(Bot):
    
    def __init__(self):
        self.q = "What is your favourite color?"
        
    def _think(self,s):
        colors = ['red','orange','yellow','green','bule','indigo','purple']
        return f'You like {s.lower()}.I like {random.choice(colors)}'


class CalculaBot(Bot):
    
    def __init__(self):
        self.q = 'Through a update,I can do calculation.Please input some arithmetic expression to try.'
        
    def _think(self,s):
        result = simple_eval(s)
        return f'Done. Result = {result}.'

    def run(self):
        while True:
            print(self._format(self.q))
            self.a = input()
            if self.a in ['x','q','exit','quit']:
                print(self._format("Bye-Bye.See you later."))
                break
            try:   
                print(self._format(self._think(self.a)))
            except:
                print(self._format("Please Input the right expression!"))
                continue

class DiceBot(Bot):
    def __init__(self,bot_current_coin,you_current_coin):
        self.q = f"let's do something difficult.Playing a dice game."
        self.p = f"You have {you_current_coin} coins,and I have {bot_current_coin} coins.\
                    \nNotice that the 'b' stand for big,the 's' stand for small and the 'd' stand for draw.\
        \nThe winner will increase 1 coin.As the game playing,if your current coin being Zero,the game is over,so do I.\
        \nLet's begin."
        self.you_current_coin = you_current_coin
        self.bot_current_coin = bot_current_coin
    
    def _win_or_lose(self,yourdice,botdice):
        if yourdice == 'b' and botdice > 7:
            return 1
        if yourdice == 's' and botdice < 7:
            return 1
        elif botdice == 7:
            return 2
        else:
            return 0

    def _think(self,n,m):
        if self._win_or_lose(n,m) == 1:
            self.bot_current_coin -= 1
            self.you_current_coin += 1
            self._say(self._format(f"You win,the dice is {m}"))
            return "Your current coin:".ljust(25,'-')+str(self.you_current_coin)+"\n"+\
                "bot current coin:".ljust(25,"-")+str(self.bot_current_coin)
        elif self._win_or_lose(n,m) == 2:
            self.bot_current_coin -= 0
            self.you_current_coin += 0
            self._say(self._format(f"Draw,the dice is {m}"))
            return "Your current coin:".ljust(25,'-')+str(self.you_current_coin)+"\n"+\
                "bot current coin:".ljust(25,"-")+str(self.bot_current_coin)
        elif self._win_or_lose(n,m) == 0:
            self.bot_current_coin += 1
            self.you_current_coin -= 1
            self._say(self._format(f"You lose,the dice is {m}"))
            return "Your current coin:".ljust(25,'-')+str(self.you_current_coin)+"\n"+\
                "bot current coin:".ljust(25,"-")+str(self.bot_current_coin)

    def run(self):
        self._say(self._format(self.q))
        self._say(self._format(self.p))
        while self.bot_current_coin != 0 and self.you_current_coin != 0:
            self.botdice  = random.randrange(2,13)
            self._say(self._format("What's your bet?"))
            self.yourdice = input()
            self._say(self._format(self._think(self.yourdice,self.botdice)))
        self._say(self._format('Game Over.'))
            
class Garfield:
    
    def __init__(self,wait = 1):
        Bot.wait = wait
        self.bots= []
        
    def add(self,bot):
        self.bots.append(bot)
        
    def _prompt(self,s):
        print(s)
        print()
        
    def run(self):
        self._prompt('This is Garfield dialog system. Let\'s talk.')
        for bot in self.bots:
            bot.run()


# class Garfield:
#     def __init__(self,wait = 1):
#         Bot.wait = wait
#         self.bots= []
        
#     def add(self,bot):
#         self.bots.append(bot)
        
#     def _prompt(self,s):
#         print(s)
#         print()

#     def run(self):
#         self._prompt('This is Garfield dialog system. Let\'s talk.')
#         # list = ['HelloBot','feelingBot','FavcolorBot']
#         if self.mode == 'list':
#             self._run_list_mode()
#         else:
#             self._run_default_mode()

#     def _run_default_mode(self):
#         for bot in self.bots:
#             bot.run()

#     def _run_list_mode(self):
#         for index,bot in enumerate(self.bots):
#             print(f"{index + 1}. {type(bot).__name__}")

#         bot_index = 0
#         bot_count = len(self.bots)
#         input_prompt = f"Enter a number to choose your friend (1-{bot_count}):"
#         while True:
#             try:
#                 bot_index = int(input(input_prompt))
#             except ValueError:
#                 print(f"Not a valid number.Please reTry.")
#                 continue
#             if bot_index < 1 or bot_index > bot_count:
#                 print(f"You can only choose between 1-{bot_count}")
#                 continue
#             else:
#                 break
#         bot = self.bots[bot_index - 1]
#         bot.run()


garfield = Garfield()

garfield.add(HelloBot())
garfield.add(feelingBot())
garfield.add(FavcolorBot())
garfield.add(CalculaBot())
garfield.add(DiceBot(2,2))
garfield.run()