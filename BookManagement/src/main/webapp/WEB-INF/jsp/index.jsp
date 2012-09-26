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
				<li class="active"><a href="#tab1" data-toggle="tab">Inbox</a></li>
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
										<th>From</th>
										<th>Subject</th>
										<th>Date</th>
										<th>Actions</th>
									</tr>
								</thead>
								<tbody>
									<tr class="odd gradeX">
										<td><img alt="" src="img/small/thumb1.png" />
											ab.alhyane@gmail.com</td>
										<td>Project</td>
										<td><small>12/02/2012</small></td>
										<td class="center"><a href="#" class="btn btn-danger"
											title="Remove"><i class="icon-remove icon-white"></i></a> <a
											href="#" class="btn btn-maniadmin-8" title="Archive"><i
												class="icon-inbox"></i></a></td>
									</tr>
								</tbody>
							</table>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</body>
</html>