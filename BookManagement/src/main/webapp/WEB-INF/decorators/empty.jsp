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
<link class="links-css" href="/bookmanagement/css/darkblue.css" rel="stylesheet" />
<!-- inbox page css -->
<link href="/bookmanagement/css/inbox.css" rel="stylesheet" />
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
<link href="/bookmanagement/css/bootstrap-responsive.css" rel="stylesheet" />
<!-- media query css -->
<link href="/bookmanagement/css/media-fluid.css" rel="stylesheet" />
<!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->
<!--[if lt IE 9]>
      <script src="http://html5shim.googlecode.com/svn/trunk/html5.js"></script>
      <![endif]-->
<sitemesh:write property='head' />
</head>
<body>
<sitemesh:write property='body' />

</body>
</html>