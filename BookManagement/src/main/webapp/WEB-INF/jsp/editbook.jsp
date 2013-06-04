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

	<script>
	$(document).ready(function() {
	    // to store it in a variable
	    var loc = window.location.toString();
	    var errorCode = loc.split("#error=")[1];
	    if (errorCode == "1" ) {
	    	toastr.error("Please select a book cover");
	    }
	});
	</script>

	
	<br />
	<div id="content" class="row-fluid span8">
		<div class="row">

			<div id="upload-article-container" class="span8">
				<h2>Edit Book</h2>
				<p>Please correct the information about this book.</p>
				<p style="font-weight:bold;">${error}</p>
				<hr>
				<form name='f' class="form-horizontal"
				action="<c:url value='/admin/bookmanagement/editbook/${book.id}' />"
				method='POST' enctype="multipart/form-data">
				<fieldset>
					<div class="control-group">
						<label class="control-label" for="title">Title</label>
						<div class="controls">
							<input id="title" name="title" class="input-xlarge focused"
								value="${book.title}" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="author">Author</label>
						<div class="controls">
							<input id="author" name="author" class="input-xlarge focused"
								value="${book.author}" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="publisher">Publisher</label>
						<div class="controls">
							<input id="publisher" name="publisher"
								class="input-xlarge focused" value="${book.publisher}" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="isbn">ISBN</label>
						<div class="controls">
							<input id="isbn" name="isbn" class="input-xlarge focused"
								value="${book.isbn}" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="description">Description</label>
						<div class="controls">
							<textarea name="description" id="description" row="5" >${book.description}</textarea>
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="category">Category</label>
						<div class="controls">
							<input id="category" name="category" class="input-xlarge focused"
								value="${book.category}" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="bookcover">BookCover</label>
						<div class="controls">
							<input id="bookcover" name="bookcover"
								class="input-xlarge focused" for="bookcover"
								placeholder="bookcover" type="file">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="buyurl">BuyUrl</label>
						<div class="controls">
							<input id="buyurl" name="buyurl" class="input-xlarge focused"
								value="${book.buyurl}" type="text">
						</div>
					</div>
					
					<div class="control-group">
						<label class="control-label" for="intelPage">Intel Page</label>
						<div class="controls">
							<input id="intelPage" name="intelPage" class="input-xlarge focused"
								value="${book.intelPage}" type="text">
						</div>
					</div>
					
										<div class="control-group">
						<label class="control-label" for="fcsDate">First Customer Shipment Date</label>
						<div class="controls">
							<input id="fcsDate" name="fcsDate" class="input-xlarge focused"
								value="${book.fcsDate}" type="text" >
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="suggestedReading">Suggested
							Reading</label>
						<div class="controls">
							<input id="suggestedReading" name="suggestedReading"
								class="input-xlarge focused" path="suggestedReading"
								checked="yes" type="checkbox">
						</div>
					</div>

				</fieldset>
				<div class="modal-footer" style="height: 15px;">
					<button type="submit" class="btn btn-primary">Update Book</button>
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