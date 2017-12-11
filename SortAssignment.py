'''
Raspberry Pi Assignment - Sorting

Sorting is simply reordering a list of items in a logical order, such as alphabetical or in increasing order.

Sounds simple, huh?  And it is for small lists of items.  But computers are often asked to sort very large lists
of items.  And the bigger they get, the more computing power it takes to do it.  The time required is not linear.
It is logarithmic - which means if it takes 1 second to sort 1 million items, it will take much, much longer than 2
seconds to sort 2 million items.

Some very intelligent people have made their life's work out of creating and optimizing sort algorithms.

ASSIGNMENT 1 - BACKGROUND
See https://en.wikipedia.org/wiki/Sorting_algorithm - you don't have to understand everything that you read, but get a
feel for the topic.

ASSIGNMENT 2 - EXPLORE THE .sort() method in Python.
Record how long it takes this method to sort 100,000 items.  Look at the code I wrote below.  It starts with only 10
items but you can increase it up to millions.  How can you change the code to record how long it takes to do the sort?

ASSIGNMENT 3 - Repalce .sort() with your own algorithms.
    - An insertion sort

    How does your sort algorithm perform compared to the one Python comes with?

    An insertion sort is pretty easy to implement.  You simply pick the first item in the list and compared it to the
    second item.  Which ever is smaller then gets compared to the third item.  You keep going until you get to the end
    of the list.  Whatever number you have at the end of the list is the smaller number in the list.  Append it to a new
    list and delete it from the original list.  Then do it all over again until your original list has no more
    elements.
    Compare this to sorting cards.  Take only the hearts from a deck and shuffle them.  Then start at the first card
    compare it to the second.  Keep the lowest card in your left hand.  Then compare to the third and so on.  At the
    end, you'll have the lowest card.  Repeat to get the next card until you are done.

ASSIGNMENT 4 - Implement a Bubble sort.  (We'll do this together when we meet online.)

'''
import random

number_of_items = 10                    # start small and increaes once working.
#
my_randoms=[]

for i in range (number_of_items):
    my_randoms.append(random.randrange(1,101,1))   # lookup randrange and make sure you understand it.

print ("\n\n\nThe list of random numbers in no particular order.")
print (my_randoms)

my_randoms.sort()

print ("\n\nThe list of random numbers in ascending sorted order.")
print (my_randoms)

my_randoms.sort(reverse=True)

print ("\n\nThe list of random numbers in descending sorted order.")
print (my_randoms)

