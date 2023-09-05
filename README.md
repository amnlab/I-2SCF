<img src="https://capsule-render.vercel.app/api?type=waving&color=auto&height=200&section=header&text=Inter-%20and%20Intra-Layer%20Split%20Computing&fontSize=40" />
<h1>Proposed Method</h1>
<body>대부분의 기존 분할컴퓨팅(split computing)연구에서 계층 간 분할(Inter-layer split)에 초점을 두는데 DNN의 각 계층을 여러 개의 독립적인 실행단위로 분리시킨다면 추가적인 inference latency를 줄일 수 있다. 따라서 본 논문은 계층 간 분할(Inter-layer split) 및 계층 내 분할(Intra-layer split) 컴퓨팅 프레임 워크 Inter- and Intra-Layer Split Computing를 제안하는 것이 목표이다.</body>

<h1>System Model</h1>
<p align="center">
<img src="https://github.com/amnlab/I-2SCF/assets/143478273/6f484f2e-8700-4cdd-b9a5-b3639bd89b59" width="500">
</p>
</br>
<body>컴퓨팅 노드가 계층적으로 분산되어 T개의 Tier가 있다고 가정하고 Central cloud에서 Tier간 링크의 전송속도와 컴퓨팅 노드의 가용 컴퓨팅 파워를 수집한다. 이렇게 수집한 정보를 기반으로 inference latency를 효율적으로 줄이기 위해 계층 간 분할(Inter-layer split)과 계층 내 분할(Intra-layer split)지점 결정 후 결정된 지점을 각 컴퓨팅 노드에 전송한다.</body>

<h1>Test Environment & Parameter Setting</h1>
<p align="center">
<img src="https://github.com/amnlab/I-2SCF/assets/143478273/355e705e-5fcb-4061-ac48-8ab7ee3c313b" width="500">
</br>
<img src="https://github.com/amnlab/I-2SCF/assets/143478273/d0b98541-6360-4c9f-8767-339052663efa" width="500">
</p>

<h1>Test Equipment</h1>
<body>
(H/W)
* CPU: 12th Gen Intel(R) Core(TM) i7-12700K 3.60 GHz
* GPU: NVIDA GeForce RTX 4090
* MEM: 32GB
* SSD/HDD: 

(S/W)
- OS: Ubuntu 64-bit 20.04
- Python 2.7.18
- Tensorflow 2.12.0
- NS-3.3
