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
		
	</script>
	<br />
	<div id="content" class="row-fluid span8">
		<div class="row row-fluid">
			<div class="span2">
				<h1>${book.title}</h1>

				<div class="thumbnail">
					<img src="<c:url value="/uploads/${book.bookcovername}"/>"
						width="100" height="120">
				</div>
			</div>

			<div id="chapter-list-container row-fluid" class="span9">
				<h2>Chapters</h2>
				
				<table class="table table-bordered table-striped" >
					<thead>
						<tr>
							<th>Number</th>
							<th>Name</th>
							<th>Technical Article Required</th>
							<th>Article</th>
							<th>Actions</th>
						</tr>
					</thead>
					<tbody>
						<c:forEach var="chapter" items="${book.bookChapters}">
							<tr class="odd gradeX">
								<td>${chapter.chapterNumber}</td>
								<td>${chapter.name}</td>
								<c:choose>
									<c:when test="${chapter.technical}">
										<td class="center"><div title="Technical Article Required" class="btn btn-success">
												<i class="icon-white icon-thumbs-up"></i>
											</div></td>
									</c:when>
									<c:otherwise>
										<td class="center"><div title="No Technical Article Required" class="btn btn-danger">
												<i class="icon-white  icon-thumbs-down"></i>
											</div></td>
									</c:otherwise>
								</c:choose>
								<td>${chapter.article}</td>
								<td class="center">
								<a href="<c:url value="/admin/bookmanagement/editchapter/${chapter.id}" />"
												class="btn btn-warning" title="Edit"><i
													class="icon-edit icon-white"></i></a> <a
									href="<c:url value="/admin/bookmanagement/deleteChapter/${chapter.id}" />"
									class="btn btn-danger" title="Remove"><i
										class="icon-remove icon-white"></i></a></td>

							</tr>
						</c:forEach>
					</tbody>
				</table>
				
			</div>
			
			
			
			
			<br />
		</div>
		<br />
		<div class="row row-fluid">
			<div class="span6" align="left">
				<a class="btn" href="/bookmanagement/admin/bookmanagement/" >Back</a>
			</div>
			<div class="span6" align="right">
				<a href="#addChapter" role="button" class="btn" data-toggle="modal">Add
					Chapter</a>
			</div>
		</div>
			<br />
		<!-- Row -->
	</div>
	<br />


	<!-- Create User MODAL -->
	<div class="modal hide fade" id="addChapter" tabindex="-1"
		role="dialog" aria-labelledby="myModalLabel" aria-hidden="true">
		<div class="modal-header">
			<button type="button" class="close" data-dismiss="modal"
				aria-hidden="true">×</button>
			<h3 id="myModalLabel">Add Chapter</h3>
		</div>
		<div class="modal-body">
			<form name='f' class="form-horizontal"
				action="<c:url value='/admin/bookmanagement/addChapter' />"
				method='POST' enctype="multipart/form-data">
				<fieldset>
					<div class="control-group">
						<label class="control-label" for="name">Name</label>
						<div class="controls">
							<input id="name" name="name" class="input-xlarge focused"
								placeholder="name" type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="chapterNumber">Chapter
							Number</label>
						<div class="controls">
							<input id="chapterNumber" name="chapterNumber"
								class="input-xlarge focused" placeholder="chapterNumber"
								type="text">
						</div>
					</div>

					<div class="control-group">
						<label class="control-label" for="technical">Has Technical
							Article</label>
						<div class="controls">
							<input id="technical" name="technical"
								class="input-xlarge focused" path="technical"
								placeholder="technical" type="checkbox">
						</div>
					</div>
					<input type="hidden" id="book_id" name="book_id" value="${book.id}">

				</fieldset>
				<div class="modal-footer" style="height: 15px;">
					<button type="submit" class="btn btn-primary">Create
						Chapter</button>
				</div>
			</form>
		</div>
	</div>

</body>
</html>