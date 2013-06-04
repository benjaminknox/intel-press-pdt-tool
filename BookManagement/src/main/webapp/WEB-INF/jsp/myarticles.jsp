<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%>
<%@ taglib uri="http://www.springframework.org/tags/form" prefix="form"%>
<%@ page language="java" contentType="text/html; charset=UTF-8"%>
<%@ taglib prefix="sec"
	uri="http://www.springframework.org/security/tags"%>
	<%@ taglib uri="http://java.sun.com/jsp/jstl/functions" prefix="fn"%>
	
<html>
<head>
<title>Article Management</title>
<meta name='description' content=''>
</head>
<body>
	<c:if test="${success != null}" >
		<script>toastr.success('${success}');</script>
	</c:if>
	<c:if test="${fn:length(errors) > 0}" >
		<script>toastr.error('Please correct the form errors');</script>
	</c:if>
	<br />
	<div id="content" class="row-fluid span8">
		
		<div class="row">
			<h1>My Assigned Articles</h1>
			<br>
			<p>This page will display all of the articles that you have been assigned.</p>
			<br>
			<div class="well">
			<c:if test="${fn:length(assigedArticles) > 0}" >
	
				<table class="table table-bordered table-striped" id="example">
					<thead>
						<tr>
							<th>Number</th>
							<th>Name</th>
							<th>Technical Article</th>
							<th>Assignee</th>
							<th>Article Doc</th>
							<th>Article Pdf</th>
							<th>Actions</th>
						</tr>
					</thead>
					<tbody>
						<c:forEach var="chapter" items="${assigedArticles}">
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
												
										<td><a class="btn btn-maniadmin-8"
											href="<c:url value="/uploads/${chapter.article.articlePdfName}"/>"><i
												class="icon-circle-arrow-down"></i></a></td>
									</c:when>
									<c:otherwise>
											<td></td>
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
				<c:if test="${fn:length(assigedArticles) == 0}" >
					<p>You have not been assigned any articles.</p>
				</c:if>
			</div>
			<a class="btn" href="/bookmanagement/" >Back</a>
			<br>
		</div>
		<!-- Row -->
	</div>
	<br />

</body>
</html>