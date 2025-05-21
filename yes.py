import random

class Game:
    def __init__(self, game_type):
        # Khởi tạo trò chơi với loại game và danh sách điểm rỗng
        self.game_type = game_type
        self._scores = []

    # Getter: điểm ngẫu nhiên theo loại trò chơi
    @property
    def score(self):
        if self.game_type == "coin":
            return random.choice([0, 1])  # 0: sấp, 1: ngửa
        elif self.game_type == "dice":
            return random.randint(1, 6)
        else:
            return None

    # Getter: trả về số lượt chơi
    @property
    def quantity(self):
        return len(self._scores)

    # Setter: thêm điểm vào danh sách điểm
    @quantity.setter
    def quantity(self, value):
        self._scores.append(value)

    # Deleter: xóa tất cả điểm đã chơi
    @quantity.deleter
    def quantity(self):
        self._scores.clear()

    # Getter: tổng điểm các lượt chơi
    @property
    def total_score(self):
        return sum(self._scores)

    # Phương thức chơi
    def play(self, rounds=1):
        print(f"Playing '{self.game_type}' game for {rounds} round(s):")
        for i in range(rounds):
            point = self.score
            self.quantity = point  # Gọi setter để thêm điểm
            print(f"Round {i + 1}: {point}")
        print(f"Total score: {self.total_score}")

game = Game("dice")
game.play(5)

print(f"Rounds played: {game.quantity}")
print(f"Total score: {game.total_score}")

del game.quantity
print(f"after the uhh reset, rounds played are abt {game.quantity}")