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
	<div class="span9">
		<img src="<c:url value="/uploads/${book.bookcovername }"/>"
			width="100" height="120" align="left" style="padding: 10px;">

		<h3>
			<u>${book.title }</u>
		</h3>
		${book.description}
	</div>

	<div class="span9">
		<br /> <a href="${book.buyurl}" target="_blank">
			<button type="button" class="btn btn-primary" data-toggle="button">Buy
				Now</button>
		</a>
	</div>
	<br />

</body>
</html>