package org.apache.jsp.WEB_002dINF.jsp;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class index_jsp extends org.apache.jasper.runtime.HttpJspBase
    implements org.apache.jasper.runtime.JspSourceDependent {

  private static final JspFactory _jspxFactory = JspFactory.getDefaultFactory();

  private static java.util.List _jspx_dependants;

  private javax.el.ExpressionFactory _el_expressionfactory;
  private org.apache.AnnotationProcessor _jsp_annotationprocessor;

  public Object getDependants() {
    return _jspx_dependants;
  }

  public void _jspInit() {
    _el_expressionfactory = _jspxFactory.getJspApplicationContext(getServletConfig().getServletContext()).getExpressionFactory();
    _jsp_annotationprocessor = (org.apache.AnnotationProcessor) getServletConfig().getServletContext().getAttribute(org.apache.AnnotationProcessor.class.getName());
  }

  public void _jspDestroy() {
  }

  public void _jspService(HttpServletRequest request, HttpServletResponse response)
        throws java.io.IOException, ServletException {

    PageContext pageContext = null;
    HttpSession session = null;
    ServletContext application = null;
    ServletConfig config = null;
    JspWriter out = null;
    Object page = this;
    JspWriter _jspx_out = null;
    PageContext _jspx_page_context = null;


    try {
      response.setContentType("text/html; charset=UTF-8");
      pageContext = _jspxFactory.getPageContext(this, request, response,
      			null, true, 8192, true);
      _jspx_page_context = pageContext;
      application = pageContext.getServletContext();
      config = pageContext.getServletConfig();
      session = pageContext.getSession();
      out = pageContext.getOut();
      _jspx_out = out;

      out.write("\n");
      out.write("\n");
      out.write("\n");
      out.write("<html>\n");
      out.write("<head>\n");
      out.write("<title>Intel Press Management</title>\n");
      out.write("<meta name='description' content='A simple page'>\n");
      out.write("</head>\n");
      out.write("<body>\n");
      out.write("\t<!--/span-->\n");
      out.write("\t<div id=\"content\" class=\"span9 section-body\">\n");
      out.write("\t\t<div id=\"section-body\" class=\"tabbable\">\n");
      out.write("\t\t\t<!-- Only required for left/right tabs -->\n");
      out.write("\t\t\t<ul class=\"nav nav-tabs\">\n");
      out.write("\t\t\t\t<li class=\"active\"><a href=\"#tab1\" data-toggle=\"tab\">Inbox</a></li>\n");
      out.write("\t\t\t</ul>\n");
      out.write("\t\t\t<div class=\"tab-content\">\n");
      out.write("\t\t\t\t<div class=\"tab-pane active\" id=\"tab1\">\n");
      out.write("\t\t\t\t\t<div class=\"row-fluid\">\n");
      out.write("\t\t\t\t\t\t<!--Tabs2-->\n");
      out.write("\t\t\t\t\t\t<div class=\"span12\">\n");
      out.write("\t\t\t\t\t\t\t<table class=\"table table-bordered table-striped pull-left\"\n");
      out.write("\t\t\t\t\t\t\t\tid=\"example\">\n");
      out.write("\t\t\t\t\t\t\t\t<thead>\n");
      out.write("\t\t\t\t\t\t\t\t\t<tr>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<th>From</th>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<th>Subject</th>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<th>Date</th>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<th>Actions</th>\n");
      out.write("\t\t\t\t\t\t\t\t\t</tr>\n");
      out.write("\t\t\t\t\t\t\t\t</thead>\n");
      out.write("\t\t\t\t\t\t\t\t<tbody>\n");
      out.write("\t\t\t\t\t\t\t\t\t<tr class=\"odd gradeX\">\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><img alt=\"\" src=\"img/small/thumb1.png\" />\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\tab.alhyane@gmail.com</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td>Project</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><small>12/02/2012</small></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td class=\"center\"><a href=\"#\" class=\"btn btn-danger\"\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\ttitle=\"Remove\"><i class=\"icon-remove icon-white\"></i></a> <a\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\thref=\"#\" class=\"btn btn-maniadmin-8\" title=\"Archive\"><i\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\t\tclass=\"icon-inbox\"></i></a></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t</tr>\n");
      out.write("\t\t\t\t\t\t\t\t\t<tr class=\"even gradeC\">\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><img alt=\"\" src=\"img/small/thumb2.png\" />\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\tab.alhyane@gmail.com</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td>Hotmail</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><small>12/02/2012</small></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td class=\"center\"><a href=\"#\" class=\"btn btn-danger\"\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\ttitle=\"Remove\"><i class=\"icon-remove icon-white\"></i></a> <a\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\thref=\"#\" class=\"btn btn-maniadmin-8\" title=\"Archive\"><i\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\t\tclass=\"icon-inbox\"></i></a></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t</tr>\n");
      out.write("\t\t\t\t\t\t\t\t\t<tr class=\"even gradeC\">\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><img alt=\"\" src=\"img/small/thumb2.png\" />\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\tab.alhyane@gmail.com</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td>Jquery</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><small>12/02/2012</small></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td class=\"center\"><a href=\"#\" class=\"btn btn-danger\"\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\ttitle=\"Remove\"><i class=\"icon-remove icon-white\"></i></a> <a\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\thref=\"#\" class=\"btn btn-maniadmin-8\" title=\"Archive\"><i\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\t\tclass=\"icon-inbox\"></i></a></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t</tr>\n");
      out.write("\t\t\t\t\t\t\t\t\t<tr class=\"even gradeC\">\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><img alt=\"\" src=\"img/small/thumb2.png\" />\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\tab.alhyane@gmail.com</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td>Application</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><small>12/02/2012</small></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td class=\"center\"><a href=\"#\" class=\"btn btn-danger\"\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\ttitle=\"Remove\"><i class=\"icon-remove icon-white\"></i></a> <a\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\thref=\"#\" class=\"btn btn-maniadmin-8\" title=\"Archive\"><i\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\t\tclass=\"icon-inbox\"></i></a></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t</tr>\n");
      out.write("\t\t\t\t\t\t\t\t\t<tr class=\"even gradeC\">\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><img alt=\"\" src=\"img/small/thumb2.png\" />\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\tab.alhyane@gmail.com</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td>Soft</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><small>12/02/2012</small></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td class=\"center\"><a href=\"#\" class=\"btn btn-danger\"\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\ttitle=\"Remove\"><i class=\"icon-remove icon-white\"></i></a> <a\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\thref=\"#\" class=\"btn btn-maniadmin-8\" title=\"Archive\"><i\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\t\tclass=\"icon-inbox\"></i></a></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t</tr>\n");
      out.write("\t\t\t\t\t\t\t\t\t<tr class=\"odd gradeA\">\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><img alt=\"\" src=\"img/small/thumb3.png\" />\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\tab.alhyane@gmail.com</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td>Facebook</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><small>12/02/2012</small></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td class=\"center\"><a href=\"#\" class=\"btn btn-danger\"\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\ttitle=\"Remove\"><i class=\"icon-remove icon-white\"></i></a> <a\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\thref=\"#\" class=\"btn btn-maniadmin-8\" title=\"Archive\"><i\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\t\tclass=\"icon-inbox\"></i></a></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t</tr>\n");
      out.write("\t\t\t\t\t\t\t\t\t<tr class=\"even gradeA\">\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><img alt=\"\" src=\"img/small/thumb2.png\" />\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\tab.alhyane@gmail.com</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td>Gmail</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><small>12/02/2012</small></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td class=\"center\"><a href=\"#\" class=\"btn btn-danger\"\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\ttitle=\"Remove\"><i class=\"icon-remove icon-white\"></i></a> <a\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\thref=\"#\" class=\"btn btn-maniadmin-8\" title=\"Archive\"><i\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\t\tclass=\"icon-inbox\"></i></a></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t</tr>\n");
      out.write("\t\t\t\t\t\t\t\t\t<tr class=\"odd gradeA\">\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><img alt=\"\" src=\"img/small/thumb1.png\" />\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\tab.alhyane@gmail.com</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td>Bootstrap</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><small>12/02/2012</small></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td class=\"center\"><a href=\"#\" class=\"btn btn-danger\"\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\ttitle=\"Remove\"><i class=\"icon-remove icon-white\"></i></a> <a\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\thref=\"#\" class=\"btn btn-maniadmin-8\" title=\"Archive\"><i\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\t\tclass=\"icon-inbox\"></i></a></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t</tr>\n");
      out.write("\t\t\t\t\t\t\t\t\t<tr class=\"even gradeA\">\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><img alt=\"\" src=\"img/small/thumb2.png\" />\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\tab.alhyane@gmail.com</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td>Project</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><small>12/02/2012</small></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td class=\"center\"><a href=\"#\" class=\"btn btn-danger\"\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\ttitle=\"Remove\"><i class=\"icon-remove icon-white\"></i></a> <a\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\thref=\"#\" class=\"btn btn-maniadmin-8\" title=\"Archive\"><i\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\t\tclass=\"icon-inbox\"></i></a></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t</tr>\n");
      out.write("\t\t\t\t\t\t\t\t\t<tr class=\"odd gradeA\">\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><img alt=\"\" src=\"img/small/thumb1.png\" />\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\tab.alhyane@gmail.com</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td>Travel</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><small>12/02/2012</small></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td class=\"center\"><a href=\"#\" class=\"btn btn-danger\"\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\ttitle=\"Remove\"><i class=\"icon-remove icon-white\"></i></a> <a\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\thref=\"#\" class=\"btn btn-maniadmin-8\" title=\"Archive\"><i\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\t\tclass=\"icon-inbox\"></i></a></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t</tr>\n");
      out.write("\t\t\t\t\t\t\t\t\t<tr class=\"even gradeA\">\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><img alt=\"\" src=\"img/small/thumb2.png\" />\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\tab.alhyane@gmail.com</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td>Demande</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><small>12/02/2012</small></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td class=\"center\"><a href=\"#\" class=\"btn btn-danger\"\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\ttitle=\"Remove\"><i class=\"icon-remove icon-white\"></i></a> <a\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\thref=\"#\" class=\"btn btn-maniadmin-8\" title=\"Archive\"><i\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\t\tclass=\"icon-inbox\"></i></a></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t</tr>\n");
      out.write("\t\t\t\t\t\t\t\t\t<tr class=\"odd gradeA\">\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><img alt=\"\" src=\"img/small/thumb1.png\" />\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\tab.alhyane@gmail.com</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td>Project</td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td><small>12/02/2012</small></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t\t<td class=\"center\"><a href=\"#\" class=\"btn btn-danger\"\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\ttitle=\"Remove\"><i class=\"icon-remove icon-white\"></i></a> <a\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\thref=\"#\" class=\"btn btn-maniadmin-8\" title=\"Archive\"><i\n");
      out.write("\t\t\t\t\t\t\t\t\t\t\t\tclass=\"icon-inbox\"></i></a></td>\n");
      out.write("\t\t\t\t\t\t\t\t\t</tr>\n");
      out.write("\t\t\t\t\t\t\t\t</tbody>\n");
      out.write("\t\t\t\t\t\t\t</table>\n");
      out.write("\t\t\t\t\t\t</div>\n");
      out.write("\t\t\t\t\t</div>\n");
      out.write("\t\t\t\t</div>\n");
      out.write("\t\t\t</div>\n");
      out.write("\t\t</div>\n");
      out.write("\t</div>\n");
      out.write("</body>\n");
      out.write("</html>");
    } catch (Throwable t) {
      if (!(t instanceof SkipPageException)){
        out = _jspx_out;
        if (out != null && out.getBufferSize() != 0)
          try { out.clearBuffer(); } catch (java.io.IOException e) {}
        if (_jspx_page_context != null) _jspx_page_context.handlePageException(t);
      }
    } finally {
      _jspxFactory.releasePageContext(_jspx_page_context);
    }
  }
}
