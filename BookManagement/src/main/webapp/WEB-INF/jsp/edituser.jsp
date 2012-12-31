<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="form"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"%>
<%@ taglib prefix="sec"
	uri="http://www.springframework.org/security/tags"%>
	<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn"%>
	
<html>
<head>
<title>Intel Press Management</title>
<meta name='description' content='A simple page'>
</head>
<body>
	
	<br />
	<div id="content" class="row-fluid span8">
		<div class="row">

			<div id="upload-article-container" class="span8">
				<h2>Edit User</h2>
				<p>Please correct the information about this book.</p>
				<p style="font-weight:bold;">${error}</p>
				<hr>
				<form name='f' class="form-horizontal"
				action="<c:url value='/admin/usermanagement/edituser/${user.id}' />"
				method='POST' enctype="multipart/form-data">
				<fieldset>
					<div class="control-group">
						<label class="control-label" for="firstname">First name</label>
						<div class="controls">
							<input id="firstname" name="firstname" class="input-xlarge focused"
								value="${user.firstname}" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="lastname">Last name</label>
						<div class="controls">
							<input id="lastname" name="lastname" class="input-xlarge focused"
								value="${user.lastname}" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="email">Email</label>
						<div class="controls">
							<input id="email" name="email"
								class="input-xlarge focused" value="${user.email}" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="username">Username</label>
						<div class="controls">
							<input id="username" name="username" class="input-xlarge focused"
								value="${user.username}" type="text">
						</div>
					</div>

				</fieldset>
				<div class="modal-footer" style="height: 15px;">
					<button type="submit" class="btn btn-primary">Update User</button>
				</div>
			</form>
			</div>
			<br />
			<a class="btn" href="/bookmanagement/admin/usermanagement/" >Back</a>
		</div>
		<!-- Row -->
	</div>
	<br />

</body>
</html>
