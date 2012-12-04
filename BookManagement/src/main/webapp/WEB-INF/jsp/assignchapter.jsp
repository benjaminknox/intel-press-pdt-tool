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
				<h2>Assign Article</h2>
				<p>Please select an author who you would like to make responsible for this chapter</p>
				<p style="font-weight:bold;">${error}</p>
				<hr>
				<form name='f' class="form-horizontal"
				action="/bookmanagement/admin/bookmanagement/assignChapter"
				method='POST'>
				<fieldset>
					<div class="control-group">
						<label class="control-label" for="title">Author</label>
						<div class="controls">
							<select name="author">
								<c:forEach var="user" items="${users}" >
									<option value="${user.id}">${user.firstname} ${user.lastname}</option>
								</c:forEach>
							</select>
						</div>
					</div>
					<input type="hidden" name="chapterId" value="${chapter.id}" >
				</fieldset>
				<div class="modal-footer" style="height: 15px;">
					<button type="submit" class="btn btn-primary">Assign</button>
				</div>
			</form>
			</div>
			<br />
		</div>
		<!-- Row -->
	</div>
	<br />

</body>
</html>