import kivy

kivy.require("1.10.0")
from kivy.app import App
from kivy.uix.button import Button
from kivy.lang import Builder
from kivy.uix.boxlayout import BoxLayout
import random


# Main
# Builds the kv file instead of having it separate
class Main(App):
    def build(self):
        Builder.load_string(
            """
            Container:
            #Container holds all the other layouts
            <Container>:
                id: contain
                orientation: "vertical"
                #pos_hint: {'center_y': 0.5, 'center_x': 0.5}
                #size_hint_y: None
                #height: 0.5625 * root.width
                StartMenu
            
            <StartMenu>:
                orientation: "vertical"
                Button:
                    text: "Начало квеста"
                    on_press: root.goto_coin_menu()
                Button:
                    text: "Выход"
                    on_press: root.quit_game()
            
            <MenuOne>:
                orientation: "vertical"
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0.5
                Label:
                    text:"Вы,родились в восемнадцатом веке в небольшом прибрежной колонии в Северной Америке.\
                    С самого детства вы мечтали отправиться в море.Однако вам не хотелось становиться простым матросом\
                    вы хотели стать капитаном своего собственного корабля!\
                    Проснувшись утром в родительской лачуге в приморском городке Тихий на территории Испанской Флориды\
                    вы твердо вознамерились в ближайшее время взять судьбу в свои руки."
                    text_size:(600, None)
                    sep:''
            
            
                Button:
                    size_hint_y: 0.2
                    text: "Продолжить"
                    font_size: "30sp"
                    on_press: root.YrOne()
            
                Button:
                    size_hint_y: 0.1
                    text: "Back"
                    on_press: root.goto_start_menu()
            
            <MenuTwo>:
                orientation: "vertical"
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0.5
                Label:
                    text:"Прогуливаясь по улицам города,вы заметили лежащий на дороге кошелек с несколькими золотыми монетами.\
                    Возможно,его кто-то обронил совсем недавно-хотите ,осмотреться в поисках владельца кошеля или заберете его себе ?\"
                    text_size:(600, None)
                    sep:''
            
                Button:
                    size_hint_y: 0.2
                    text: "Попытаться найти владельца кошелька"
                    font_size: "30sp"
                    on_press: root.YrTwo()
            
                Button:
                    size_hint_y: 0.2
                    text: "Оставить кошель с золотыми монетами себе"
                    font_size: "30sp"
                    on_press: root.PodYrTwo()
                Button:
                    size_hint_y: 0.1
                    text: "Back"
                    on_press: root.goto_start_menu()
            
            <MenuTwoPod1>:
                orientation: "vertical"
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0.5
                Label:
                    text:"Вы осмотрелись,попытавшись найти хозяина кошелька.\
                    В следующий миг к вам подошел мужчина неприятной внешности с покрытым шрамами лицом\
                    ”Я смотрю,ты мое золотишко присвоить себе решил?Давай его живо сюда!” - Хотите отдать кошель с пятью монетами ?"
                    text_size:(600, None)
                    sep:''
            
                Button:
                    size_hint_y: 0.2
                    text: "Да"
                    font_size: "30sp"
                    on_press: root.YrThree1()
            
                Button:
                    size_hint_y: 0.2
                    text: "Нет"
                    font_size: "30sp"
                    on_press: root.PodYrThree1()
                Button:
                    size_hint_y: 0.1
                    text: "Back"
                    on_press: root.StartMenu()
            
            <MenuTwoPod2>:
                orientation: "vertical"
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0.5
                Label:
                    text:"Не став искать хозяина пропажи,вы убрали кошель в карман и быстро зашагали прочь.\
                    В следующий миг к вам подошел мужчина неприятной внешности с покрытым шрамами лицом\
                    ”Я смотрю,ты мое золотишко присвоить себе решил?Давай его живо сюда!” - Хотите отдать кошель с пятью монетами ?"
                    text_size:(600, None)
                    sep:''
            
                Button:
                    size_hint_y: 0.2
                    text: "Да"
                    font_size: "30sp"
                    on_press: root.YrThree()
            
                Button:
                    size_hint_y: 0.2
                    text: "Нет"
                    font_size: "30sp"
                    on_press: root.PodYrThree()
                Button:
                    size_hint_y: 0.1
                    text: "Back"
                    on_press: root.StartMenu()
            
            <MenuTwoPod1Da>:
                orientation: "vertical"
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0.5
                Label:
                    text:"Вы протянули мужчине найденный кошель.\
                    Выхватив находку из ваших рук,бандит с силой толкнул вас ,повалив на землю,и скрылся в толпе.\
                    Поднявшись на ноги,вы обнаружили,что мужчина обронил из кошеля одну монету"
                    text_size:(600, None)
                    sep:''
            
                Button:
                    size_hint_y: 0.2
                    text: "Продолжить"
                    font_size: "30sp"
                    on_press: root.TwoPod1Da1()
            
            
                Button:
                    size_hint_y: 0.1
                    text: "Back"
                    on_press: root.StartMenu()
            <MenuTwoPod1Net>:
                orientation: "vertical"
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0
                Label:
                    text:"Мужчина стоявший перед вами резким движением правой руки достал из кармана нож\
                    и пырнул вас в живот. Уже через 20 секунд вы лежали на земле с колотым ранением,из которого сочилась кровь"
                    text_size:(600, None)
                    sep:''
            
            <MenuTwoPod2Da>:
                orientation: "vertical"
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0.5
                Label:
                    text:"Вы протянули мужчине найденный кошель.\
                    Выхватив находку из ваших рук,бандит с силой толкнул вас ,повалив на землю,и скрылся в толпе.\
                    Поднявшись на ноги,вы обнаружили,что мужчина обронил из кошеля одну монету"
                    text_size:(600, None)
                    sep:''
            
                Button:
                    size_hint_y: 0.2
                    text: "Продолжить"
                    font_size: "30sp"
                    on_press: root.YrThree()
            
            
                Button:
                    size_hint_y: 0.1
                    text: "Back"
                    on_press: root.StartMenu()
            <MenuTwoPod2Net>:
                orientation: "vertical"
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0
                Label:
                    text:"Мужчина стоявший перед вами резким движением правой руки достал из кармана нож\
                    и пырнул вас в живот. Уже через 20 секунд вы лежали на земле с колотым ранением,из которого сочилась кровь"
                    text_size:(600, None)
                    sep:''
            
            <MenuSob2>:
                orientation: "vertical"
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0.5
                Label:
                    text:"Вы протянули мужчине найденный кошель.\
                    Выхватив находку из ваших рук,бандит с силой толкнул вас ,повалив на землю,и скрылся в толпе.\
                    Поднявшись на ноги,вы обнаружили,что мужчина обронил из кошеля одну монету"
                    text_size:(600, None)
                    sep:''
            
                Button:
                    size_hint_y: 0.2
                    text: "Продолжить"
                    font_size: "30sp"
                    on_press: root.SobIst2()
            
            
            
            
            <MenuSob2_next>:
                orientation: "vertical"
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0
                Label:
                    text:" Пройдя чуть дальше по площади вы заметили как к вам подошел нищий калека\
                    чья хромота явно была притворной:”Не поделитесь с бедняком монеткой?” - нищий протянул вам свою сухую ладонь"
                    text_size:(600, None)
                    sep:''
            
                Button:
                    size_hint_y: 0.2
                    text: "Помощь нищему"
                    font_size: "30sp"
                    on_press: root.SobIst2_nextPod1()
            
                Button:
                    size_hint_y: 0.2
                    text: "Пройти мимо"
                    font_size: "30sp"
                    on_press: root.SobIst2_nextPod2()
            
            <MenuSob2_nextPod1>:
                orientation: "vertical"        
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0
                Label:
                    text:"Когда вы отдали последнюю монету попрошайке,он рассыпался в благодарностях и быстро ретировался." 
                    text_size:(600, None)
                    sep:''
            
                Button:
                    size_hint_y: 0.2
                    text: "Продолжить"
                    font_size: "30sp"
                    on_press: root.SobIst2_nextPod1()
            
            <MenuSob2_nextPod2>:
                orientation: "vertical"
            
                BoxLayout:
                    orientation: "vertical"
                Label:
                    text:"Вы не стали отдавать последнюю монету попрошайке,который тут же разразился бранью.\
                    Проходящий мимо гвардеец с размаху отвесил калеке подзатыльник,заставив быстро ретироваться,и повернулся к вам:”Правильно!Нечего этих актеров подкармливать!”"
                    text_size:(600, None)
                    sep:''
            
                Button:
                    size_hint_y: 0.2
                    text: "Продолжить"
                    font_size: "30sp"
                    on_press: root.SobIst2_nextPod2()
            
            
            <MenuSob3>:
                orientation: "vertical"
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0.5
                Label:
                    text:"И вот подошло время подумать о своем будущем капитана.Для начала вам нужно набрать экипаж,который будет готов вас поддержать в любой момент.\
                    Пройдя по площади чуть дальше вы зашли в один из местных баров.\
                    Присев за одну из барных стоек,вы заметили знакомого пьянчугу. Вы решили угостить его бокалом хорошего рома. Через некоторое время ваш знакомый повернулся к вам и уверенно сказал….Если ты когда-нибудь обзаведешься кораблем,я непременно хочу отправиться в плавание с тобой!"
                    text_size:(600, None)
                    sep:''
            
                Button:
                    size_hint_y: 0.2
                    text: "Продолжить"
                    font_size: "30sp"
                    on_press: root.SobIst3()
            
            
            
            
            <MenuSob4>:
                orientation: "vertical"
                BoxLayout:
                    orientation: "vertical"
                    size_hint_y: 0
                Label:
                    text:"Вы немного передохнули и забрали из своего тайника горсть накопленных монет.Пора отправляться навстречу приключениям ! "
                    text_size:(600, None)
                    sep:''
            
                Button:
                    size_hint_y: 0.2
                    text: "Навстречу приключениям!"
                    font_size: "30sp"
                    on_press: root.SobIst2_nextPod1()
            
            """)
        global root
        root = Container()
        return root


