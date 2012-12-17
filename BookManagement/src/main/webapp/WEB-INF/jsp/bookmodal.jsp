<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="form"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"%>
<%@ taglib prefix="sec"
	uri="http://www.springframework.org/security/tags"%>
	<%@ taglib prefix='fn' uri='http://java.sun.com/jsp/jstl/functions' %>
<html>
<head>
<title>Intel Press Management</title>
<meta name='description' content='A simple page'>
</head>
<body>
	<div class="span5">
		<img src="<c:url value="/uploads/${book.bookcovername }"/>"
			width="100" height="120" align="left" style="padding: 10px;">
		<h3>
			<u>${book.title}</u>
		</h3>
		<p>${book.description}</p>
	</div>
	<c:if test="${fn:length(book.bookChapters) > 0}" >
	
	<table class="table table-bordered table-striped" id="example">
		<thead>
			<tr>
				<th>Number</th>
				<th>Name</th>
				<th>Technical Article</th>
				<th>Assignee</th>
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
						<c:when test="${chapter.technical && chapter.article == null }">
							<td class="center"><center>
									<div title="Technical Article Required and NOT submitted"
										class="btn btn-warning" style="width: 50px">Yes</div>
								</center></td>
						</c:when>
						<c:when test="${chapter.technical && chapter.article != null }">
							<td class="center"><center>
									<div title="Technical Article Required and submitted"
										class="btn btn-success" style="width: 50px">Yes</div>
								</center></td>
						</c:when>
						<c:otherwise>
							<td class="center"><center>
									<div title="No Technical Article Required"
										class="btn btn-danger" style="width: 50px">No</div>
								</center></td>
						</c:otherwise>
					</c:choose>

					<td>${chapter.assignedUser.firstname}</td>

					<c:choose>
						<c:when test="${chapter.technical && chapter.article != null }">
							<td><a class="btn btn-maniadmin-8"
								href="<c:url value="/uploads/${chapter.article.articleName}"/>"><i
									class="icon-circle-arrow-down"></i></a></td>
						</c:when>
						<c:otherwise>
								<td></td>
						</c:otherwise>
					</c:choose>
					<c:choose>
						<c:when test="${chapter.technical && chapter.article == null && user.id == chapter.assignedUser.id}">
							<td class="center"><a title="Upload Article"
								class="btn btn-inverse"
								href="/bookmanagement/uploadArticle/${chapter.id}">
									<i class="icon-white icon-circle-arrow-up"></i>
							</a></td>
						</c:when>
						
						<c:otherwise>
							<!--  Admins can always upload, so make sure we display the button -->
							<sec:authorize access="hasRole('ROLE_ADMIN')">
								<td class="center"><a title="Upload Article"
								class="btn btn-inverse"
								href="/bookmanagement/uploadArticle/${chapter.id}">
									<i class="icon-white icon-circle-arrow-up"></i>
								</a></td>
							</sec:authorize>
							
							<!-- We arent the assigned user or an Admin -->
							<sec:authorize access="!hasRole('ROLE_ADMIN')">
								<td class="center"></td>
							</sec:authorize>
						</c:otherwise>
					</c:choose>
					<sec:authorize access="hasRole('ROLE_ADMIN')">
						<c:choose>
							<c:when test="${chapter.technical}">
								<td>							
								<a title="Assign Article"
									class="btn btn-success"
									href="/bookmanagement/admin/bookmanagement/assignChapter/${chapter.id}">
										<i class="icon-white icon-pencil"></i>
								</a></td>
							</c:when>
						</c:choose>
					</sec:authorize>
				</tr>
			</c:forEach>
		</tbody>
	</table>
	</c:if>
	<div class="span5">
		<br /> <a href="${book.buyurl}" target="_blank">
			<button type="button" class="btn btn-primary" data-toggle="button">Buy
				Now</button>
		</a>
	</div>
	<br />

</body>
</html>