import inter_intra
import numpy as np
import networkx as nx
print("======================================================================================")
print("Central Node Execute")
print("======================================================================================")

T = 3
R_tt = [inter_intra.information[0][1], inter_intra.information[1][2]]
C_t = [inter_intra.information[0][5], inter_intra.information[1][5], inter_intra.information[2][5]]

layer_input_size = [32, 16, 16, 8, 8, 8, 4, 4, 4, 2, 2, 2, 1]

power = [[inter_intra.csmaTier0_info[0][2], inter_intra.csmaTier0_info[1][2], inter_intra.csmaTier0_info[2][2]], 
[inter_intra.csmaTier1_info[0][2], inter_intra.csmaTier1_info[1][2], inter_intra.csmaTier1_info[2][2]], 
[inter_intra.csmaTier2_info[0][2], inter_intra.csmaTier2_info[1][2], inter_intra.csmaTier2_info[2][2]]]
## Neural Network
L = 13
D_l = [3072, 16384, 32768, 8192, 16384, 16384, 4096, 8192, 8192, 2048, 2048, 2048, 512] #input size
F_l = [81, 38, 76, 38, 76, 76, 38, 76, 76, 18, 18, 18, 0] #GFlop
#F_l = [324, 152, 304, 152, 304, 304, 152, 304, 304, 72, 72, 72, 0] #GFlop
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

print("[Inter-Layer Split Policy]")
for i in range(3):
    print("Tier", i, "Splitting Point :", Tier_print[i])

def express_as_weighted_sum(k, weights):  # j = 3, 6, 9
    if len(weights) == 3:  # 가중치 리스트의 길이가 3인지 확인

        # 각 가중치의 인덱스와 값을 함께 저장
        weighted_indices = list(enumerate(weights))
        # 가중치를 기준으로 내림차순 정렬
        weighted_indices.sort(key=lambda x: x[1], reverse=True)

        # 각 가중치를 k와 비례하도록 정규화
        normalized_weights = [weight / sum(weights) for weight in weights]

        a, b, c = 0, 0, 0

        if k == 4:  # 4*4 예외 처리
            count = 0
            for index, _ in weighted_indices:
                if index == 0:
                    a = 2
                elif index == 1:
                    b = 2
                elif index == 2:
                    c = 2

                count += 1
                if count == 2:
                    break
            return [a, b, c]

        # 각 변수에 정규화된 가중치를 적용하여 할당
        a = int(normalized_weights[0] * k)
        b = int(normalized_weights[1] * k)
        c = int(normalized_weights[2] * k)

        # 남은 차이를 가중치가 큰 순서대로 더해주기
        diff = k - (a + b + c)
        for index, _ in weighted_indices:
            if diff > 0:
                if index == 0:
                    a += 1
                elif index == 1:
                    b += 1
                elif index == 2:
                    c += 1
                diff -= 1
            else:
                break

        # 짝수 변환 과정
        if a % 2 == 1 and b % 2 == 1:
            if a == b:
                a -= 1
                b += 1
            else:
                a += 1
                b -= 1
        elif b % 2 == 1 and c % 2 == 1:
            if b == c:
                b -= 1
                c += 1
            else:
                b += 1
                c -= 1
        elif a % 2 == 1 and c % 2 == 1:
            if a == c:
                a -= 1
                c += 1
            else:
                a += 1
                c -= 1

        # 결과 반환
        return [a, b, c]
    else:
        # 조건에 맞지 않으면 예외 처리
        print("주어진 k 값이 2의 배수가 아니거나, 가중치 리스트의 길이가 3이 아닙니다.")
        return None

Layer_size1 = layer_input_size[Tier_[0][0] - 1:Tier_[0][1]]
Layer_size2 = layer_input_size[Tier_[1][0] - 1:Tier_[1][1]]
Layer_size3 = layer_input_size[Tier_[2][0] - 1:Tier_[2][1]]

Node_ = []
Node_.append([])
for i in range(0, len(Layer_size1)):
    Node_[0].append(express_as_weighted_sum(Layer_size1[i], power[0]))
Node_.append([])   
for i in range(0, len(Layer_size2)):
    Node_[1].append(express_as_weighted_sum(Layer_size2[i], power[1]))
Node_.append([])
for i in range(0, len(Layer_size3)):
    Node_[2].append(express_as_weighted_sum(Layer_size3[i], power[2]))
Node_[2].append([0, 0, 2])
Node_[2].append([0, 0, 2])
Node_[2].append([0, 0, 2])
Node_[2].append([0, 0, 1])
print("[Intra-Layer Split Policy]")
for i in range(3):
    print("Tier", i, "Splitting Point :", Node_[i])
    
