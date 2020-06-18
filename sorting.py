from random import shuffle

def main_menu():

    menu = ("""
Number Sorter v1.1 by JojoInNutShell
Choose which type of number sorting method do you want to see :
1) Bubble Sort
2) Selection Sort
3) Insertion Sort
4) All Number Sorting Methods\n
""")

    choose = int(input(menu))
    if choose == 1:
        bubble_sort(list_to_sort,sort_finish,counter,last_index,last_index_temp,moves,mover)
    elif choose == 2:
        selection_sort(list_to_sort,smallest,searcher,index_now,fully_sorted,pos)
    elif choose == 3:
        insertion_sort(list_to_sort,fully_sorted,mover,moves)
    elif choose == 4:
        bubble_sort(list_to_sort,sort_finish,counter,last_index,last_index_temp,moves,mover)
        selection_sort(list_to_sort,smallest,searcher,index_now,fully_sorted,pos)
        insertion_sort(list_to_sort,fully_sorted,mover,moves)
    else:
        main_menu()

def after_sorting_menu():
    choose = int(input("Do you want to go back to main menu? 1) Yes 2) Nope : "))
    if choose == 1:
        main_menu()
    elif choose == 2:
        pass

def last_index_finder(list_to_sort,last,counter):
    while last == False:
        try:
            try_index = list_to_sort[counter]
            counter += 1
        except Exception:
            last = True
            return counter - 1
    
def bubble_sort(list_to_sort,sort_finish,counter,last_index,last_index_temp,moves,mover):
    list_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    sort_finish = False
    counter = 0
    print("BUBBLE SORT : ")
    print(list_to_sort)
    while sort_finish == False:
        if counter == last_index_temp:
            print(f"The sorting is finished : {list_to_sort}\n\n")
            sort_finish = True
            break
        elif last_index == mover:
            last_index = last_index_temp
            mover += 1
        if list_to_sort[last_index - 1] > list_to_sort[last_index]:
            list_to_sort[last_index - 1], list_to_sort[last_index] = list_to_sort[last_index], list_to_sort[last_index - 1]
            print(list_to_sort)
            last_index -= 1
            counter = 0
            moves += 1
        else:
            counter += 1
            last_index -= 1
            moves += 1

def selection_sort(list_to_sort,smallest,searcher,index_now,fully_sorted,pos):
    list_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    fully_sorted = 0
    print("SELECTION SORT : ")
    print(list_to_sort)
    sort_finish = False
    while fully_sorted != len(list_to_sort):
        if list_to_sort[index_now] == searcher:
            list_to_sort.insert(pos, searcher)
            list_to_sort.pop(index_now + 1)
            fully_sorted += 1
            index_now = 0 + fully_sorted
            pos += 1
            searcher += 1
            print(list_to_sort)
        else:
            index_now += 1
    print(f"The sorting is finished : {list_to_sort}\n\n")

def insertion_sort(list_to_sort,fully_sorted,mover,moves):
    list_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    fully_sorted = 1
    print("INSERTION SORT : ")
    print(list_to_sort)
    while fully_sorted != len(list_to_sort):
        if list_to_sort[fully_sorted -1 - mover] > list_to_sort[fully_sorted]:
            mover += 1
        elif fully_sorted -1 - mover == -1:
            mover -= 1
            list_to_sort.insert(0, list_to_sort[fully_sorted])
            list_to_sort.pop(fully_sorted + 1)
            fully_sorted += 1
            mover  = 0
            print(list_to_sort)
        elif mover > 0:
            list_to_sort.insert(fully_sorted - mover, list_to_sort[fully_sorted])
            list_to_sort.pop(fully_sorted + 1)
            mover  = 0
            fully_sorted += 1
            print(list_to_sort)
        else:
            fully_sorted += 1
    print(f"The sorting is finished : {list_to_sort}\n\n")

#Variables for sorting (More than once used variable)
list_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
fully_sorted = 0
mover = 0
moves = 0

#Variables for bubble sort
counter = 0
try_index = 0
last = False
last_index = last_index_finder(list_to_sort,last,counter) #You also can use len(list_to_sort) - 1 rather than to use that function
last_index_temp = last_index
sort_finish = False

#Variables for selection sort
smallest = 0
searcher = 1
index_now = 0
pos = 0

main_menu()
