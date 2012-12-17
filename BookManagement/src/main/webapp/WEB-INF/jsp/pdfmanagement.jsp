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
	<!--/span-->
	<!-- User Roles Table: -->
	<div id="content" class="span9 section-body">
		<div id="section-body" class="tabbable">
			<!-- Only required for left/right tabs -->
			<ul class="nav nav-tabs">
				<li class="active"><a href="#tab1" data-toggle="tab">All Pdfs Uploaded</a></li>
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
										<th>Title</th>
										<th>Author</th>
										<th>ISBN</th>
										<th>Actions</th>
									</tr>
								</thead>
								<tbody>
									<c:forEach var="pdf" items="${pdfs}">
										<tr class="odd gradeX">
											<td>${pdf.title}</td>
											<td>${pdf.author}</td>
											<td>${pdf.isbn}</td>
											<td class="center"><a
												href="<c:url value="/admin/pdfmanagement/delpdf/${pdf.id}" />"
												class="btn btn-danger" title="Remove"><i
													class="icon-remove icon-white"></i></a></td>
										</tr>
									</c:forEach>
								</tbody>
							</table>
						</div>
					</div>
				</div>
			</div>
		</div>
		<div align="right">
		</div>
		<br />
	</div>

	<!-- Create New Role MODAL -->
	<div class="modal hide fade" id="createNewRole" tabindex="-1"
		role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
		<div class="modal-header">
			<button type="button" class="close" data-dismiss="modal"
				aria-hidden="true">×</button>
			<h3 id="myModalLabel">Create New Role</h3>
		</div>
		<div class="modal-body">
			<form name='f' class="form-horizontal"
				action="<c:url value='/admin/rolemanagement/createrole' />"
				method='POST'>
				<fieldset>
					<div class="control-group">
						<label class="control-label" for="authority">Role Name</label>
						<div class="controls">
							<input id="authority" name="authority"
								class="input-xlarge focused" placeholder="ROLE_EXAMPLE"
								type="text">
						</div>
					</div>
				</fieldset>
				<div class="modal-footer" style="height: 15px;">
					<button type="submit" class="btn btn-primary">Create Role</button>
				</div>
			</form>
		</div>
	</div>

	<!-- Add Role To User MODAL -->
	<div class="modal hide fade" id="addRoleToUser" tabindex="-1"
		role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
		<div class="modal-header">
			<button type="button" class="close" data-dismiss="modal"
				aria-hidden="true">×</button>
			<h3 id="myModalLabel">Add Role To User</h3>
		</div>
		<div class="modal-body">
			<form name='f' class="form-horizontal"
				action="<c:url value='/admin/rolemanagement/addroletouser' />"
				method='POST'>
				<fieldset>

					<div class="control-group">
						<label class="control-label" for="username">User:</label>
						<div class="controls">
							<select id="username" name="username" multiple="multiple">
								<c:forEach var="user" items="${users}">
									<option>${user.username}</option>
								</c:forEach>
							</select>
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="role">Role:</label>
						<div class="controls">
							<select id="role" name="role" multiple="multiple">
								<c:forEach var="role" items="${roles}">
									<option>${role.authority}</option>
								</c:forEach>
							</select>
						</div>
					</div>
				</fieldset>
				<div class="modal-footer" style="height: 15px;">
					<button type="submit" class="btn btn-primary">Add Role To
						User</button>
				</div>
			</form>
		</div>
	</div>
</body>
</html>