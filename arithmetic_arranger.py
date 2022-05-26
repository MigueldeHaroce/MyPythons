# NOTE: If you only use 4 parameters, so I only put 4 parameters

def arithmetic_arranger(oplist, do_or_not):
    global secondnum4, firstnum4, thirdnum4, secondnum3, firstnum3, thirdnum3, secondnum2, firstnum2, thirdnum2, secondnum1, firstnum1, thirdnum1, result1, result2, result3, result4
    mylist = oplist
    first = mylist[0]
    second = mylist[1]
    third = mylist[2]
    fourth = mylist[3]
    first_list = first.split()
    second_list = second.split()
    third_list = third.split()
    fourth_list = fourth.split()
    for _ in fourth_list:
        firstnum4 = int(fourth_list[0])
        secondnum4 = fourth_list[1]
        thirdnum4 = int(fourth_list[2])
    for numb_int3 in third_list:
        firstnum3 = int(third_list[0])
        secondnum3 = third_list[1]
        thirdnum3 = int(third_list[2])
    for numb_int2 in second_list:
        firstnum2 = int(second_list[0])
        secondnum2 = second_list[1]
        thirdnum2 = int(second_list[2])
    for numb_int1 in first_list:
        firstnum1 = int(first_list[0])
        secondnum1 = first_list[1]
        thirdnum1 = int(first_list[2])

    if secondnum4 == "+":
        result4 = firstnum4 + thirdnum4
    elif secondnum4 == "-":
        result4 = firstnum4 - thirdnum4

    if secondnum3 == "+":
        result3 = firstnum3 + thirdnum3
    elif secondnum3 == "-":
        result3 = firstnum3 - thirdnum3

    if secondnum2 == "+":
        result2 = firstnum2 + thirdnum2
    elif secondnum2 == "-":
        result2 = firstnum2 - thirdnum2

    if secondnum1 == "+":
        result1 = firstnum1 + thirdnum1
    elif secondnum1 == "-":
        result1 = firstnum1 - thirdnum1

    print("Your operation are:")
    print(f" {firstnum1}    {firstnum2}    {firstnum3}    {firstnum4}")
    print(f"{secondnum1} {thirdnum1}  {secondnum2}   {thirdnum2}  {secondnum3}  {thirdnum3}  {secondnum4}{thirdnum4}")
    print("----   ----   ----   ----")
    if do_or_not:
        print(f' {result1}    {result2}    {result3}   {result4}')



arithmetic_arranger(["329 + 34", "321 - 1", "123 + 21", "312 + 2344"], True)
