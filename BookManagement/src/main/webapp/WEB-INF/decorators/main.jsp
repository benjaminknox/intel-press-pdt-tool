<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%><%@ taglib
	uri="http://www.springframework.org/tags/form" prefix="form"%><%@ page
	language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
<%@ taglib prefix="sec"
	uri="http://www.springframework.org/security/tags"%>
<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="utf-8" />
<title><sitemesh:write property='title' /></title>
<meta name="viewport" content="width=device-width, initial-scale=1.0" />
<meta name="description" content="" />
<meta name="author" content="" />
<!-- Le styles -->
<!-- bootstrap css -->
<link href="/bookmanagement/css/bootstrap.min.css" rel="stylesheet" />
<!-- base css -->
<link class="links-css" href="/bookmanagement/css/darkblue.css"
	rel="stylesheet" />
	
	<script src="/bookmanagement/js/jquery.min.js"></script>

<!-- inbox page css -->
<link href="/bookmanagement/css/inbox.css" rel="stylesheet" />
<link rel="icon" type="image/png" href="/bookmanagement/img/Intel.png">
      
<style type="text/css">
body {
	padding-top: 60px;
	padding-bottom: 40px;
}

.sidebar-nav {
	padding: 9px 0;
}
</style>
<!-- responsive css -->
<link href="/bookmanagement/css/bootstrap-responsive.css"
	rel="stylesheet" />
<!-- media query css -->
<link href="/bookmanagement/css/media-fluid.css" rel="stylesheet" />
<!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
<!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
      <![endif]-->
<sitemesh:write property='head' />
</head>
<body>
	<div class="navbar navbar-fixed-top">
		<div class="navbar-inner">
			<div class="container-fluid">
				<a class="btn btn-navbar" data-toggle="collapse"
					data-target=".nav-collapse"> <span class="icon-bar"></span> <span
					class="icon-bar"></span> <span class="icon-bar"></span>
				</a> <a class="brand" href="/bookmanagement/"><img
					src="/bookmanagement/img/logo-small.png" alt="logo" /></a>
				<ul class="nav pull-left bar-root">
					<li class="divider-vertical"></li>
				</ul>
				<div class="group-menu nav-collapse">
					<ul class="nav pull-right">
						<li class="divider-vertical"></li>
						<li class="dropdown"><a data-toggle="dropdown" href="#">
								Hello: <sec:authentication property="principal.username" /> <b
								class="caret"></b>
						</a>
							<ul class="dropdown-menu">
								<li>
									<div id="profileModal">
										
										<div class="modal-footer">
											<center><a class="btn btn-info"
												href="<c:url value="/j_spring_security_logout" />">Logoff</a>
												</center>
										</div>
									</div>
								</li>
							</ul></li>
					</ul>
					<!--<form action="#" class="navbar-search pull-right">
						<input type="text" placeholder="Search" class="search-query span2" />
					</form> -->
				</div>
			</div>
		</div>
	</div>
	<div class="container-fluid">
		<div class="row-fluid">
			<div id="menu-left" class="span3">
				<div class="sidebar-nav">
					<ul class="nav nav-list">
						<li><a href="<c:url value="/suggestedreading"/>"><i
								class="icon-th"></i><span>Book Management</span></a></li>
						<li><a href="<c:url value="/" />"><i
								class="icon-th-large"></i><span>Statistics</span></a></li>
						<li><a href="<c:url value="/pdfconversion"/>"><i class="icon-list-alt"></i><span>
									PDF Conversion</span></a></li>
						<sec:authorize access="hasRole('ROLE_ADMIN')">
							<li class="accordion-menu"><a href="#collapseOne"
								data-toggle="collapse" class="accordion-toggle"><i
									class="icon-warning-sign"></i><span> Admin <i
										class="icon-chevron-down pull-right"></i></span></a>
								<div class="accordion-body collapse dropdown" id="collapseOne">
									<div class="accordion-inner">
										<ul class="nav nav-list">
											<li><a href="<c:url value="/admin/usermanagement/" />">User
													Management</a></li>
											<li><a href="<c:url value="/admin/rolemanagement/" />">Role
													Management</a></li>
											<li><a href="<c:url value="/admin/bookmanagement/" />">Book
													Management</a></li>
											<li><a href="<c:url value="/admin/pdfmanagement/" />">Pdf
													Management</a></li>
										</ul>
									</div>
								</div></li>
						</sec:authorize>
					</ul>
					<div class="togglemenuleft"></div>
				</div>
				<!--/.well -->
			</div>
			<sitemesh:write property='body' />
		</div>
		<footer>
			<p>
				<strong>&copy; Cummings Engineering 2012</strong>
			</p>
		</footer>

	</div>
	<!-- Le javascript
         ================================================== -->
	<!-- Placed at the end of the document so the pages load faster -->
	<script src="/bookmanagement/js/jquery.min.js"></script>
	<script src="/bookmanagement/js/bootstrap.min.js"></script>
	<script src="/bookmanagement/js/jquery.dataTables.js"></script>
	<script src="/bookmanagement/js/jquery-ui.min.js"></script>
	<script type="text/javascript">
		$(document).ready(function() {

			$('#menu-left a').click(function() {
				$('#menu-left').find('a').removeClass('active');
				$(this).addClass('active');
			});
			$('a').tooltip('hide');
			// sort table 
			$('#example').dataTable();
			$('a.style').click(function() {
				var style = $(this).attr('href');
				$('.links-css').attr('href', 'css/' + style);
				return false;
			});

			// switch style 
			$(".switcher").click(function() {
				if ($(this).find('i').hasClass('icon-circle-arrow-right'))
					$('.theme').animate({
						left : '0px'
					}, 500);
				else
					$('.theme').animate({
						left : '-89'
					}, 500);

				$(this).find('i').toggleClass('icon-circle-arrow-right');
				$(this).find('i').toggleClass('icon-circle-arrow-left');
			});
		});
	</script>
</body>
</html>