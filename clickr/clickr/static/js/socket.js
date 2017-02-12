$(function() {
	var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
	var chat_socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/waitforquestion" + window.location.pathname);

	$('#chatform').on('submit', function(event) {
	    var message = {
	        name: $('#name').val(),
	        option: $('#option').val(),
	    }
	    chat_socket.send(JSON.stringify(message));
	    return false;
	});

	chatsocket.onmessage = function(message) {
    var data = JSON.parse(message.data);
    $('#question').append(
    	data.question_text;
    	data.options;
    	);
   	};
});

