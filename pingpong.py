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

# find double hours of the people
def find_double(time):
    dt = list()
    st = list()

    #find the insection of 4 people
    #it iterate one by one like 1234, 2345
    for i in range(0, len(time)):
        if i != (len(time)-3):
            same = list(set(time[i]).intersection(time[i+1]).intersection(time[i+2]).intersection(time[i+3]))
            if len(same) > len(dt) and same not in dt:
                dt = same
            else:
                continue
        else:
            break

    #slice the time begin and end
    temp = dt[1:-1]

    #slice the time end
    dt = dt[:-1]

    #slice the double time from all person and convert to list
    for i in range(0, len(time)):
        st.append(set(time[i])-set(temp))
    for i in range(0,len(st)):
        st[i] = list(st[i])

    return [len(dt), st, dt]
            
def find_single(time, dt):
    sin = list()
    play = 0
    temp1 = [0,0]
    pair = 0

    #iterate through the avialable time to find the single players
    for i in range (9, 18):
        if i not in dt:
            temp1[0] = i
            temp1[1] = i + 1
            for i in time:
                if set(temp1).issubset(set(i)) == True:
                    pair += 1
                else:
                    continue
            if pair >= 2:
                play += 1
                pair = 0
            else:
                pair = 0
                continue
        else:
            continue
    return play
time = change_input()
if len(time) >= 4:
    tmp = find_double(time)
    res = [find_single(tmp[1], tmp[2]), tmp[0]]
    print(res)
else:
    res = [find_single(time, []), 0]
    print(res)