# The primary gui piece that holds all the other gui pieces
class Container(BoxLayout):
    pass


# The first menu the user sees
class StartMenu(BoxLayout):
    def quit_game(self):
        App.get_running_app().stop()

    def goto_coin_menu(self):
        root.clear_widgets()
        root.add_widget(MenuOne())


# The bulk of the coin flip program, this is where stuff happens
# Flipping more than a million coins can be laggy
class MenuOne(BoxLayout):
    def goto_start_menu(self):
        root.clear_widgets()
        root.add_widget(StartMenu())

    def YrOne(self):
        root.clear_widgets()
        root.add_widget(MenuTwo())
        print("ПодУровень1")


class MenuTwo(BoxLayout):
    def goto_start_menuTwo(self):
        root.clear_widgets()
        root.add_widgets(MenuOne())

    def YrTwo(self):
        root.clear_widgets()
        root.add_widget(MenuTwoPod1())
        print('ПодУровень3')

    def PodYrTwo(self):
        root.clear_widgets()
        root.add_widget(MenuTwoPod2())
        print('ПодУровень4')


#####################################################################
class MenuTwoPod1(BoxLayout):
    def goto_start_menuThree(self):
        root.clear_widgets()
        root.add_widgets(MenuTwo())

    def YrThree1(self):
        root.clear_widgets()
        root.add_widget(MenuTwoPod1Da())
        print("ПодУровень5")

    def PodYrThree1(self):
        root.clear_widgets()
        root.add_widget(MenuTwoPod1Net())
        print("ПодУровень6")


