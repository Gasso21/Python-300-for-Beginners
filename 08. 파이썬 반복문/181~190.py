#181
apart = [[101,102],[201,202],[301,302]]

#182
stock = [[100, 200, 300],[80, 210, 330]]

#183
stock = {'시가':[100, 200, 300], '종가':[80, 210, 330]}

#184
stock = {'10/10':[80, 110, 70, 90], '10/11':[210, 230, 190, 200]}

#185
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j, "호")

#186
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in i:
        print(j, "호")

#187
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart[::-1]:
    for j in i[::-1]:
        print(j, "호")
#188
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j, "호 \n-----")

#189
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j, "호")
    print("-----")

#190
apart = [ [101, 102], [201, 202], [301, 302] ]
for i in apart:
    for j in i:
        print(j, "호")
print("-----")
