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
				<li class="active"><a href="#" data-toggle="tab">Dashboard</a></li>
			</ul>
			<div class="tab-content">
				<div class="tab-pane active" id="tab1">
					<div class="row-fluid">
						<!--Tabs2-->
						<div class="span12">
							<p><b>Total Books:</b> <span style="font-size:200%" >${bookCount}</span></p>
							<p><b>Total Chapters:</b> <span style="font-size:200%" >${chapterCount}</span></p>
							<p><b>Technical Articles Progress:</b> <span style="font-size:200%" ><i>${totalArticles}</i><b>/${totalArticles+uncompletedArticles}</b></span></p>
							<div class="progress progress-success active" >
								<div style="width:${progress}%" class="bar" ></div>
							</div>
						</div>
					</div>
				</div>
			</div>
		</div>
	</div>
</body>
</html>
