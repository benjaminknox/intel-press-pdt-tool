<%@ taglib uri="http://java.sun.com/jsp/jstl/core" prefix="c"%><%@ taglib
	uri="http://www.springframework.org/tags/form" prefix="form"%><%@ page
	language="java" contentType="text/html; charset=UTF-8"
	pageEncoding="UTF-8"%>
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
<link class="links-css" href="css/base.css" rel="stylesheet" />
<!-- inbox page css -->
<link href="css/inbox.css" rel="stylesheet" />
<!-- custom css  -->
<link class="links-css" href="css/jquery-ui-bootstrap-1.8.16.custom.css"
	rel="stylesheet">
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
			</div>
		</div>
	</div>
	<sitemesh:write property='body' />
	<!-- Le javascript
         ================================================== -->
	<!-- Placed at the end of the document so the pages load faster -->
	<script src="js/jquery.min.js"></script>
	<script src="js/bootstrap.min.js"></script>
	<script src="js/jquery.dataTables.js"></script>
	<script src="js/jquery-ui.min.js"></script>
</body>
</html>