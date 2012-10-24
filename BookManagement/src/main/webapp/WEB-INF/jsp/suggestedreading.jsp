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
		function findBook(id) {

			$.get('<c:url value="/getBook/" />' + id, function(data) {
				$('.book-modal').html(data);
				//$('#myModal').css("left", Math.max(0, (($(window).width() - $('#myModal').outerWidth()) / 2) + $(window).scrollLeft()) + "px");
				$('#myModal').modal('show');
			});

		}
	</script>
	<br />
	<div id="content" class="row-fluid span8">
		<c:set var="rowIndex" value="0" scope="page" />
		<c:forEach var="suggestedBook" items="${suggestedBooks}">

			<c:if test="${rowIndex == 0}">
				<div class="row-fluid">
					<ul class="">
			</c:if>
			<li class="span2 book"><a id="findBook"
				href="javascript:findBook('${suggestedBook.id}');">
					<c:set var="articlesToDo" value="false" scope="page" />
					<c:forEach var="chapter" items="${suggestedBook.bookChapters}">
						<c:if test="${chapter.technical && chapter.article == null}">
							<c:set var="articlesToDo" value="true" scope="page" />
						</c:if>
					</c:forEach>
					
					<c:if test="${articlesToDo}" >
						<div class="thumbnail bookmark-red" title="More technical chapters exist">
					</c:if>
					<c:if test="${!articlesToDo}" >
						<div class="thumbnail bookmark-blue" title="All technical articles have been completed" >
					</c:if>
						<img
							src="<c:url value="/uploads/${suggestedBook.bookcovername}"/>"
							width="120" height="120">
						<div class="caption">
							<div align="center">
								<p>${suggestedBook.title}</p>
							</div>
						</div>
					</div>
			</a></li>
			<c:if test="${rowIndex == 5}">
				</ul>
	</div>
	<br />
	<c:set var="rowIndex" value="0" scope="page" />
	</c:if>
	<c:set var="rowIndex" value="${rowIndex + 1}" scope="page" />
	</c:forEach>
	</ul>
	</div>
	<br>
	</div>


	<div class="modal hide" id="myModal" tabindex="-1" role="dialog"
		aria-labelledby="myModalLabel" aria-hidden="true"  >
		<div class="modal-header ">
			<button type="button" class="close" data-dismiss="modal"
				aria-hidden="true">×</button>
			<h3 id="myModalLabel">Book Info</h3>
		</div>
		<div class="modal-body book-modal">
			<p>One fine body…</p>
		</div>
		<div class="modal-footer">
			<button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>
		</div>
	</div>

</body>
</html>