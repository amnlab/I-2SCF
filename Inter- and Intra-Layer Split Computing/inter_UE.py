import node0
import node1
import node2
import evaluation
print("======================================================================================")
print("Inter UE Execute")
print("======================================================================================")

if(node0.end_Layer0 == 13):
    eval0 = evaluation.evaluation_for_SC(node0.intermediate_result0, node0.y_test)
    #print(eval0)
    inference_latency = node0.latency0
    print("node 1 inference latnecy : ", node0.latency0)
    print("-------------------------------")
    print("Total inference latency : ", inference_latency)
elif(node1.end_Layer1 == 13):
    eval1 = evaluation.evaluation_for_SC(node1.intermediate_result1, node0.y_test)
    #print(eval1)
    inference_latency = node0.latency0 + node1.latency1
    print("node 1 inference latnecy : ", node0.latency0)
    print("node 2 inference latnecy : ", node1.latency1)
    print("-------------------------------")
    print("Total inference latency : ", inference_latency)
elif(node2.end_Layer2 == 13):
    eval2 = evaluation.evaluation_for_SC(node2.intermediate_result2, node0.y_test)
    #print(eval2)
    inference_latency = node0.latency0 + node1.latency1 + node2.latency2
    print("node 1 inference latnecy : ", node0.latency0)
    print("node 2 inference latnecy : ", node1.latency1)
    print("node 3 inference latnecy : ", node2.latency2)
    print("-------------------------------")
    print("Total inference latency : ", inference_latency)

latency = inference_latency
