from abc import ABC, abstractmethod

class Shape:

    @abstractmethod
    def getArea() -> None:
        pass
    @abstractmethod
    def render() -> None:
        pass

class Square(Shape):

    def __init__(self, side: int) -> None:
        super().__init__()
        self.side: int = side
    
    def getArea(self) -> int:
        return self.side**2
    
    def render(self) -> None:
        for i in range(self.side):
            if i == 0 or i == self.side-1:
                print(f"{'*':^2}"*self.side)
            else:
                print(f"{'*':^2}"+f"{' ':^2}"*(self.side-2)+f"{'*':^2}")

class Rectangle(Shape):

    def __init__(self, base: int, height: int) -> None:
        super().__init__()
        self.base = base
        self.height = height
    
    def getArea(self) -> int:
        return self.base*self.height

    def render(self) -> int:
        for i in range(self.height):
            if i == 0 or i == self.height-1:
                print(f"{'*':^2}"*self.base)
            else:
                print(f"{'*':^2}"+f"{' ':^2}"*(self.base-2)+f"{'*':^2}")

class Triangle(Shape):

    def __init__(self, side: int) -> None:
        super().__init__()
        self.side: int = side
    
    def getArea(self) -> float:
        return (self.side**2)//2

    def render(self) -> None:
        for i in range(self.side):
            if i == 0:
                print(f"{'*':^2}")
            elif i < self.side-1:
                print(f"{'*':^2}"+f"{' ':^2}"*(i-1)+f"{'*':^2}")
            else:
                print(f"{'*':^2}"*self.side)