class MenuTwoPod2(BoxLayout):
    def goto_start_menuThree(self):
        root.clear_widgets()
        root.add_widgets(MenuTwo())

    def YrThree(self):
        root.clear_widgets()
        root.add_widget(MenuTwoPod2Da())
        print("ПодУровень7")

    def PodYrThree(self):
        root.clear_widgets()
        root.add_widget(MenuTwoPod2Net())
        print("ПодУровень8")


#####################################################################
class MenuTwoPod1Da(BoxLayout):
    def goto_start_menuThree(self):
        root.clear_widgets()
        root.add_widgets(MenuTwoPod1())

    def TwoPod1Da1(self):
        root.clear_widgets()
        root.add_widget(MenuSob2())
        print("MenuTwoPod1 da12 ")

    def TwoPod2Da1(self):
        root.clear_widgets()
        root.add_widget(MenuSob2())
        print("MenuTwoPod1 neteff1 ")


class MenuTwoPod1Net(BoxLayout):
    def goto_start_menuThree(self):
        root.clear_widgets()
        root.add_widgets(MenuTwoPod1())

    def TwoPod1Net1(self):
        root.clear_widgets()
        root.add_widget(MenuTwoPod1Net())
        print("MenuTwoPod1 net1")


#####################################################################
class MenuTwoPod2Da(BoxLayout):
    def goto_start_menuThree(self):
        root.clear_widgets()
        root.add_widgets(MenuTwoPod1())

    def YrThree(self):
        root.clear_widgets()
        root.add_widget(MenuSob2())
        print("MenuTwoPod1 da1 ")

    def PodYrThree(self):
        root.clear_widgets()
        root.add_widget(MenuTwoPod1Da())
        print("MenuTwoPod1 da2 ")


