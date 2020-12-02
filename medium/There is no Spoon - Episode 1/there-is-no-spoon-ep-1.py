width = int(input())  # the number of cells on the X axis
height = int(input())  # the number of cells on the Y axis

L = []
for i in range(height):
    line = input() # width characters, each either 0 or .
    L.append([])
    for j in range(width):
        
        if line[j] == '0':
            if L[i] != []:
                L[i][-1][1] = (i, j)
                
            L[i].append([(i, j), (-1, -1), (-1, -1)])

            if i > 0:

                def update_power_node(L, cur_row_index, cur_col_index):
                    for k in range(cur_row_index-1, -1, -1):    
                        for l in range(len(L[k])):
                            node_list = L[k][l]
                            if node_list[0] == (k, cur_col_index):
                                node_list[2] = (cur_row_index, cur_col_index)
                                L[k][l] = node_list
                                return L
                    return L

                L = update_power_node(L, i, j)

for line in L:
    for n in line:
        print(f'{n[0][1]} {n[0][0]} {n[1][1]} {n[1][0]} {n[2][1]} {n[2][0]}')