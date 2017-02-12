	var ws_scheme = window.location.protocol == "https:" ? "wss" : "ws";
	var chat_socket = null;
	var name = "";

	function initiateSocket(name, label) {
		console.log('Initializing websocket.');
		name = name;
		console.log(ws_scheme + '://' + window.location.host + "/clickr/" + label);
		chat_socket = new ReconnectingWebSocket(ws_scheme + '://' + window.location.host + "/clickr/" + label);
		chat_socket.onmessage = function(message) {
	    var data = JSON.parse(message.data);
	    console.log(data);
	    $('#js-new-questions').append($("<div>" + data.question_text + "</div>"));
	    for (i in data.options) {
	    	$('#js-new-questions').append(
	    		$("<div class='optionSelect' text=" + data.options[i][0] + "qn=" + data.question_id + " >" + data.options[i][1] + "</div>")
	    	);
	   	};
   };
	}

	$('.optionSelect').on('click', function(event) {
	    var message = {
	        name: name,
	        question: $(this).attr('qn'),
	        option: $(this).attr('text'),
	    }
	    chat_socket.send(JSON.stringify(message));
	    return false;
	});
