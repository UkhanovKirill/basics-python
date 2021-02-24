from typing import Any

class Clothes:
    _clothes = []

    def __init__(self, measuring: Any):
        self._measuring = measuring
        self._tissue_required = None

        self._clothes.append(self)

    def _calc_tissue_required(self):
        raise NotImplemented

    @property
    def tissue_required(self) -> float:
        #Расход ткани
        if not self._tissue_required:
            self._calc_tissue_required()

        return self._tissue_required

    @property
    def measuring(self) -> Any:
        #Узнать размер
        return self._measuring

    @measuring.setter
    def measuring(self, measuring: Any):
        #Установить новый размер пальто
        self._measuring = measuring
        self._tissue_required = None

    @property
    def total_tissue_required(self):
        #Ткани на всю одежду
        return sum([item.tissue_required for item in self._clothes])


class Coat(Clothes):
    def _calc_tissue_required(self):
        #посчитать расход ткани для пальто
        self._tissue_required = round(self.measuring / 6.5 + 0.5, 2)

    @property
    def V(self) -> Any:
        #Узнать размер пальто
        return self.measuring

    @V.setter
    def V(self, size: Any):
        #Установить новый размер пальто
        self.measuring = size

    def __str__(self):
        return f"Для пошива пальто {self.measuring} размера " \
               f"требуется {self.tissue_required} кв. метров ткани"


class Suit(Clothes):
    def _calc_tissue_required(self):
        #посчитать расход ткани для костюма
        self._tissue_required = round(2 * self.measuring * 0.01 + 0.3, 2)

    @property
    def H(self) -> Any:
        #Узнать размер костюма
        return self.measuring

    @H.setter
    def H(self, height: Any):
        #Установить новый размер костюма
        self.measuring = height

    def __str__(self):
        return f"Для пошива костюма на рост {self.measuring} см. " \
               f"требуется {self.tissue_required} кв. метров ткани"

coat = Coat(5)
print(coat)
coat.V = 10
print(coat)

suit = Suit(178)
print(suit)
suit.H = 200
print(suit)

print(coat.total_tissue_required)
print(suit.total_tissue_required)