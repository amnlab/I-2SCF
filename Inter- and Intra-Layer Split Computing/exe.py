import inter_intra_UE
import inter_UE

inter = inter_UE.latency
intra = inter_intra_UE.latency
print("---------------------------------------------------------------------")
print("## Compare Infernce Latency")
print("Inter-Layer Split Computing:", inter)
print("Inter- and Intra-Layer Split Computing:", intra)
improve = (inter - intra)/inter * 100
print("---------------------------------------------------------------------")
print("Improved", improve,"% than Inter-Layer Split Computing")
