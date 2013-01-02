<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="form"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"%>
<%@ taglib prefix="sec"
	uri="http://www.springframework.org/security/tags"%>
<html>
<head>
<title>Intel Press Management</title>
<meta name='description' content='A simple page'>
</head>
<body>
	<script>
	function deleteBook (bookId) {
		
		var choice = confirm("Are you sure you want to delete this user?");
		
		if(bookId != "" && choice) {
			window.location.href = "/bookmanagement/admin/usermanagement/deluser/"+bookId;
		}
	}
	
	</script>
	<script>
	$(document).ready(function() {
	    // to show it in an alert window
	    //alert(window.location);

	    // to store it in a variable
	    var loc = window.location.toString();
	    var successCode = loc.split("#success=")[1];
	    if (successCode == "1" ) {
	    	toastr.success("Succesfully reset password");
	    }
	});
	</script>

	<!--/span-->
	<div id="content" class="span9 section-body">
		<div id="section-body" class="tabbable">
			<!-- Only required for left/right tabs -->
			<ul class="nav nav-tabs">
				<li class="active"><a href="#tab1" data-toggle="tab">Users</a></li>
			</ul>
			<div class="tab-content">
				<div class="tab-pane active" id="tab1">
					<div class="row-fluid">
						<!--Tabs2-->
						<div class="span12">
							<table class="table table-bordered table-striped pull-left"
								id="example">
								<thead>
									<tr>
										<th>ID</th>
										<th>Username</th>
										<th>Enabled</th>
										<th>Actions</th>
									</tr>
								</thead>
								<tbody>
									<c:forEach var="user" items="${users}">

										<tr class="odd gradeX">
											<td>${user.id}
											<td>${user.username}</td>
											<td>${user.enabled}</td>
											<td class="center"><a
												href="<c:url value="/admin/usermanagement/resetpassword/${user.id}" />"
												class="btn btn-info" title="Reset Password"><i
													class="icon-retweet icon-white"></i></a> <a
												href="<c:url value="/admin/usermanagement/edituser/${user.id}" />"
												class="btn btn-warning" title="Edit"><i
													class="icon-edit icon-white"></i></a> <a
												href="<c:url value="javascript:deleteBook('${user.id}')" />"
												class="btn btn-danger" title="Remove"><i
													class="icon-remove icon-white"></i></a></td>
													
													
										</tr>
									</c:forEach>
								</tbody>
							</table>
						</div>
					</div>
				</div>

				<div align="right">
					<a href="#createNewUser" role="button" class="btn"
						data-toggle="modal">Create New User</a>
				</div>

			</div>
		</div>
	</div>

	<!-- Create User MODAL -->
	<div class="modal hide fade" id="createNewUser" tabindex="-1"
		role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
		<div class="modal-header">
			<button type="button" class="close" data-dismiss="modal"
				aria-hidden="true">×</button>
			<h3 id="myModalLabel">Create New User</h3>
		</div>
		<div class="modal-body">
			<form name='f' class="form-horizontal"
				action="<c:url value='/admin/usermanagement/adduser' />"
				method='POST'>
				<fieldset>
					<div class="control-group">
						<label class="control-label" for="firstname">Firstname</label>
						<div class="controls">
							<input id="firstname" name="firstname"
								class="input-xlarge focused" placeholder="firstname" type="text">
						</div>
					</div>
					<div class="control-group">
						<label class="control-label" for="lastname">Lastname</label>
						<div class="controls">
							<input id="lastname" name="lastname" class="input-xlarge focused"
								placeholder="lastname" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="email">Email</label>
						<div class="controls">
							<input id="email" name="email" class="input-xlarge focused"
								placeholder="email" type="text">
						</div>
					</div>
					<div class="control-group">
						<label class="control-label" for="password">Password</label>
						<div class="controls">
							<input id="password" name="password" type="password"
								class="input-xlarge focused" placeholder="password"
								autocomplete="off">
						</div>
					</div>
				</fieldset>
				<div class="modal-footer" style="height: 15px;">
					<button type="submit" class="btn btn-primary">Create User</button>
				</div>
			</form>
		</div>
	</div>

</body>
</html>