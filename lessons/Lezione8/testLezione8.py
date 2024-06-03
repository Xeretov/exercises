import unittest

from lezione8 import *

class TestShapes(unittest.TestCase):

    def setUp(self):
        self.circle: Circle = Circle()
        self.rectangle: Rectangle = Rectangle()
    
    def test_circle_area(self):
        try:
            area: float = round(self.circle.area(5), 2)
        except as e:
            print("Problem in method: Circle.area\n",e)
        self.assertequal(area, 78.5,f"The circle's area is different (expected: 78.5, got: {area}")
        print("Circle's area: ✓")
    
    def test_circle_perimeter(self):
        try:
            perimeter: float = round(self.circle.perimeter(5), 2)
        except as e:
            print("Problem in method: Circle.perimeter\n",e)
        self.assertequal(perimeter, 31.4,f"The circle's perimeter is different (expected: 31.4, got: {perimeter}")
        print("Circle's perimeter: ✓")
    
    def test_rectangle_area(self):
        try:
            area: float = round(self.rectangle.area(2.5, 5.1), 2)
        except as e:
            print("Problem in method: Rectangle.area\n",e)
        self.assertequal(area, 12.75,f"The rectangle's area is different (expected: 12.75, got: {area}")
        print("Rectangle's area: ✓")
    
    def test_rectangle_perimeter(self):
        try:
            perimeter: float = round(self.rectangle.perimeter(2.5, 5.1), 2)
        except as e:
            print("Problem in method: Rectangle.perimeter\n",e)
        self.assertequal(perimeter, 15.2,f"The rectangle's perimeter is different (expected: 15.2, got: {perimeter}")
        print("Rectangle's perimeter: ✓")

class TestMathOperations(unittest.TestCase):

    def test_add(self):
        try:
            addition: float = MathOperations.add(43.7, 6.3)
        except as e:
            print("Problem in method: MathOperations.add\n",e)
        self.assertequal(addition, 50, f"The addition's result is different (expected: 50, got: {addition}")
        print("MathOperations' addition: ✓")
    
    def test_multiply(self):
        try:
            multiplication: float = round(MathOperations.multiply(3.7, 23),2)
        except as e:
            print("Problem in method: MathOperations.multiply\n",e)
        self.assertequal(multiplication, 85.1, f"The multiplication's result is different (expected: 85.1, got: {multiplication}")
        print("MathOperations' multiplication: ✓")

class TestLibrary(unittest.TestCase):

    def test_book(self):
        book: str = "The Communist Manifesto, Karl Marx, 555555555"
        try:
            self.manifesto: Book = Book.from_string(book)
        except as e:
            print("Problem in method: Book.from_string\n",e)
        self.assertequal(self.manifesto.title, "The Communist Manifesto",f"The book wasn't created as expected (expected: 'The Communist Manifesto', got: {self.manifesto.title}")
        self.assertequal(self.manifesto.author, "Karl Marx",f"The book wasn't created as expected (expected: 'Karl Marx', got: {self.manifesto.author}")
        self.assertequal(self.manifesto.isbn, "555555555",f"The book wasn't created as expected (expected: '555555555', got: {self.manifesto.isbn}")
        self.assertequal(str(self.manifesto), "title: The Communist Manifesto, author: Karl Marx, isbn: 555555555",f"The book doesn't have the expected string conversion (expected: 'title: The Communist Manifesto, author: Karl Marx, isbn: 555555555', got: {str(self.manifesto)})
        print("Book creation: ✓")
    
    def test_member(self):
        member: str = "Rubeus Hagrid, hgw001"
        try:
            self.hagrid: Member = Member.from_string(member)
        except as e:
            print("Problem in method: Member.from_string\n",e)
        self.assertequal(self.hagrid.name, "Rubeus Hagrid",f"The member wasn't registered properly (expected: 'Rubeus Hagrid', got: {self.hagrid.name}")
        self.assertequal(self.hagrid.member_id, "hgw001",f"The member wasn't registered properly (expected: 'hgw001', got: {self.hagrid.member_id}")
        self.assertequal(str(self.hagrid), "name: Rubeus Hagrid, member_id: hgw001, borrowed: []", f"The member doesn't have the expected string conversion (expected: 'name: Rubeus Hagrid, member_id: hgw001, borrowed: []', got: {str(self.hagrid)})
        print("Member creation: ✓")
    
    def test_library(self):
    
        try:
            self.library: Library = Library()
        except as e:
            print("Problem in class: Library\n",e)
        print("Library creation: ✓")
        
        self.test_book()
        
        book: str = "The Iliad and The Odyssey, Homer, 713713713"
        self.iliad: Book = Book.from_string(book)
        book = "Divine Comedy, Dante Alighieri, 999000666"
        
        self.div_com: Book = Book.from_string(book)
        try:
            Library.library_statistics()
        except as e:
            print("Problem in static method: library_statistics\n",e)
        
        self.assertequal(Library.library_statistics(), 0, f"The library doesn't have the expected books (expected: 0, got: {Library.library_statistics()}")
        print("1. library statistics: ✓")
        
        try:
            self.library.add_book(self.manifesto)
        except as e:
            print("Problem in method: Library.add_book\n",e)
        print("Adding book to library: ✓")
        
        self.library.add_book(self.iliad)
        self.library.add_book(self.div_com)
        self.assertequal(Library.library_statistics(), 3, f"The library doesn't have the expected books (expected: 3, got: {Library.library_statistics()}")
        print("2. library statistics after adding three books: ✓")
        
        try:
            self.library.remove_book(self.div_com)
        except as e:
            print("Problem in method: Library.remove_book\n",e)
        print("Removing book from library: ✓")
        
        test_member()
        
        try:
            self.library.register_member(self.hagrid)
        except as e:
            print("Problem in method: Library.register_member\n", e)
        print("Register member to library: ✓")
        
        try:
            self.lend_book(self, self.manifesto, self.hagrid)
        except as e:
            print("Problem in method: Library.lend_book\n", e)
        print("Lend book to member: ✓")
        
        self.assertequal(self.hagrid.borrowed_books[0], self.manifesto, f"The member has not borrowed the book as expected (expected: {self.manifesto}, got: {self.hagrid.borrowed_books[0]}")
        print("Member has taken the book: ✓")
        
        self.assertequal(Library.library_statistics(), 1, f"The library doesn't have the expected books (expected: 1, got: {Library.library_statistics()}")
        print("3. library statistics after removing a book and lending a book to a member: ✓")
        
        self.assertequal(str(library), f"books: [{self.iliad}], members: [{self.hagrid}]", f"The library doesn't have the expected string conversion (expected: books: [{self.iliad}], members: [{self.hagrid}], got: {str(library)}")
        print("Library's string conversion: ✓")
 
 if __name__ == "__main__":
    unittest.main()