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
	$(document).ready(function() {
	    // to show it in an alert window
	    //alert(window.location);

	    // to store it in a variable
	    var loc = window.location.toString();
	    var errorCode = loc.split("#error=")[1];
	    if (errorCode == "1" ) {
	    	$("#errors").text("The file extension for the uploaded article is not on the approved list.");
	    }
	    if (errorCode == "2" ) {
	    	$("#errors").text("Please enter a article title, and select an article.");
	    }
	    if (errorCode == "3" ) {
	    	$("#errors").text("Please select an article.");
	    }
	});
	</script>
	<br />
	<div id="content" class="row-fluid span8">
		<div class="row">
			<div class="span4">
				<h1>${chapter.book.title}</h1>
				<h3><i>${chapter.name}</i></h3>
				<div class="thumbnail">
					<img src="<c:url value="/uploads/${chapter.book.bookcovername}"/>"
						width="100" height="120">
				</div>
			</div>

			<div id="upload-article-container" class="span8">
				<h2>Upload Article</h2>
				<div id="errors"></div>
				<hr>
				<form name='f' class="form-horizontal"
				action="<c:url value='/addArticle/${chapter.id}' />"
				method='POST' enctype="multipart/form-data">
				<fieldset>
					<div class="control-group">
						<label class="control-label" for="title">Article Title</label>
						<div class="controls">
							<input id="title" name="title" class="input-xlarge focused"
								placeholder="title" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="article">Article</label>
						<div class="controls">
							<input id="article" name="article"
								class="input-xlarge focused" for="article"
								placeholder="article" type="file">
						</div>
					</div>
					
				</fieldset>
				<div class="modal-footer row-fluid" style="height: 15px;">
				<div class="span1" >
				<a class="btn" class="span6" href="/bookmanagement/suggestedreading" > Back
				</a>
				</div>
					<div class="span10">
					<button type="submit" class="btn btn-primary">Upload Article</button>
					</div>
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