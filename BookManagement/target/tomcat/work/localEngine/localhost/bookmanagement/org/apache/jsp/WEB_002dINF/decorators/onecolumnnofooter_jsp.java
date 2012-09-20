package org.apache.jsp.WEB_002dINF.decorators;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class onecolumnnofooter_jsp extends org.apache.jasper.runtime.HttpJspBase
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
      out.write("<!DOCTYPE html>\n");
      out.write("<html lang=\"en\">\n");
      out.write("<head>\n");
      out.write("<meta charset=\"utf-8\" />\n");
      out.write("<title><sitemesh:write property='title' /></title>\n");
      out.write("<meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n");
      out.write("<meta name=\"description\" content=\"\" />\n");
      out.write("<meta name=\"author\" content=\"\" />\n");
      out.write("<!-- Le styles -->\n");
      out.write("<!-- bootstrap css -->\n");
      out.write("<link href=\"css/bootstrap.min.css\" rel=\"stylesheet\" />\n");
      out.write("<!-- base css -->\n");
      out.write("<link class=\"links-css\" href=\"css/darkblue.css\" rel=\"stylesheet\" />\n");
      out.write("<!-- inbox page css -->\n");
      out.write("<link href=\"css/inbox.css\" rel=\"stylesheet\" />\n");
      out.write("<!-- custom css  -->\n");
      out.write("<link class=\"links-css\" href=\"css/jquery-ui-bootstrap-1.8.16.custom.css\"\n");
      out.write("\trel=\"stylesheet\">\n");
      out.write("<style type=\"text/css\">\n");
      out.write("body {\n");
      out.write("\tpadding-top: 60px;\n");
      out.write("\tpadding-bottom: 40px;\n");
      out.write("}\n");
      out.write("\n");
      out.write(".sidebar-nav {\n");
      out.write("\tpadding: 9px 0;\n");
      out.write("}\n");
      out.write("</style>\n");
      out.write("<!-- responsive css -->\n");
      out.write("<link href=\"css/bootstrap-responsive.css\" rel=\"stylesheet\" />\n");
      out.write("<!-- media query css -->\n");
      out.write("<link href=\"css/media-fluid.css\" rel=\"stylesheet\" />\n");
      out.write("<!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->\n");
      out.write("<!--[if lt IE 9]>\n");
      out.write("      <script src=\"http://html5shim.googlecode.com/svn/trunk/html5.js\"></script>\n");
      out.write("      <![endif]-->\n");
      out.write("<sitemesh:write property='head' />\n");
      out.write("</head>\n");
      out.write("<body>\n");
      out.write("\t<div class=\"navbar navbar-fixed-top\">\n");
      out.write("\t\t<div class=\"navbar-inner\">\n");
      out.write("\t\t\t<div class=\"container-fluid\">\n");
      out.write("\t\t\t\t<a class=\"btn btn-navbar\" data-toggle=\"collapse\"\n");
      out.write("\t\t\t\t\tdata-target=\".nav-collapse\"> <span class=\"icon-bar\"></span> <span\n");
      out.write("\t\t\t\t\tclass=\"icon-bar\"></span> <span class=\"icon-bar\"></span>\n");
      out.write("\t\t\t\t</a> <a class=\"brand\" href=\"index.html\"><img\n");
      out.write("\t\t\t\t\tsrc=\"img/logo-small.png\" alt=\"logo\" /></a>\n");
      out.write("\t\t\t</div>\n");
      out.write("\t\t</div>\n");
      out.write("\t</div>\n");
      out.write("\t<sitemesh:write property='body' />\n");
      out.write("\t<!-- Le javascript\n");
      out.write("         ================================================== -->\n");
      out.write("\t<!-- Placed at the end of the document so the pages load faster -->\n");
      out.write("\t<script src=\"js/jquery.min.js\"></script>\n");
      out.write("\t<script src=\"js/bootstrap.min.js\"></script>\n");
      out.write("\t<script src=\"js/jquery.dataTables.js\"></script>\n");
      out.write("\t<script src=\"js/jquery-ui.min.js\"></script>\n");
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
