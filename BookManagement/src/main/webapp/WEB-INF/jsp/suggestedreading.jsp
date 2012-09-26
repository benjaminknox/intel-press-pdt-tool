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
	<br />
	<div id="content" class="row-fluid span8">
		<c:set var="rowIndex" value="0" scope="page" />
		<c:forEach var="suggestedBook" items="${suggestedBooks}">

			<c:if test="${rowIndex == 0}">
				<div class="row-fluid">
					<ul class="">
			</c:if>
			<li class="span2">
				<div class="thumbnail">
					<img src="http://placehold.it/100x100" alt="">
					<div class="caption">
						<p>${suggestedBook.title}</p>
					</div>
				</div>
			</li>
			<c:if test="${rowIndex == 5}">
				</ul>
				</div>
				<br/>
			<c:set var="rowIndex" value="0" scope="page" />
			</c:if>
			<c:set var="rowIndex" value="${rowIndex + 1}" scope="page" />
	</c:forEach>
				</ul>
			</div>
	</div>
				<br/>
</body>
</html>