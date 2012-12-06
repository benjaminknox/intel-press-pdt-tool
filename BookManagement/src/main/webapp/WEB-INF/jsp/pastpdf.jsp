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
					<h1>Completed Conversions</h1>
					<div id="section-body">
						<p>Below are all of the PDF's that have been completed. You can re-download any of these at your convenience. </p>
						<br>
						<div class="tab-content">
							<div class="tab-pane active" id="tab1">
								<div class="row-fluid">
									<!--Tabs2-->
									<div class="span12">
										<table class="table table-bordered table-striped pull-left"
											id="example">
											<thead>
												<tr>
													<th>Title</th>
													<th>Author</th>
													<th>Contact Email</th>
													<th>Output Format</th>
													<th>Actions</th>
												</tr>
											</thead>
											<tbody>
												<c:forEach var="pdf" items="${completedPdfs}">
													<tr class="odd gradeX">
														<td>${pdf.title}</td>
														<td>${pdf.author}</td>
														<td>${pdf.email}</td>
														<td>${pdf.format}</td>
														<td class="center"><a
															href="<c:url value="/downloadepub/${pdf.id}" />"
															class="btn btn-success" title="Download"><i
																class="icon-arrow-down icon-white"></i></a></td>
													</tr>
												</c:forEach>
											</tbody>
										</table>
									</div>
								</div>
							</div>
						</div>



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