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
<link href="css/bootstrap.min.css" rel="stylesheet" />
<!-- base css -->
<link class="links-css" href="css/darkblue.css" rel="stylesheet" />
<!-- inbox page css -->
<link href="css/inbox.css" rel="stylesheet" />
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
<link href="css/bootstrap-responsive.css" rel="stylesheet" />
<!-- media query css -->
<link href="css/media-fluid.css" rel="stylesheet" />
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
				</a> <a class="brand" href="index.html"><img
					src="img/logo-small.png" alt="logo" /></a>
				<ul class="nav pull-left bar-root">
					<li class="divider-vertical"></li>
					<li><a href="chat.html"><i class="icon-comment icon-white"></i><span
							class="label label-important">6</span></a></li>
					<li class="dropdown"><a href="#" data-toggle="dropdown"> <i
							class="icon-envelope icon-white"></i><span
							class="label label-important">5 new</span></a>
						<ul class="dropdown-menu">
							<li><a href="inbox.html"> <img
									src="img/small/thumb1.png" alt="" /> Subject : Project
									<p class="help-block">
										<small>From: ab.alhyane@gmail.com</small>
									</p> <span class="label">23/09/2012</span>
							</a></li>
							<li class="divider"></li>
							<li><a href="inbox.html"> <img
									src="img/small/thumb2.png" alt="" /> Subject : Film
									<p class="help-block">
										<small>From: ab.alhyane@gmail.com</small>
									</p> <span class="label">21/04/2012</span>
							</a></li>
							<li class="divider"></li>
							<li><a href="inbox.html"> <img
									src="img/small/thumb3.png" alt="" /> Subject : Meeting
									<p class="help-block">
										<small>From: ab.alhyane@gmail.com</small>
									</p> <span class="label">20/02/2012</span>
							</a></li>
							<li class="divider"></li>
							<li><a href="inbox.html"> <img
									src="img/small/thumb4.png" alt="" /> Subject : Tasks
									<p class="help-block">
										<small>From: y.kostali@gmail.com</small>
									</p> <span class="label">19/01/2012</span>
							</a></li>
							<li class="divider"></li>
							<li class="active"><a href="inbox.html"> Show All </a></li>
						</ul></li>
					<li class="dropdown"><a href="#" data-toggle="dropdown"> <i
							class="icon-refresh icon-white"></i><span
							class="label label-info">3 Updates</span></a>
						<ul class="dropdown-menu">
							<li><a href="#"> Theme </a></li>
							<li><a href="#"> Components</a></li>
							<li><a href="#"> Plugins</a></li>
							<li class="divider"></li>
							<li class="active"><a href="#"> Show All </a></li>
						</ul></li>
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
									<div class="modal-header">
										<h3>Todo</h3>
									</div>
									<div class="modal-body">
										<div class="row">
											<div class="span1">
												<p>Todo</p>
											</div>
										</div>
									</div>
									<div class="modal-footer">
										<a class="btn btn-info"
											href="<c:url value="j_spring_security_logout" />">Logoff</a>
									</div>
								</li>
							</ul></li>
					</ul>
					<form action="#" class="navbar-search pull-right">
						<input type="text" placeholder="Search" class="search-query span2" />
					</form>
				</div>
			</div>
		</div>
	</div>
	<div class="container-fluid">
		<div class="row-fluid">
			<div id="menu-left" class="span3">
				<div class="sidebar-nav">
					<ul class="nav nav-list">
						<li><a href="index.html"><i class="icon-th-large"></i><span>
									Dashboard</span></a></li>
						<li><a href="widget.html"><i class="icon-th"></i><span>
									Widgets</span></a></li>
						<li><a href="tables.html"><i class="icon-list-alt"></i><span>
									Tables</span></a></li>
						<sec:authorize access="hasRole('ROLE_ADMIN')">
							<li class="accordion-menu"><a href="#collapseOne"
								data-toggle="collapse" class="accordion-toggle"><i
									class="icon-warning-sign"></i><span> Admin <i
										class="icon-chevron-down pull-right"></i></span></a>
								<div class="accordion-body collapse dropdown" id="collapseOne">
									<div class="accordion-inner">
										<ul class="nav nav-list">
											<li><a href="<c:url value="usermanagement" />">User Management</a></li>
											<li><a href="<c:url value="bookmanagement" />">Book Management</a></li>
										</ul>
									</div>
								</div></li>
						</sec:authorize>
					</ul>
					<div class="togglemenuleft">
						<a class="toggle-menu"><i
							class="icon-circle-arrow-left icon-white"></i></a>
					</div>
				</div>
				<!--/.well -->
			</div>
			<sitemesh:write property='body' />
		</div>
		<footer>
			<p>
				<strong>&copy; Maniadmin 2012</strong>
			</p>
		</footer>

	</div>
	<!-- Le javascript
         ================================================== -->
	<!-- Placed at the end of the document so the pages load faster -->
	<script src="js/jquery.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/jquery.dataTables.js"></script>
	<script src="js/jquery-ui.min.js"></script>
	<script type="text/javascript">
		$(document).ready(function() {
			$('.togglemenuleft').click(function() {
				$('#menu-left').toggleClass('span1');
				$('#menu-left').toggleClass('icons-only');
				$('#menu-left').toggleClass('span3');

				$('#content').toggleClass('span9');
				$('#content').toggleClass('span11');
				$(this).find('i').toggleClass('icon-circle-arrow-right');
				$(this).find('i').toggleClass('icon-circle-arrow-left');
				$('#menu-left').find('span').toggle();
				$('#menu-left').find('.dropdown').toggle();
			});

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