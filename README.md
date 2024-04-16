<div align="center">
<h1>😉CBOM</h1>
  
SBOM을 이용한 취약점 식별 자동화 시스템 <br> Automation System for Vulnerability Identification Using SBOM

![대시보드1](https://github.com/Dxhyeon/cbom-project/assets/118159407/803a765e-ea6e-4f66-94cb-f4f89b3826eb)

</div>

<br>

## 프로젝트 소개

 - CBOM은 SBOM을 이용하여 소프트웨어의 취약점을 식별하고 투명성을 검증할 수 있는 솔루션입니다.
 - 취약점 식별 외에도 소프트웨어에 사용된 오픈소스와 라이선스를 확인할 수 있습니다.
 - 대시보드를 통해 취약점 식별 결과를 한눈에 확인할 수 있습니다.
 - 취약점 식별 결과와 SBOM 정보를 Report로 저장할 수 있습니다.
 
<br>

## 팀원 구성

<div align="center">

| **강민식** | **김도현** | **최수호** | **최영훈** |
| :------: |  :------: | :------: | :------: |
| [<img src="https://avatars.githubusercontent.com/u/127810857?v=4" height=150 width=150> <br/> @MynameisMansik](https://github.com/MynameisMansik) | [<img src="https://avatars.githubusercontent.com/u/118159407?v=4" height=150 width=150> <br/> @Dxhyeon](https://github.com/Dxhyeon) | [<img src="https://avatars.githubusercontent.com/u/71062855?v=4" height=150 width=150> <br/> @S4nso](https://github.com/S4nso) | <img src="https://github.com/Dxhyeon/cbom-project/assets/118159407/939243a3-2385-4412-8b76-614a80972694" height=150 width=150> <br/> 최영훈 |
|Front-end Develop|Back-end Develop|Back-end Develop|Front-end Develop|

</div>

<br>

## 1. 개발 환경
- Front-end : Django, Bootstrap, Chart.js
- Back-end : Python, Django
- Database : MariaDB
- 협업 툴 : Notion, Discord, Github
  
<br>

## 2. SBOM

### SBOM 이란?
SBOM(Software Bill Of Materials)은 소프트웨어의 구성 요소 및 종속성을 체계적으로 문서화한 목록입니다. 이 문서는 소프트웨어 제작에 사용된 모든 구성 요소와 그들간의 관계의 상세한 정보를 포함하며,
소프트웨어 보안 및 소프트웨어 공급망 관리의 핵심 구성 요소입니다. 

### SBOM에 포함되는 주요 정보

| 항목            | 설명                                                    |
|-----------------|---------------------------------------------------------|
| 공급자 정보     | 소프트웨어 컴포넌트를 제공한 조직 또는 개인의 정보         |
| 컴포넌트 이름 및 식별자 | 각 구성 요소의 이름과 고유한 식별 번호               |
| 버전 정보       | 컴포넌트의 버전 정보로, 업데이트 및 변경 사항을 추적할 수 있습니다. |
| 컴포넌트 해시   | 컴포넌트의 무결성을 확인하기 위한 해시 값                 |
| 종속성 및 관계  | 컴포넌트 간의 의존성 및 상호 작용 정보                   |
| 작성자 정보     | 컴포넌트를 작성한 개인 또는 팀의 정보                     |
| 라이선스 정보   | 컴포넌트에 적용된 라이선스 유형과 조건                     |
| 취약성 정보     | 컴포넌트의 보안 취약점 및 관련된 보안 업데이트 정보         |

### SBOM의 중요성
SBOM은 소프트웨어의 투명성을 높이고, 보안 전문가가 취약점을 식별하고 관리하는 데 큰 도움을 제공합니다. 또한, 개발, 유지보수, 보안 측면에서 효율적인 소프트웨어 관리와 관련된 다양한 작업을 지원하는 필수 도구입니다.

<br>

## 3. 개발 기간 및 작업 관리

### 개발 기간

- 전체 개발 기간 : 2023-09-05 ~ 2023-11-21
- DB 설계 & 구축 : 2023-09-21 ~ 2023-10-14
- Web 설계 & 구축 : 2023-09-28 ~ 2023-10-16
- 취약점 식별 기능 구현 : 2023-09-05 ~ 2023-11-21

### 작업 관리

 - Notion과 Discord를 사용하여 진행 상황을 공유하였습니다.
 - 매 주 대면 회의를 진행하며 작업 순서에 대하여 논의하고, Trouble Shooting을 진행하였습니다.

<br>

## 4. 프로젝트 구성도

![image](https://github.com/Dxhyeon/cbom-project/assets/118159407/04d74e46-712d-4a58-922f-f3c38c5ec333)

|단계|내용|
|-----|---|
|1. SBOM 업로드|사용자는 웹 플랫폼에 SBOM을 업로드|
|2. SBOM 구성 요소 추출 및 출력|각 구성 요소의 패키지와 버전등 사용된 정보를 추출하여 재가공 및 웹 플랫폼 출력|
|3. 취약점 식별 및 분석|CVE와 CWE 데이터를 활용하여 오픈 소스 패키지의 취약점을 식별하고 해당 취약점 내용 추출하여 저장|
|4. 시각적 결과 제공|취약점 분석 결과는 웹 플랫폼을 통해 사용자에게 시각적으로 제공|

<br>

## 5. 페이지별 기능

### [초기화면]

- 접속 초기화면인 서비스 소개 페이지입니다.
- SBOM에 대한 정보와 중요성, 서비스의 설명이 소개되어 있습니다.

| 초기화면 |
|----------|
|![1online-video-cutter com-ezgif com-video-to-gif-converter (1)](https://github.com/Dxhyeon/cbom-project/assets/118159407/07467606-44a9-4cda-a16d-f0baf8c3c7ed)|

<br>

### [대시보드]

#### 1. 취약점 식별

- SBOM을 업로드하여 취약점을 식별합니다.
- 핵심 결과를 시각화하여 가독성을 높혔습니다.
  
| 취약점 식별 결과 |
|----------|
|![1online-video-cutter com1-ezgif com-video-to-gif-converter](https://github.com/Dxhyeon/cbom-project/assets/118159407/7ba4bc91-6660-4137-be39-1b66cba5c249)|

<br>

#### 2. CVE 페이지 호출

- 식별된 취약점에 대한 CVE 페이지를 호출합니다.
- CVE의 자세한 내용을 확인할 수 있습니다.

| CVE 페이지 호출 |
|----------|
|![1online-video-cutter com2-ezgif com-video-to-gif-converter](https://github.com/Dxhyeon/cbom-project/assets/118159407/179617ae-3623-40d8-ad2e-d9464bc6b98c)|

<br>

### [SBOM List]

- SBOM의 자세한 정보를 확인할 수 있습니다.
- 컴포넌트 이름과 버전, 제공자, 라이선스 정보, 해쉬값이 포함되어 있습니다.

| SBOM Detailed Information |
|----------|
|![1online-video-cutter com4-ezgif com-video-to-gif-converter (1)](https://github.com/Dxhyeon/cbom-project/assets/118159407/56de65d8-ce3e-4deb-ac9f-c322e0468124)|

<br>

### [Vulnerability List]

#### 1. 식별된 취약점 정보 확인

- 식별된 취약점의 자세한 정보를 확인할 수 있습니다.
- CVE ID, CWE ID, Description, Risk Score, Risk Level을 제공합니다. ( National Vulnerability Database  기준 )

| Vulnerability Detailed Information |
|----------|
|![1-ezgif com-video-to-gif-converter](https://github.com/Dxhyeon/cbom-project/assets/118159407/81d60af4-450e-4513-a89b-d94feb32730f)|

<br>

#### 2. CWE 페이지 호출

- 식별된 취약점에 대한 CWE 페이지를 호출합니다.
- CWE의 자세한 내용을 확인할 수 있습니다.

| CWE 페이지 호출 |
|----------|
|![2-ezgif com-video-to-gif-converter](https://github.com/Dxhyeon/cbom-project/assets/118159407/34a3308f-61ef-4041-aa66-d8d32fa82a36)|

<br>

### [License List]

#### 1. 사용 라이선스 정보 확인

- 사용된 라이선스의 정보를 확인할 수 있습니다.
- 사용 의무 사항과 Description을 제공합니다.

| License Detailed Information |
|----------|
|![12-ezgif com-video-to-gif-converter](https://github.com/Dxhyeon/cbom-project/assets/118159407/c6d2c1de-ca70-4a37-8ef4-42d469a922cb)|

<br>

#### 2. 라이선스 페이지 호출

- 사용된 라이선스에 대한 페이지를 호출합니다.
- 라이선스의 자세한 내용을 확인할 수 있습니다.

| License 페이지 호출 |
|----------|
|![13-ezgif com-video-to-gif-converter](https://github.com/Dxhyeon/cbom-project/assets/118159407/a11f31ca-9f60-484d-a75a-584930bfcbc8)|

<br>

### [Generate Report]

- 취약점 식별 결과와 SBOM 정보를 Report로 저장합니다.

| Generate Report |
|----------|
|![14-ezgif com-video-to-gif-converter](https://github.com/Dxhyeon/cbom-project/assets/118159407/871cd40c-f155-4d38-a794-e2acb802fccd)|

<br>

### 6. 향후 계획

- 취약점 조치 방안 자동화
  - 취약점 식별은 가능하나, 해당 취약점에 대한 대응 방안을 자세하게 알 수 없음
  - AI를 통해 적절한 대응 방안을 제공할 수 있는 방향으로 계획

<br>

- 컴포넌트 무결성 검사
   - SBOM의 컴포넌트 해시 값을 활용하지 못했음
   - 검사를 통해 파일 변조 등 소프트웨어의 무결성 검증 

<br>

- 라이선스 충돌 탐지
  - 라이선스에 대한 정보를 활용하지 못했음
  - 사용된 오픈소스의 라이선스간의 충돌을 탐지하여 라이선스 양립성(Compatibility) 문제 해결




  
