import time

class Book:
    def __init__(self, title, author, pages):
        self.title = title
        self.author = author
        self.pages = pages
        
    def __str__(self) :
        return f'{self.title} by {self.author}'
    
    def __repr__(self) :
        return f"Book('{self.title}', '{self.author}', {self.pages})"
    
    def __len__(self) :
        return self.pages
    
    def __add__(self,other):
        if isinstance(other,Book) :
            total_pages = self.pages + other.pages
            return Book(f"Combined Book", "Various Authors", total_pages)
    def __eq__(self, other):
        if isinstance(other,Book):
            return self.pages == other.pages
    def __lt__(self, other):
        if isinstance(other,Book):
            return self.pages < other.pages
        
    def __getitem__(self,key):
        if key =='title':
            return self.title
        elif key =='author':
            return self.author
        elif key =='pages':
            return self.pages
        else :
            return "Invalid keyword"
        
    def __setitem__(self,key,value):
        if key == 'title':
            self.title = value
        elif key == 'author':
            self.author = value
        elif key == 'pages':
            self.pages = value
        else:
            raise KeyError(f"'{key}' is not a valid key.")
    def __call__(self):
        return f"{self.title} is available to be read."
    
    def __enter__(self):
        print(f"You've opened '{self.title}'. Enjoy your reading!")
        
        return self

    def __exit__(self, exc_type, exc_value, traceback):
        time.sleep(5)
        print(f"You've finished reading '{self.title}'. Goodbye!")
    
        
     
    
book1 = Book("The Great Gatsby", "F. Scott Fitzgerald", 180)
book2 = Book("To Kill a Mockingbird", "Harper Lee", 320)
book3 = Book("Pride and Prejudice", "Jane Austen", 280)
print(book1) #str
print(repr(book1))
print(len(book1))
combined_book = book1 + book2  # __add__
print(combined_book, len(combined_book))
print(book1 == book3) 
print(book2 < book3)

print(book1['title']) #
print(book1['age']) 
print(book1.title)
print(book2['author'])
book1['author'] = "New Author" 
print(book1['author']) 
book1.author = "New cool Author" 
print(book1['author']) 
print(book3()) #Makes the object callable
with book3:  # __enter__ and __exit__
    print("Reading...")    
print("Book closed.")
print(dir(Book))