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
	<c:if test="${errors != null}">
		<script>toastr.error('Please fill out all sections of the form.', 'Form Error');</script>
	</c:if>

	<c:if test="${success != null}">
		<script>toastr.success('The supplied information has been giving to the PDF Conversion system.', 'PDF Converstion Submitted');</script>
	</c:if>
	
	<c:if test="${status != null}">
		<script>toastr.error("Couldn't connect to PDF Server", 'Server Error');</script>
	</c:if>
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
					
					<div class="control-group">
						<label class="control-label" for="pdf">Output Format</label>
						<div class="controls">
							<select id="format" name="format">
								<option value="epub">EPUB</option>
								<option value="mobi">MOBI</option>
								<option value="rtf">RTF</option>
								<option value="txt">TXT</option>
								<option value="azw3">AZW3</option>
								<option value="fb2">FB2</option>
								<option value="oeb">OEB</option>
								<option value="lit">LIT</option>
								<option value="lrf">LRF</option>
								<option value="htmlz">HTMLZ</option>
								<option value="pdb">PDB</option>
								<option value="pml">PML</option>
								<option value="rb">RB</option>
								<option value="snb">SNB</option>
								<option value="tcr">TCR</option>
								<option value="txtz">TXTZ</option>
							</select>
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