import sys
def change_input():
    tpp = list(input("Please input in the right format \n E.g. [[9,10], [9,12], [13,15], [10,18]]\n").split())
    # after split, the first element will have [ at the beginning and , at the back
    # this will slice of those 2
    tpp[0] = tpp[0][2:len(tpp[0])-2]

    # also need to slice the [ and , from the middle element as well
    if len(tpp) > 2:
        for i in range(1,len(tpp)-1):
            tpp[i] = tpp[i][1:-2]
        tpp[len(tpp)-1] = tpp[len(tpp)-1][1:-2]
    else:
        # slice the ] at the end
        tpp[len(tpp)-1] = tpp[len(tpp)-1][1:-2]
        
    # load the string list to new list, convert to int and sort
    tpp_list = list()
    for i in range(0,len(tpp)):
        tpp_list.append(tpp[i].split(","))
    for i in tpp_list:
        for j in range(0, 2):
            try:
                i[j] = int(i[j])
            except:
                print("Input was wrong formatting")
                sys.exit(1)
    temp = list()
    ready = list()
    for i, j in sorted(tpp_list):
        for k in range (i, j+1):
            temp.append(k)
        ready.append(temp)
        temp = list()
    return ready


def find_time(time):
    double = 0
    single = 0
    temp1 = [0,0]
    pair = 0

    #iterate for all the time
    for i in range (9, 18):
        temp1[0] = i
        temp1[1] = i + 1
        for i in time:
            if set(temp1).issubset(set(i)) == True:
                pair += 1
            else:
                continue

        # if the particular part has 4 players, count as double
        if pair >= 4:
            double += 1
            pair = 0

        # if the particular time has 2 or 3 players, count as single
        elif pair >= 2:
            single += 1
            pair = 0
        else:
            pair = 0
            continue
    return [single,double]
time = change_input()
res = find_time(time)
print(res)
