# README.md
* 서버 실행 시 `Error: That port is already in use.` 에러가 발생하는 경우
<pre>sudo lsof -t -i tcp:8000 | xargs kill -9</pre>
