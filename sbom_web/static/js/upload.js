// 파일 업로드 함수 정의
function ekUpload() {
  // 초기화 함수
  function Init() {
    // 콘솔에 업로드 초기화 메시지 출력
    console.log("업로드가 초기화되었습니다.");

    // DOM 요소 가져오기
    var fileSelect = document.getElementById('file');
    var fileDrag = document.getElementById('file-drag');
    var submitButton = document.getElementById('submit-button');

    // 파일 선택 이벤트 처리
    fileSelect.addEventListener('change', fileSelectHandler, false);

    // XHR2 사용 가능한지 확인
    var xhr = new XMLHttpRequest();
    if (xhr.upload) {
      // 파일 드래그 앤 드롭 관련 이벤트 처리
      fileDrag.addEventListener('dragover', fileDragHover, false);
      fileDrag.addEventListener('dragleave', fileDragHover, false);
      fileDrag.addEventListener('drop', fileSelectHandler, false);
    }
  }

  // 파일 드래그 관련 이벤트 처리
  function fileDragHover(e) {
    var fileDrag = document.getElementById('file-drag');

    e.stopPropagation();
    e.preventDefault();
  }

  // 파일 선택 이벤트 처리
  function fileSelectHandler(e) {
    // FileList 객체 가져오기
    var files = e.target.files || e.dataTransfer.files;

    // 이벤트 취소 및 드래그 스타일 초기화
    fileDragHover(e);

    // 모든 파일 객체 처리
    for (var i = 0, f; f = files[i]; i++) {
      parseFile(f);
      uploadFile(f);
    }
    //var fileSelect = document.getElementById('file');
    //fileSelect.disabled = true;
  }

  // 출력 함수
  function output(msg) {
    // 응답 영역 요소 가져오기
    var m = document.getElementById('messages');
    m.innerHTML = msg;
  }

  // 파일 분석 함수
  function parseFile(file) {
    console.log(file.name);
    output(
      '<strong>' + encodeURI(file.name) + '</strong>'
    );

    var imageName = file.name;

    // 파일 확장자 확인 (이미지인지 확인)
    var isImage = /\.(?=spdx|json)/gi.test(imageName);
    if (isImage) {
      // 이미지 파일인 경우
      document.getElementById('start').classList.add("hidden");
      document.getElementById('response').classList.remove("hidden");
      document.getElementById('notimage').classList.add("hidden");
    } else {
      // 이미지 파일이 아닌 경우
      document.getElementById('file-image').classList.add("hidden");
      document.getElementById('notimage').classList.remove("hidden");
      document.getElementById('start').classList.remove("hidden");
      document.getElementById('response').classList.add("hidden");
      document.getElementById("file-form").reset();
    }
  }

  // 파일 업로드 함수
  function uploadFile(file) {
    var xhr = new XMLHttpRequest();

    if (xhr.upload) {
      // 파일 크기 제한 확인 (제한 없음)
      xhr.onreadystatechange = function (e) {
        if (xhr.readyState == 4) {
          if (xhr.status == 200) {
            // 파일 업로드 성공 시 처리
            var response = JSON.parse(xhr.responseText);
            if (response.message === 'File uploaded successfully.') {
              // 파일 업로드 성공 처리 수행
            }
          } else {
            // 파일 업로드 실패 시 처리
          }

        }
      };


      // 파일 업로드 시작
      xhr.open('POST', document.getElementById('file-form').action, true);
      xhr.setRequestHeader('X-File-Name', encodeURIComponent(file.name));
      //xhr.setRequestHeader('X-File-Size', file.size);
      //xhr.setRequestHeader('Content-Type', 'multipart/form-data');
      xhr.send(file);
      
    }
  }

  // File API 지원 여부 확인
  if (window.File && window.FileList && window.FileReader) {
    Init();
  } else {
    document.getElementById('file-drag').style.display = 'none';
  }
}

// 파일 업로드 함수 호출
ekUpload();