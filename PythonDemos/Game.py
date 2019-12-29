class Game:
    # 历史最高分
    top_score = 0

    def __init__(self, player_name):
        self.player_name = player_name

    @staticmethod
    def show_help():
        print("帮助。。。。")

    @classmethod
    def show_top_score(cls):
        print("历史记录 %d " %cls.top_score)

    def start_game(self):
        print("%s 开始游戏啦 " %self.player_name)


# 静态方法
Game.show_help()
# 类方法
Game.show_top_score()
# 实例方法
Game("小明").start_game()
