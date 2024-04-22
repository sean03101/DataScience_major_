# Border emphasis LIME

### 연구 배경
![image](https://github.com/sean03101/DataScience_major_/assets/59594037/84626bd0-7326-49ba-9704-ff65b636d595)


LIME(Local Interpretable Model-agnostic Explanations) 
  - 블랙박스 모델의 예측에 대해 해석 가능한 모델로 지역적으로 근사 시킴으로써 블랙박스 모델을 설명
  - 개별 데이터 객체에 대한 블랙박스 모델의 예측을 설명하기 위하여 local surrogate model을 학습
  - 다음과 같은 절차를 통해 관심개체에 대한 블랙박스 모델의 예측을 설명
      1) 블랙박스 모델의 예측에 대해 설명하고자 하는 데이터 객체를 선택한다.
      2) 관심개체 주위로 데이터셋을 교란(perturb)시켜 새로운 데이터 샘플들을 생성하고 블랙박스 모델의 예측 값을 얻는다.
      3) 관심개체와 생성된 샘플 간의 거리와 Exponential smoothing kernel을 통해 생성된 각 샘플에 대한 가중치를 설정한다
      4) Weighted, interpretable model을 학습한다.
      5) Local model을 해석함으로써 관심개체에 대한 예측을 설명한다.

        

  - 장점
      1) 블랙박스 모델에 관계 없이 모델을 설명할 수 있다. (Local model agnostic)
      2) 테이블, 텍스트, 이미지 데이터 모두에서 사용 가능하다.
  - 단점
      1) Hyperparameter 대한 민감성 : LIME에서 설정하는 hyperparameter에 따라 설명의 결과가 완전히 다를 수 있다.
      2) 데이터 생성의 랜덤성 : 무작위로 교란(perturb)을 통해 생성된 샘플로 학습된 local surrogate model은 블랙 박스 모델을 충분히 근사하지 않을 수 있다.
      3) 불안정성 : 동일한 데이터 객체에 대해서도 매번 서로 다른 설명을 도출할 수 있다. 



### 연구 방법론 : Border emphasis LIME

![image](https://github.com/sean03101/DataScience_major_/assets/59594037/ed662a34-fbbf-4014-8c9b-b616f5f46260)

- **Classification black box model에 적용 가능한 Local surrogate method**
- 기존 LIME은 설명하고자 하는 샘플 주위에 무작위로 교란된 샘플들을 생성하고 local surrogate model을 학습 -> 이렇게 학습된 local surrogate model은 지역적으로 블랙박스 모델과 유사하지 않을 수 있으며 설명의 결과가 정확하지 않을 수 있음

<br>

- Border emphasis LIME은 **<U>black box model의 클래스 간 경계에 있는 데이터 샘플의 개수를 늘림으로써 local surrogate model의 정확도와 설명력을 높임</U>**
- 지역적으로 black box model과 더욱 유사한 surrogate model을 생성할 수 있음

<br>

제안하는 방법은 
  1) 기존의 LIME과 동일한 방식으로 설명하고자 하는 데이터 객체 주변으로 Random perturbation을 통해 데이터 샘플 생성
  2) 유클리디안 거리를 이용해 각 샘플 별 k개의 이웃 샘플 선택
  3) 이웃 샘플들 중 서로 다른 클래스(Black box model의 예측 클래스)에 속한 샘플이 존재할 경우 아래와 같은 수식을 통해 추가적으로 데이터 샘플을 생성
       - 추가 데이터(s) 생성 (𝑥^𝑅: 다른 클래스에 속한 데이터 샘플, 0≤𝜇≤1)
      ![image](https://github.com/sean03101/DataScience_major_/assets/59594037/d0f89f08-a849-4216-9d41-87225393e9da)
  4) Random perturbation으로 생성한 샘플들에 추가적으로 생성한 샘플들을 더하여 local surrogate model을 학습

### 기대 효과

 - Border line에서의 LIME의 불안정성을 개선할 수 있다.
 - 지역적인 부분에서 블랙박스 모델과 더 유사한 Local surrogate model을 학습시킬 수 있다.
 - 블랙박스 모델에 대해 더 정확한 설명력을 가지는 Local surrogate model을 학습시킬 수 있다.


