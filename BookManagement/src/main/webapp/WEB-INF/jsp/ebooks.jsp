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
				<h2>Mangage Ebooks</h2>
				<p>Please Upload any types of e-book necessary for this Book!</p>
				<hr>
				<form name='f' class="form-horizontal"
				action="<c:url value='/admin/pdfmanagement/uploadebook' />"
				method='POST' enctype="multipart/form-data">
				<fieldset> 
				
				<c:if test="${pdf.epubFileName != null}">
					<div class="control-group">
						<label class="control-label" for="epub">Current EPUB</label>
						<div class="controls">
							<a href="<c:url value='/downloadepub/${pdf.id}' />">${pdf.epubFileName}</a>
						</div>
					</div>
				</c:if>
				
					<div class="control-group">
						<label class="control-label" for="epub">EPUB Format</label>
						<div class="controls">
							<input id="epub" name="epub"
								class="input-xlarge focused" for="epub"
								placeholder="epub" type="file">
						</div>
					</div>
					
					<hr>
				
				<c:if test="${pdf.mobiFileName != null}">
					<div class="control-group">
						<label class="control-label" for="epub">Current MOBI</label>
						<div class="controls">
							<a href="<c:url value='/downloadmobi${pdf.id}' />">${pdf.mobiFileName}</a>
						</div>
					</div>
				</c:if>
				
					<div class="control-group">
						<label class="control-label" for="mobi">MOBI Format</label>
						<div class="controls">
							<input id="mobi" name="mobi"
								class="input-xlarge focused" for="mobi"
								placeholder="mobi" type="file">
						</div>
					</div>
					
					<input type="hidden" name="pdf" value="${pdf.id}">
					
				</fieldset>
				<div class="modal-footer" style="height: 15px;">
					<button type="submit" class="btn btn-primary">Upload Ebooks</button>
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