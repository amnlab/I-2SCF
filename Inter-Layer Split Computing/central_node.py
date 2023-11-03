import inter_intra
import numpy as np
import networkx as nx
print("=========================================================")
print("=================Central node execute====================")
print("=========================================================")

T = 3
R_tt = [inter_intra.information[0][1], inter_intra.information[1][2]]
C_t = [inter_intra.information[0][5], inter_intra.information[1][5], inter_intra.information[2][5]]
#8.3, 10.3, 14
#[3, 5], [4, 6], [6, 8]

layer_input_size = [32, 16, 16, 8, 8, 8, 4, 4, 4, 2, 2, 2, 1]
power = [[3, 5], [4, 6], [6, 8]]

# Neural Network
L =13
D_l = [3072, 16384, 32768, 8192, 16384, 16384, 4096, 8192, 8192, 2048, 2048, 2048, 512] #input size
F_l = [81, 38, 76, 38, 76, 76, 38, 76, 76, 18, 18, 18, 0] #GFlop + padding
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
    Tier_.append([Layer_.count(1) + Layer_.count(2) + 1, Layer_.count(1) + Layer_.count(2) + Layer_.count(3)])
    Tier_print.append([Layer_.count(1) + Layer_.count(2) + 1, Layer_.count(1) + Layer_.count(2) + Layer_.count(3)])
else:
    Tier_.append([0, 0])
    Tier_print.append([0, 0])
print("PATH", Tier_)

