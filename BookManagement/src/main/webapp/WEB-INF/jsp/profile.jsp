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
	<c:if test="${success != null}" >
		<script>toastr.success('${success}');</script>
	</c:if>
	<c:if test="${fn:length(errors) > 0}" >
		<script>toastr.error('Please correct the form errors');</script>
	</c:if>
	<br />
	<div id="content" class="row-fluid span8">
		<div class="row">

			<div id="upload-article-container" class="span8">
				<h2>Profile</h2>
				<p>Below is some basic information about you and your contributions to this system.</p>
				<c:forEach var="error" items="${errors}">
					<p style="font-weight:bold;" >${error}</p>
				</c:forEach>
				<hr>
				
				<p>Username: ${user.username}</p>
				<p>First Name: ${user.firstname}</p>
				<p>Last Name: ${user.lastname}</p>
				<p>Email: ${user.email}</p>
				<br>
				
				<h2>Change Password</h2>
				<hr>
				<form name='f' class="form-horizontal"
				action="<c:url value='/resetpassword/${user.id}' />"
				method='POST' enctype="multipart/form-data">
				<fieldset>
					<div class="control-group">
						<label class="control-label" for="oldPassword">Old Password</label>
						<div class="controls">
							<input id="oldPassword" name="oldPassword" class="input-xlarge focused"
								value="" type="password">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="newPasswordOne">New Password</label>
						<div class="controls">
							<input id="newPasswordOne" name="newPasswordOne" class="input-xlarge focused"
								value="" type="password">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="newPasswordTwo">New Password Again</label>
						<div class="controls">
							<input id="newPasswordTwo" name="newPasswordTwo"
								class="input-xlarge focused" value="" type="password">
						</div>
					</div>


				</fieldset>
				<div class="modal-footer" style="height: 15px;">
					<button type="submit" class="btn btn-primary">Change Password</button>
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