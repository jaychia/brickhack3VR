$(function() {
		var loginButton = $("#login-submit");
		var loginField = $("#login-field");
		var classField = $("#class-field");
		var loginForm = $("#js-login-div");
		var activeDiv = $("#js-active-div");
		var oldquestions = $("#js-old-questions");
		var profnamebanner = $("#profnamebanner");

		activeDiv.hide();

		loginButton.click(function(e){
			$.ajax({
				url: "student/" + loginField.val() + '/' + classField.val(),
				success: function(resp) {
					showClassroom(resp);
				},
				error: function() {
					alert('shit!');
				}
			});
			return false;
		});

		function showClassroom(resp) {
			profnamebanner.text("Welcome, " + resp.student_name);
			loginForm.hide();
			for (i in resp.questions) {
				var question = resp.questions[i];
				var questionWrapper = $("<div class='qWrapper'></div>");
				oldquestions.append(questionWrapper);
				var id = question[0];
				var txt = question[1];
				questionWrapper.append($("<div class='question'>" + (parseInt(i) + 1).toString() + ") " + txt + "</div>"));
				var options = question[2];
				for (j in options) {
					var option = options[j];
					var optiondiv = $("<div class='option'>" + option + "</div>");
					questionWrapper.append(optiondiv);
				}
			}
			activeDiv.show();
			initiateSocket(resp.student_name, resp.class_label);
		}

	});