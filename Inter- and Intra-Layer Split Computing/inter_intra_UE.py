import tier0
import tier1
import tier2
import evaluation

print("======================================================================================")
print("Inter-Intra UE execute")
print("======================================================================================")

if(tier0.end_Layer0 == 9):
    eval0 = evaluation.evaluation_for_SC(tier0.intermediate_result, tier0.y_test)
    #print(eval0)
    inference_latency = tier0.inference_Latency
    print("Tier 1 inference_latency :  ", tier0.inference_Latency)
    print("-----------------------------------")
    print("Total inference_latency :  ", tier0.inference_Latency)
elif(tier1.end_Layer1 == 9):
    eval1 = evaluation.evaluation_for_SC(tier1.intermediate_result, tier0.y_test)
    #print(eval1)
    inference_latency = tier0.inference_Latency + tier1.inference_Latency
    print("Tier 1 inference_latency :  ", tier0.inference_Latency)
    print("Tier 2 inference_latency :  ", tier1.inference_Latency)
    print("-----------------------------------")
    print("Total inference_latency :  ", tier0.inference_Latency + tier1.inference_Latency) 
elif(tier2.end_Layer2 == 9):
    eval2 = evaluation.evaluation_for_SC(tier2.intermediate_result, tier0.y_test)
    #print(eval2)
    inference_latency = tier0.inference_Latency + tier1.inference_Latency + tier2.inference_Latency
    print("Tier 1 inference_latency :  ", tier0.inference_Latency)
    print("Tier 2 inference_latency :  ", tier1.inference_Latency)
    print("Tier 3 inference_latency :  ", tier2.inference_Latency)
    print("-----------------------------------")
    print("Total inference_latency :  ", tier0.inference_Latency + tier1.inference_Latency + tier2.inference_Latency)

latency = inference_latency
