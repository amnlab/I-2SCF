import inter_intra
import numpy as np
import networkx as nx
print("=========================================================")
print("=================Central node execute====================")
print("=========================================================")

T = 3
R_tt = [inter_intra.information[0][1], inter_intra.information[1][2]]
C_t = [inter_intra.information[0][5], inter_intra.information[1][5], inter_intra.information[2][5]]

layer_input_size = [32, 16, 16, 8, 8, 8, 4, 4, 4, 2, 2, 2, 1]
power = [[inter_intra.csmaTier0_info[0][2], [inter_intra.csmaTier0_info[1][2]], [inter_intra.csmaTier1_info[0][2], inter_intra.csmaTier1_info[1][2]], [inter_intra.csmaTier2_info[0][2], inter_intra.csmaTier2_info[1][2]]
# Neural Network
L = 13
D_l = [3072, 16384, 32768, 8192, 16384, 16384, 4096, 8192, 8192, 2048, 2048, 2048, 512] #input size
F_l = [81, 38, 76, 38, 76, 76, 38, 76, 76, 18, 18, 18, 0] #GFlop
padding = [0, 2.5, 5, 5, 9.5, 9.5, 9.5, 19, 19, 0, 0, 0, 0] #padding GFlop
tau_R = 0.1

N_V = T * L
A = np.zeros((N_V + 1, N_V + 1))

for i in range(1, N_V + 1):
    for j in range(1, N_V + 1):
        if j == i + 1 and (i % T) != 0:
            A[i, j] = np.inf
    for j in range(1, N_V + 1):
        if j == i + T:
            if (i % T) != 0:
                A[i, j] = F_l[int(np.ceil(i / T)) - 1] / C_t[i % T - 1]
            else:
                A[i, j] = F_l[int(np.ceil(i / T)) - 1] / C_t[T - 1]
    for j in range(1, N_V + 1):
        if j == i + T + 1:
            if (i % T) != 0:
                A[i, j] = D_l[int(np.ceil(i / T)) - 1] / R_tt[i % T - 1] + F_l[int(np.ceil(i / T)) - 1] / C_t[i % T - 1]
G = nx.DiGraph(A)
G.add_node(1)
last_vertex = G.number_of_nodes()
A = np.pad(A, ((0, 0), (0, 1)), 'constant', constant_values=0)

for i in range(1, N_V + 1):
    if int(np.ceil(i / T)) == L:
        A[i, last_vertex] = F_l[int(np.ceil(i / T)) - 1] / C_t[T - 1] + tau_R

A = np.delete(A, 0, 0)
A = np.delete(A, 0, 1)

A = np.vstack((A, np.zeros((1, last_vertex))))

G = nx.DiGraph(A)

P = nx.shortest_path(G, source=0, target=last_vertex - 1, weight='weight')
d = nx.shortest_path_length(G, source=0, target=last_vertex - 1, weight='weight')


Layer_ = []
for i in range(0, len(P) - 1):
    if((P[i] + 1)%3 == 0):
        Layer_.append((P[i] + 1) % 3 + 3)
    else:
        Layer_.append((P[i] + 1)%3)
#print(Layer_)
Tier_ = []
Tier_print = []
if  Layer_.count(1) != 0:
    Tier_.append([1, Layer_.count(1)])
    Tier_print.append([1, Layer_.count(1)])
else:
    Tier_.append([0, 0])
    Tier_print.append([0, 0])
if  Layer_.count(2) != 0:
    Tier_.append([Layer_.count(1) + 1, Layer_.count(1) + Layer_.count(2)])
    Tier_print.append([Layer_.count(1) + 1, Layer_.count(1) + Layer_.count(2)])
else:
    Tier_.append([0, 0])
    Tier_print.append([0, 0])
if  Layer_.count(3) != 0:
    Tier_.append([Layer_.count(1) + Layer_.count(2) + 1, Layer_.count(1) + Layer_.count(2) + Layer_.count(3) - 4])
    Tier_print.append([Layer_.count(1) + Layer_.count(2) + 1, Layer_.count(1) + Layer_.count(2) + Layer_.count(3)])
else:
    Tier_.append([0, 0])
    Tier_print.append([0, 0])

for i in range(3):
    for j in range(2):
        if Tier_[i][j] == 13:	
            Tier_[i][j] = 9

print("PATH", Tier_print)
Node_ = []
for i in range(0, 3):
    if i == 0:
        Node_.append([[]])
        node = power[i].index(max(power[i]))
        if(node == 0):
            Node_[i][0].append(layer_input_size[Tier_[i][0] - 1])
            Node_[i][0].append(0)
        elif(node == 1):
            Node_[i][0].append(0)
            Node_[i][0].append(layer_input_size[Tier_[i][0] - 1])
        for j in range(Tier_[i][0] + 1, Tier_[i][1] + 1):
            if Tier_[i][0] == Tier_[i][1] and Tier_[i][0] != 0:
                Node_.append([[]])
                node = power[i].index(max(power[i]))
                if(node == 0):
                    Node_[i][0].append(layer_input_size[j - 1])
                    Node_[i][0].append(0)
                elif(node == 1):
                    Node_[i][0].append(0)
                    Node_[i][0].append(layer_input_size[j - 1])

            elif Tier_[i][0] != Tier_[i][1] and Tier_[i][0] != 0:
                if j == Tier_[i][0]:
                    Node_.append([])
                if j >= 11:
                    node = power[i].index(max(power[i]))
                    if (node == 0):
                        split_point = [layer_input_size[j - 1], 0]
                        Node_[i].append(split_point)
                    if (node == 1):
                        split_point = [0, layer_input_size[j - 1]]
                        Node_[i].append(split_point)
                else:
                    split_point1 = round(power[i][0] * (layer_input_size[j - 1]/(power[i][0] + power[i][1])))
                    split_point2 = round(power[i][1] * (layer_input_size[j - 1]/(power[i][0] + power[i][1])))
                    if split_point1 % 2 == 1 or split_point2 % 2 == 1:
                        node = power[i].index(max(power[i]))
                        if (node == 0):
                            split_point1 = split_point1 + 1
                            split_point2 = split_point2 - 1
                        elif (node == 1):
                            split_point1 = split_point1 - 1
                            split_point2 = split_point2 + 1
                    split_point = [split_point1, split_point2]
                    Node_[i].append(split_point)
    else:
        for j in range(Tier_[i][0], Tier_[i][1] + 1):
            if Tier_[i][0] == Tier_[i][1] and Tier_[i][0] != 0 or Tier_[i][0] == 1:
                Node_.append([[]])
                node = power[i].index(max(power[i]))
                if(node == 0):
                    Node_[i][0].append(layer_input_size[j - 1])
                    Node_[i][0].append(0)
                elif(node == 1):
                    Node_[i][0].append(0)
                    Node_[i][0].append(layer_input_size[j - 1])

            elif Tier_[i][0] != Tier_[i][1] and Tier_[i][0] != 0:
                if j == Tier_[i][0]:
                    Node_.append([])
                if j >= 11:
                    node = power[i].index(max(power[i]))
                    if (node == 0):
                        split_point = [layer_input_size[j - 1], 0]
                        Node_[i].append(split_point)
                    if (node == 1):
                        split_point = [0, layer_input_size[j - 1]]
                        Node_[i].append(split_point)
                else:
                    split_point1 = round(power[i][0] * (layer_input_size[j - 1]/(power[i][0] + power[i][1])))
                    split_point2 = round(power[i][1] * (layer_input_size[j - 1]/(power[i][0] + power[i][1])))
                    if split_point1 % 2 == 1 or split_point2 % 2 == 1:
                        node = power[i].index(max(power[i]))
                        if (node == 0):
                            split_point1 = split_point1 + 1
                            split_point2 = split_point2 - 1
                        elif (node == 1):
                            split_point1 = split_point1 - 1
                            split_point2 = split_point2 + 1
                    split_point = [split_point1, split_point2]
                    Node_[i].append(split_point)
    
    
print("SplitPoint", Node_)

