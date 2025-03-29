reading_books={"noor","renuka","sadhiya","minha","banusha","asra","jaziyah","aisha"}
painting={"renuka","asra","zainab","kaneez","marya","sheeza","aazeen","aisha"}

#union: join two sets but removes duplicate
print(reading_books.union(painting))
#to get the common names in the groups: 
print(reading_books.intersection(painting))
#people who like reading books but dont like painting
print(reading_books.difference(painting))
#people who like painting but do not like reading books
print(painting.difference(reading_books))
#getting uncommon names
print(reading_books.symmetric_difference(painting))