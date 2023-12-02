invent_name = ['r', 'p', 'a', 'm', 'i', 'k', 'x', 't', 'f', 'd', 's', 'c']
invent_cost = [25, 15, 15, 20, 5, 15, 20, 25, 15, 10, 20, 20]
invent_place = [3, 2, 2, 2, 1, 1, 3, 1, 1, 1, 2, 2]

invent_1 = []
for i in range(0,len(invent_place)):
    if invent_place[i] == 1:
        helpmas = []
        helpmas.append(invent_cost[i])
        helpmas.append(invent_name[i])
        invent_1.append(helpmas)
invent_1.sort()

invent_2 = []
for i in range(0,len(invent_place)):
    if invent_place[i] == 2:
        helpmas = []
        helpmas.append(invent_cost[i])
        helpmas.append(invent_name[i])
        invent_2.append(helpmas)
invent_2.sort()

invent_3 = []
for i in range(0,len(invent_place)):
    if invent_place[i] == 3:
        helpmas = []
        helpmas.append(invent_cost[i])
        helpmas.append(invent_name[i])
        invent_3.append(helpmas)
invent_3.sort()



table = []
score = []
for i in range(0,len(invent_place)):
    helptable = ['0', '0', '0']
    name = invent_name[i]
    cost = invent_cost[i]
    place = invent_place[i]
    helptable.append(name*place)
    scorehelp = [0,0,0]
    scorehelp.append(cost)
    column = place-1
    while column<7:
        val1 = 0
        val2 = 0
        val3 = 0
        if column==2:
            if invent_1[-1][1] not in helptable[-1]:
                helptable.append(helptable[-1] + invent_1[-1][1])
                scorehelp.append(invent_1[-1][0])
                column += 1
            else:
                helptable.append(helptable[-1] + invent_1[-2][1])
                scorehelp.append(invent_1[-2][0])
                column += 1
        elif column ==3:
            for i in range (-1,0-len(helptable[-1])-1,-1):
                if len(invent_1) < i*(-1):
                    val1 = 0
                elif invent_1[i][1] in helptable[-1]:
                    val1 = 0
                else:
                    val1 = invent_1[i][0]
                    val1_1 = invent_1[i][1]
                    break
            for i in range (-1,0-len(helptable[-2])-1,-1):
                if len(invent_2) < i * (-1):
                    val1 = 0
                elif invent_2[i][1] not in helptable[-2]:
                    val2 = invent_2[i][0]
                    val2_1 = invent_2[i][1]
                    break
            if val2+scorehelp[-2] > val1+scorehelp[-1]:
                helptable.append(helptable[-2]+ val2_1*2)
                scorehelp.append(val2+scorehelp[-2])
                column += 1
            else:
                helptable.append(helptable[-2]+ val1_1)
                scorehelp.append(val1+scorehelp[-1])
                column += 1
        else:
            for i in range (-1,0-len(helptable[-1])-1,-1):
                if len(invent_1) < i * (-1):
                    val1 = 0
                elif invent_1[i][1] in helptable[-1]:
                    val1 = 0
                else:
                    val1 = invent_1[i][0]
                    val1_1 = invent_1[i][1]
            for i in range (-1,0-len(helptable[-2])-1,-1):
                if len(invent_2) < i * (-1):
                    val1 = 0
                if invent_2[i][1] not in helptable[-2]:
                    val2 = invent_2[i][0]
                    val2_1 = invent_2[i][1]
                    break
            for i in range (-1,0-len(helptable[-3])-1,-1):
                if len(invent_3) < i * (-1):
                    val1 = 0
                if invent_3[i][1] not in helptable[-3]:
                    val3 = invent_3[i][0]
                    val3_1 = invent_3[i][1]
                    break
            if val2+scorehelp[-2]>val1+scorehelp[-1] and val2+scorehelp[-2] > val3+scorehelp[-3]:
                helptable.append(helptable[-2]+ val2_1*2)
                scorehelp.append(val2+scorehelp[-2])
                column += 1
            elif val1+scorehelp[-1]>val3+scorehelp[-3]:
                helptable.append(helptable[-1]+ val1_1)
                scorehelp.append(val1 + scorehelp[-1])
                column += 1
            else:
                helptable.append(helptable[-3]+ val3_1*3)
                scorehelp.append(val3 + scorehelp[-3])
                column += 1
    score.append(scorehelp[-1])
    table.append(helptable[-1])

scorein = score.index(max(score))
stro = table[scorein]
itmas = []
for i in stro:
    mas = [i]
    itmas.append(mas)
print(itmas[:4])
print(itmas[4:])
counterscore = 15+max(score)
for i in range (0,len(invent_name)):
    if invent_name[i] not in stro:
        counterscore -= invent_cost[i]
print('Итоговые очки выживания: ', counterscore)