class MenuTwoPod2Net(BoxLayout):
    def goto_start_menuThree(self):
        root.clear_widgets()
        root.add_widgets(MenuTwoPod1())

    def YrThree(self):
        root.clear_widgets()
        root.add_widget(MenuSob2())
        print("MenuTwoPod1 net1")

    def PodYrThree(self):
        root.clear_widgets()
        root.add_widget(MenuTwoPod1Net())
        print("MenuTwoPod1 net2")


class MenuSob2(BoxLayout):
    def goto_start_menuThree(self):
        root.clear_widgets()
        root.add_widgets(MenuTwoPod1Da())

    def SobIst2(self):
        root.clear_widgets()
        root.add_widget(MenuSob2_next())
        print("Sobitie2")


#####################################################################
class MenuSob2_next(BoxLayout):
    def goto_start_menuThree(self):
        root.clear_widgets()
        root.add_widgets(MenuSob2())

    def SobIst2_nextPod1(self):
        root.clear_widgets()
        root.add_widget(MenuSob2_nextPod1())
        print("SobitiePod1")

    def SobIst2_nextPod2(self):
        root.clear_widgets()
        root.add_widget(MenuSob2_nextPod2())
        print("SobitiePod2")


class MenuSob2_nextPod1(BoxLayout):
    def goto_start_menuThree(self):
        root.clear_widgets()
        root.add_widgets(MenuSob2_next())

    def SobIst2_nextPod1(self):
        root.clear_widgets()
        root.add_widget(MenuSob3())
        print("Sobitie2321")


class MenuSob2_nextPod2(BoxLayout):
    def goto_start_menuThree(self):
        root.clear_widgets()
        root.add_widgets(MenuSob2_next())

    def SobIst2_nextPod2(self):
        root.clear_widgets()
        root.add_widget(MenuSob3())
        print("Sobitie212")


class MenuSob3(BoxLayout):
    def goto_start_menuThree(self):
        root.clear_widgets()
        root.add_widgets(MenuSob2_nextPod1())

    def SobIst3(self):
        root.clear_widgets()
        root.add_widget(MenuSob4())
        print("Sobitie3")


class MenuSob4(BoxLayout):
    def goto_start_menuThree(self):
        root.clear_widgets()
        root.add_widgets(MenuSob3())

    def SobIst4(self):
        root.clear_widgets()
        root.add_widget(MenuSob2_next())
        print("Sobitie4")


# Runs the program
if __name__ == '__main__':
    Main().run()



