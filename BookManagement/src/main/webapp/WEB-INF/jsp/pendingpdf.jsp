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

	<br />
	<div id="content" class="row-fluid span9">
		<div class="row-fluid">
			<div id="pending-uploads" class="span12">
				<!-- Pending Uploads Table -->

				<div id="content" class="span9 section-body">
					<h1>Pending Conversions</h1>
					<div id="section-body">
						<p>The PDF conversion system is a very time and computation intensive process. On this page you can watch all of the PDF's and thier progress as they travel through the system. If a PDF is no longer listed, that means it has been completed. Completed Conversions are available <a href="/bookmanagement/pastpdf/">here</a></p>
						<br>
						<table class="table table-striped">
		                    <thead>
		                        <tr>
		                            <th>Title</th>
		                            <th>Author</th>
		                            <th>Contact Email</th>
		                            <th>Output Format</th>
		                        </tr>
		                    </thead>
		                    <tbody>
		                    <c:forEach var="pdf" items="${noncompletedPdfs}">
		                        <tr>
		                            <td>${pdf.title}</td> 
									<td>${pdf.author}</td> 
 									<td>${pdf.email}</td>
 									<td>${pdf.format}</td>
		                        </tr>
		                        </c:forEach>
		                    </tbody>
		                </table>
                    	<br>
					</div>
				</div>
				<!-- End Pending Table -->
				<br />
			</div>
			<!-- Row -->
		</div>
	</div>
	<br />
</body>
</html>