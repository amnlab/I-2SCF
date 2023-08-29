import node0
import node1
import node2
import evaluation
print("======================================================================================")
print("UE execute")
print("======================================================================================")

if(node0.end_Layer0 == 13):
    print("oK", node0.intermediate_result0)
    eval0 = evaluation.evaluation_for_SC(node0.intermediate_result0, node0.y_test)
    print(eval0)
    inference_latency = node0.latency0
    print("node0 inference latnecy : ", node0.latency0)
    print("-------------------------------")
    print("Total inference latency : ", inference_latency)
elif(node1.end_Layer1 == 13):
    print("oK", node1.intermediate_result1)
    eval1 = evaluation.evaluation_for_SC(node1.intermediate_result1, node0.y_test)
    print(eval1)
    inference_latency = node0.latency0 + node1.latency1
    print("node0 inference latnecy : ", node0.latency0)
    print("node1 inference latnecy : ", node1.latency1)
    print("-------------------------------")
    print("Total inference latency : ", inference_latency)
elif(node2.end_Layer2 == 13):
    print("oK")
    eval2 = evaluation.evaluation_for_SC(node2.intermediate_result2, node0.y_test)
    print(eval2)
    inference_latency = node0.latency0 + node1.latency1 + node2.latency2
    print("node0 inference latnecy : ", node0.latency0)
    print("node1 inference latnecy : ", node1.latency1)
    print("node2 inference latnecy : ", node2.latency2)
    print("-------------------------------")
    print("Total inference latency : ", inference_latency)

