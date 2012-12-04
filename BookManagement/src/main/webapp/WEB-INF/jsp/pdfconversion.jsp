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
	<div id="content" class="row-fluid span9">
		<div id="previous-uploads" class="span12"></div>
		<div id="upload-article-container" class="span8">
			<h2>Upload Pdf</h2>
			<p>This page is used to upload new pdf's to be converted. After
				being processed, books will be added to the system, and E-book
				formats will be available for download.</p>
			<p>The email listed as the pdf's contact email will receive an
				email with links to all applicable converted types when the
				conversion process is finished.</p>
			<c:forEach var="error" items="${errors}">
				<p style="font-weight: bold;">${error}</p>
			</c:forEach>
			<hr>
			<form name='f' class="form-horizontal"
				action="<c:url value='/uploadPdf' />" method='POST'
				enctype="multipart/form-data">
				<fieldset>
					<div class="control-group">
						<label class="control-label" for="title">Book Title</label>
						<div class="controls">
							<input id="title" name="title" class="input-xlarge focused"
								placeholder="title" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="author">Book Author</label>
						<div class="controls">
							<input id="author" name="author" class="input-xlarge focused"
								placeholder="author" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="email">Contact Email</label>
						<div class="controls">
							<input id="email" name="email" class="input-xlarge focused"
								placeholder="email" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="pdf">Pdf</label>
						<div class="controls">
							<input id="pdf" name="pdf" class="input-xlarge focused" for="pdf"
								placeholder="pdf" type="file">
						</div>
					</div>
				</fieldset>
				<div class="modal-footer" style="height: 15px;">
					<button type="submit" class="btn btn-primary">Upload Pdf</button>
				</div>
			</form>
		</div>
		<br />
	</div>
	<!-- Row -->

	<br />
</body>
</html>