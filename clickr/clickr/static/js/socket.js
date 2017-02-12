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
		    console.log(data.activate);
		    if (data.activate) {
		    	var newqn = $("<div class='list-group' id=qn"+ data.question_id + "></div>");
		    	$('#js-new-questions').append(newqn);
		    	newqn.append($("<div class='activeQn list-group-item active'>" + data.question_text + "</div>"));
			    for (i in data.options) {
			    	newqn.append(
			    		$("<div class='optionSelect list-group-item' text=" + data.options[i][0] + "qn=" + data.question_id + " >" + data.options[i][1] + "</div>")
			    	);
			   	};
			   	var pbar = $("<div class='progress progress-striped active'><div id='pbarinside' class='progress-bar' style='width: 0%'></div>");
			   	newqn.append(pbar);
			   	makeItMove($("#pbarinside"));
		    } else {
		    	$("#qn" + data.question_id).remove();
		    }
		}
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

	function makeItMove(pbar) {
		pbar.animate({width: "100%"}, 10000);
	}
