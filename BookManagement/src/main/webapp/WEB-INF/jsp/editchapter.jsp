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
				<h2>Edit Chapter</h2>
				<p>Please correct the information about this chapter.</p>
				<p style="font-weight:bold;">${error}</p>
				<hr>
				<form name='f' class="form-horizontal"
				action="<c:url value='/admin/bookmanagement/editchapter/${chapter.id}' />"
				method='POST' enctype="multipart/form-data">
				<fieldset>
					<div class="control-group">
						<label class="control-label" for="name">Name</label>
						<div class="controls">
							<input id="name" name="name" class="input-xlarge focused"
								value="${chapter.name}" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="chapterNumber">Chapter
							Number</label>
						<div class="controls">
							<input id="chapterNumber" name="chapterNumber"
								class="input-xlarge focused" value="${chapter.chapterNumber}"
								type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="technical">Has Technical
							Article</label>
						<div class="controls">
							<input id="technical" name="technical"
								class="input-xlarge focused" path="technical"
								
								<c:if test="${chapter.technical}" >
								checked="yes" 
								</c:if>
								
								type="checkbox">
						</div>
					</div>

				</fieldset>
				<div class="modal-footer" style="height: 15px;">
					<button type="submit" class="btn btn-primary">Update Chapter</button>
				</div>
			</form>
			</div>
			<br />
						<a class="btn" href="/bookmanagement/admin/bookmanagement/chapters/${chapter.book.id}" >Back</a>
		</div>
		<!-- Row -->
	</div>
	<br />

</body>
</html>