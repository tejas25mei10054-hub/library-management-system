#global Variables
Books = []
users = []
issuedbooks = []

#Adds Book to the library
def addbook():
  Title = input("Enter Book Title: ")
  Author = input("Enter Book Author: ")
  ISBN = input("Enter Book ISBN: ")
  print("Book ", Title ," by" ,Author ,"with ISBN", ISBN, "added to the library.")
  Book = {"title": Title, "author": Author, "isbn": ISBN}
  Books.append(Book)

#Gives all the books in library as output
def listbooks():
  print(Books)

#Searches if given book is present in Library
def searchbooks():
   isbn = input("Enter ISBN to search: ")
   for book in Books:
         if book["isbn"] == isbn:
            print("Book found:", book)
            return
   print("Book with ISBN", isbn, "not found.")

#Deletes book from library if present
def deletebooks():
   isbn = input("Enter ISBN to delete: ")
   for book in Books:
         if book["isbn"] == isbn:
            Books.remove(book)
            print("Book with ISBN", isbn, "deleted.")
            return
   print("Book with ISBN", isbn, "not found.")

#Registers user in the library so that he can issue books
def registeruser():
   user = input("Enter User Name to register: ")
   print("User", user, "registered successfully.")
   users.append(user)

#Issues book to the user and reflects book is gone from the library
def issuebooks():
   user = input("Enter User Name: ")
   isbn = input("Enter Book ISBN to issue: ")
   for book in Books:
         if book["isbn"] == isbn:
            if user in users:
             print("Book with ISBN", isbn, "issued to", user)
            else :
             print("User", user, "not found.")
            issuedbooks.append(book)
            Books.remove(book)
            return
   print("Book with ISBN", isbn, "not found.")

#Returns book from issued books to library
def returnbooks():
   user = input("Enter User Name: ")
   if user not in users:
      print("User", user, "not found.")
      return
   isbn = input("Enter Book ISBN to return: ")
   print("Book with ISBN", isbn, "returned by", user)
   for book in issuedbooks:
      if book["isbn"] == isbn:
         Books.append(book)
         issuedbooks.remove(book)

   
 #Executes whole program till Exit 
def main():
   while True:
       print("--- Library Management System ---")
       print("1. Add Book")
       print("2. List Books")
       print("3. Search Book")
       print("4. Delete Book")
       print("5. Register User")
       print("6. Issue Book")
       print("7. Return Book")
       print("8.Issued Books")
       print("9. Exit")
       choice = input("Enter your choice: ")
       if choice == '1':
         addbook()
       elif choice == '2':
        listbooks()
       elif choice == '3':
        searchbooks()
       elif choice == '4':
         deletebooks()
       elif choice == '5':
         registeruser()
       elif choice == '6':
         issuebooks()
       elif choice == '7':
         returnbooks()
       elif choice == '8':
         print(issuedbooks)
       elif choice == '9':
         print("Exiting the program.")
         break
       else:
        print("Invalid choice. Please try again.")
      
if __name__ == "__main__":
   main()

