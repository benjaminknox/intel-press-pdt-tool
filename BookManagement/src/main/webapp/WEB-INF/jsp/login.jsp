<%@ taglib prefix="c" uri="http://java.sun.com/jsp/jstl/core"%>
<%@ taglib prefix="sec"
	uri="http://www.springframework.org/security/tags"%>
<html>
<head>
<title>Intel Press Management - Login</title>
</head>
<body onload='document.f.j_username.focus();'>
	<div class="modal">
		<div class="modal-header">

			<h3>Login</h3>
		</div>
		<div class="modal-body" style="text-align: center">

			<c:if test="${not empty error}">
				<div class="alert alert-error" style="height: 20px;">
					<p>
						<span class="ui-icon ui-icon-mail-closed"
							style="float: left; height: 5px; margin-right: .3em;"></span> <strong>Error:</strong>
						Invalid login credentials, please try again.
					</p>
				</div>
			</c:if>
			<form name='f' class="form-horizontal"
				action="<c:url value='j_spring_security_check' />" method='POST'>
				<fieldset>
					<div class="control-group">
						<label class="control-label" for="j_username">Username</label>
						<div class="controls">
							<input id="j_username" name="j_username"
								class="input-xlarge focused" placeholder="username" type="text">
						</div>
					</div>
					<div class="control-group">
						<label class="control-label" for="j_password">Password</label>
						<div class="controls">
							<input id="j_password" name="j_password"
								class="input-xlarge focused" placeholder="password"
								type="password" autocomplete="off">
						</div>
					</div>
				</fieldset>
				<div class="modal-footer" style="height: 15px;">
					<button type="submit" class="btn btn-primary">Submit</button>
				</div>
			</form>

		</div>
	</div>
</body>
</html>