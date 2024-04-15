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
