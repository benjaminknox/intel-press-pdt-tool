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
				<h2>Reset Password</h2>
				<p>if you are sure that you would like to reset  <b>${user.username}</b>'s password please click the bellow button.</p>
				<p>The new password will be <b>1234</b></p>
				<hr>
				<form name='f' class="form-horizontal"
				action="<c:url value='/admin/usermanagement/resetpassword/${user.id}' />"
				method='POST' enctype="multipart/form-data">
				<div class="modal-footer" style="height: 15px;">
					<button type="submit" class="btn btn-primary">Update User</button>
				</div>
			</form>
			</div>
			<br />
			<a class="btn" href="/bookmanagement/admin/bookmanagement/" >Back</a>
		</div>
		<!-- Row -->
	</div>
	<br />

</body>
</html>