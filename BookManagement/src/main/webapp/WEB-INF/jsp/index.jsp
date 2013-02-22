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
							<!-- <div id="container" style="min-width: 400px; height: 400px; margin: 0 auto"></div> -->
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
	
		<script>
	    var chart;
	    $(document).ready(function() {
	        chart = new Highcharts.Chart({
	            chart: {
	                renderTo: 'container',
	                plotBackgroundColor: null,
	                plotBorderWidth: null,
	                plotShadow: false
	            },
	            title: {
	                text: 'Browser market shares at a specific website, 2010'
	            },
	            tooltip: {
	                pointFormat: '{series.name}: <b>{point.percentage}%</b>',
	                percentageDecimals: 1
	            },
	            plotOptions: {
	                pie: {
	                    allowPointSelect: true,
	                    cursor: 'pointer',
	                    dataLabels: {
	                        enabled: true,
	                        color: '#000000',
	                        connectorColor: '#000000',
	                        formatter: function() {
	                            return '<b>'+ this.point.name +'</b>: '+ this.percentage +' %';
	                        }
	                    }
	                }
	            },
	            series: [{
	                type: 'pie',
	                name: 'Browser share',
	                data: [
	                    ['Firefox',   45.0],
	                    ['IE',       26.8],
	                    {
	                        name: 'Chrome',
	                        y: 12.8,
	                        sliced: true,
	                        selected: true
	                    },
	                    ['Safari',    8.5],
	                    ['Opera',     6.2],
	                    ['Others',   0.7]
	                ]
	            }]
	        });
	    });
	    </script>
</body>
</html>
