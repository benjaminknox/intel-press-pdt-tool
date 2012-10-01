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
	function findBook(id) {
		
			$.get('<c:url value="/getBook/" />'+id, function(data) {
				$('.modal-body').html(data);
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
				href="javascript:findBook(${suggestedBook.id});">

					<div class="thumbnail">
						<img src="http://placehold.it/100x100" alt="">
						<div class="caption">
							<p>${suggestedBook.title}</p>
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
	</div>
	<br />


	<div class="modal hide" id="myModal" tabindex="-1" role="dialog"
		aria-labelledby="myModalLabel" aria-hidden="true">
		<div class="modal-header">
			<button type="button" class="close" data-dismiss="modal"
				aria-hidden="true">×</button>
			<h3 id="myModalLabel">Book Info</h3>
		</div>
		<div class="modal-body">
			<p>One fine body…</p>
		</div>
		<div class="modal-footer">
			<button class="btn" data-dismiss="modal" aria-hidden="true">Close</button>
		</div>
	</div>

</body>
</html>