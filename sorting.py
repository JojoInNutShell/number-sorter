def last_index_finder(list_to_sort,last,counter):
    while last == False:
        try:
            try_index = list_to_sort[counter]
            counter += 1
        except Exception:
            last = True
            return counter - 1

def bubble_sort(list_to_sort,sort_finish,counter,last_index,last_index_temp,moves):
    counter = 0
    print(list_to_sort)
    while sort_finish == False:
        if counter == last_index_temp:
            print("The sort is finished!")
            print(list_to_sort)
            sort_finish = True
            break
        elif last_index == 0:
            last_index = last_index_temp
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

list_to_sort = [10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
counter = 0
try_index = 0
moves = 0
last = False
last_index = last_index_finder(list_to_sort,last,counter)
last_index_temp = last_index
sort_finish = False

bubble_sort(list_to_sort,sort_finish,counter,last_index,last_index_temp,moves)