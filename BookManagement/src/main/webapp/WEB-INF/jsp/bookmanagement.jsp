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
	<div id="content" class="span9 section-body">
		<div id="section-body" class="tabbable">
			<!-- Only required for left/right tabs -->
			<ul class="nav nav-tabs">
				<li class="active"><a href="#tab1" data-toggle="tab">Books</a></li>
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
										<th>Title</th>
										<th>Author</th>
										<th>Publisher</th>
										<th>ISBN</th>
										<th>Category</th>
										<th>SuggestedReading</th>
										<th>Actions</th>
									</tr>
								</thead>
								<tbody>
									<c:forEach var="book" items="${books}">

										<tr class="odd gradeX">
											<td>${book.id}
											<td>${book.title}</td>
											<td>${book.author}</td>
											<td>${book.publisher}</td>
											<td>${book.isbn}</td>
											<td>${book.category}</td>
											<td>${book.suggestedReading}</td>
											<td class="center"><a
												href="<c:url value="/admin/bookmanagement/delbook/${book.id}" />"
												class="btn btn-warning" title="Edit"><i
													class="icon-edit icon-white"></i></a> <a
												href="<c:url value="/admin/bookmanagement/delbook/${book.id}" />"
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
						data-toggle="modal">Create New Book</a>
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
			<h3 id="myModalLabel">Create New Book</h3>
		</div>
		<div class="modal-body">
			<form name='f' class="form-horizontal"
				action="<c:url value='/admin/bookmanagement/addbook' />"
				method='POST'>
				<fieldset>
					<div class="control-group">
						<label class="control-label" for="title">Title</label>
						<div class="controls">
							<input id="title" name="title" class="input-xlarge focused"
								placeholder="title" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="author">Author</label>
						<div class="controls">
							<input id="author" name="author" class="input-xlarge focused"
								placeholder="author" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="publisher">Publisher</label>
						<div class="controls">
							<input id="publisher" name="publisher"
								class="input-xlarge focused" placeholder="publisher" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="isbn">ISBN</label>
						<div class="controls">
							<input id="isbn" name="isbn" class="input-xlarge focused"
								placeholder="isbn" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="description">Description</label>
						<div class="controls">
							<textarea name="description" id="description" row="5">description</textarea>
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="category">Category</label>
						<div class="controls">
							<input id="category" name="category" class="input-xlarge focused"
								placeholder="category" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="bookCoverUrl">BookCover</label>
						<div class="controls">
							<input id="bookCoverUrl" name="bookCoverUrl"
								class="input-xlarge focused" placeholder="bookCoverUrl"
								type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="buyurl">BuyUrl</label>
						<div class="controls">
							<input id="buyurl" name="buyurl" class="input-xlarge focused"
								placeholder="buyurl" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="category">Category</label>
						<div class="controls">
							<input id="category" name="category" class="input-xlarge focused"
								placeholder="category" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="suggestedReading">Suggested
							Reading</label>
						<div class="controls">
							<input id="suggestedReading" name="suggestedReading"
								class="input-xlarge focused" path="suggestedReading"
								placeholder="suggestedReading" type="checkbox">
						</div>
					</div>

				</fieldset>
				<div class="modal-footer" style="height: 15px;">
					<button type="submit" class="btn btn-primary">Create Book</button>
				</div>
			</form>
		</div>
	</div>

</body>
</html>