// console.log(window.location.pathname);

var socket = new WebSocket(
  "ws://127.0.0.1:8000/ws/number" + window.location.pathname
);
// // socket.onopen = function (e) {
// //   socket.send(JSON.stringify({ winpath: window.location.pathname }));
// // };
socket.onmessage = function (e) {
  var data = JSON.parse(e.data);
  document.querySelector("#app").innerHTML = data["text"];
};
