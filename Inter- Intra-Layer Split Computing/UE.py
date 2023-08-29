import Tier0
import Tier1
import Tier2
import evaluation
print("\n\n=========================================================")
print("======================UE execute=========================")
print("=========================================================")

if(Tier0.end_Layer0 == 9):
    eval0 = evaluation.evaluation_for_SC(Tier0.intermediate_result, Tier0.y_test)
    print("OK", eval0)
elif(Tier1.end_Layer1 == 9):
    eval1 = evaluation.evaluation_for_SC(Tier1.intermediate_result, Tier0.y_test)
    print("OK", eval1) 
elif(Tier2.end_Layer2 == 9):
    eval2 = evaluation.evaluation_for_SC(Tier2.intermediate_result, Tier0.y_test)
    print("OK", eval2)
    
print("Tier0 inference_latency :  ", Tier0.inference_Latency)
print("Tier1 inference_latency :  ", Tier1.inference_Latency)
print("Tier2 inference_latency :  ", Tier2.inference_Latency)
print("-----------------------------------")
print("Total inference_latency :  ", Tier0.inference_Latency + Tier1.inference_Latency + Tier2.inference_Latency)
