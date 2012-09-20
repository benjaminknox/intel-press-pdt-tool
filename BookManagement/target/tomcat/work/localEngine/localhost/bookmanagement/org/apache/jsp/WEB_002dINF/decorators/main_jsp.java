package org.apache.jsp.WEB_002dINF.decorators;

import javax.servlet.*;
import javax.servlet.http.*;
import javax.servlet.jsp.*;

public final class main_jsp extends org.apache.jasper.runtime.HttpJspBase
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
      out.write("   <head>\n");
      out.write("      <meta charset=\"utf-8\" />\n");
      out.write("      <title><sitemesh:write property='title'/></title>\n");
      out.write("      <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />\n");
      out.write("      <meta name=\"description\" content=\"\" />\n");
      out.write("      <meta name=\"author\" content=\"\" />\n");
      out.write("      <!-- Le styles -->\n");
      out.write("      <!-- bootstrap css -->\n");
      out.write("      <link href=\"css/bootstrap.min.css\" rel=\"stylesheet\" />\n");
      out.write("      <!-- base css -->\n");
      out.write("      <link class=\"links-css\" href=\"css/darkblue.css\" rel=\"stylesheet\" />\n");
      out.write("      <!-- inbox page css -->\n");
      out.write("      <link href=\"css/inbox.css\" rel=\"stylesheet\" />\n");
      out.write("      <style type=\"text/css\">\n");
      out.write("         body {\n");
      out.write("         padding-top: 60px;\n");
      out.write("         padding-bottom: 40px;\n");
      out.write("         }\n");
      out.write("         .sidebar-nav {\n");
      out.write("         padding: 9px 0;\n");
      out.write("         }\n");
      out.write("      </style>\n");
      out.write("      <!-- responsive css -->\n");
      out.write("      <link href=\"css/bootstrap-responsive.css\" rel=\"stylesheet\" />\n");
      out.write("      <!-- media query css -->\n");
      out.write("      <link href=\"css/media-fluid.css\" rel=\"stylesheet\" />\n");
      out.write("      <!-- Le HTML5 shim, for IE6-8 support of HTML5 elements -->\n");
      out.write("      <!--[if lt IE 9]>\n");
      out.write("      <script src=\"http://html5shim.googlecode.com/svn/trunk/html5.js\"></script>\n");
      out.write("      <![endif]-->\n");
      out.write("      <sitemesh:write property='head'/>\n");
      out.write("   </head>\n");
      out.write("   <body>\n");
      out.write("      <div class=\"navbar navbar-fixed-top\">\n");
      out.write("         <div class=\"navbar-inner\">\n");
      out.write("            <div class=\"container-fluid\">\n");
      out.write("               <a class=\"btn btn-navbar\" data-toggle=\"collapse\" data-target=\".nav-collapse\">\n");
      out.write("               <span class=\"icon-bar\"></span>\n");
      out.write("               <span class=\"icon-bar\"></span>\n");
      out.write("               <span class=\"icon-bar\"></span>\n");
      out.write("               </a>\n");
      out.write("               <a class=\"brand\" href=\"index.html\"><img src=\"img/logo-small.png\" alt=\"logo\" /></a>\n");
      out.write("               <ul class=\"nav pull-left bar-root\">\n");
      out.write("                  <li class=\"divider-vertical\"></li>\n");
      out.write("                  <li><a href=\"chat.html\"><i class=\"icon-comment icon-white\"></i><span class=\"label label-important\">6</span></a> </li>\n");
      out.write("                  <li class=\"dropdown\">\n");
      out.write("                     <a href=\"#\" data-toggle=\"dropdown\"> <i class=\"icon-envelope icon-white\"></i><span class=\"label label-important\">5 new</span></a> \n");
      out.write("                     <ul class=\"dropdown-menu\">\n");
      out.write("                        <li>\n");
      out.write("                           <a href=\"inbox.html\">\n");
      out.write("                              <img src=\"img/small/thumb1.png\" alt=\"\" /> Subject : Project \n");
      out.write("                              <p class=\"help-block\"><small>From: ab.alhyane@gmail.com</small></p>\n");
      out.write("                              <span class=\"label\">23/09/2012</span>\n");
      out.write("                           </a>\n");
      out.write("                        </li>\n");
      out.write("                        <li class=\"divider\"></li>\n");
      out.write("                        <li>\n");
      out.write("                           <a href=\"inbox.html\">\n");
      out.write("                              <img src=\"img/small/thumb2.png\" alt=\"\" /> Subject : Film \n");
      out.write("                              <p class=\"help-block\"><small>From: ab.alhyane@gmail.com</small></p>\n");
      out.write("                              <span class=\"label\">21/04/2012</span> \n");
      out.write("                           </a>\n");
      out.write("                        </li>\n");
      out.write("                        <li class=\"divider\"></li>\n");
      out.write("                        <li>\n");
      out.write("                           <a href=\"inbox.html\">\n");
      out.write("                              <img src=\"img/small/thumb3.png\" alt=\"\" /> Subject : Meeting \n");
      out.write("                              <p class=\"help-block\"><small>From: ab.alhyane@gmail.com</small></p>\n");
      out.write("                              <span class=\"label\">20/02/2012</span>\n");
      out.write("                           </a>\n");
      out.write("                        </li>\n");
      out.write("                        <li class=\"divider\"></li>\n");
      out.write("                        <li>\n");
      out.write("                           <a href=\"inbox.html\">\n");
      out.write("                              <img src=\"img/small/thumb4.png\" alt=\"\" /> Subject : Tasks \n");
      out.write("                              <p class=\"help-block\"><small>From: y.kostali@gmail.com</small></p>\n");
      out.write("                              <span class=\"label\">19/01/2012</span>\n");
      out.write("                           </a>\n");
      out.write("                        </li>\n");
      out.write("                        <li class=\"divider\"></li>\n");
      out.write("                        <li class=\"active\"><a href=\"inbox.html\"> Show All </a></li>\n");
      out.write("                     </ul>\n");
      out.write("                  </li>\n");
      out.write("                  <li class=\"dropdown\">\n");
      out.write("                     <a href=\"#\" data-toggle=\"dropdown\"> <i class=\"icon-refresh icon-white\"></i><span class=\"label label-info\">3 Updates</span></a> \n");
      out.write("                     <ul class=\"dropdown-menu\">\n");
      out.write("                        <li><a href=\"#\"> Theme </a></li>\n");
      out.write("                        <li><a href=\"#\"> Components</a></li>\n");
      out.write("                        <li><a href=\"#\"> Plugins</a></li>\n");
      out.write("                        <li class=\"divider\"></li>\n");
      out.write("                        <li class=\"active\"><a href=\"#\"> Show All </a></li>\n");
      out.write("                     </ul>\n");
      out.write("                  </li>\n");
      out.write("               </ul>\n");
      out.write("               <div class=\"group-menu nav-collapse\">\n");
      out.write("                  <ul class=\"nav pull-right\">\n");
      out.write("                     <li class=\"divider-vertical\"></li>\n");
      out.write("                     <li class=\"dropdown\">\n");
      out.write("                        <a data-toggle=\"dropdown\" href=\"#\">Salutations, Ab Alhyane <b class=\"caret\"></b></a>\n");
      out.write("                        <ul class=\"dropdown-menu\">\n");
      out.write("                           <li>\n");
      out.write("                              <div class=\"modal-header\">\n");
      out.write("                                 <h3>Kostali Youssef - Admin</h3>\n");
      out.write("                              </div>\n");
      out.write("                              <div class=\"modal-body\">\n");
      out.write("                                 <div class=\"row\">\n");
      out.write("                                    <div class=\"span1\"><img src=\"img/avatar/photo.png\" alt=\"avatar\" /></div>\n");
      out.write("                                    <div class=\"span3 pull-right\">\n");
      out.write("                                       <h5>mail@gmail.com</h5>\n");
      out.write("                                       <a href=\"#\" class=\"link-modal\">Account</a>  <a href=\"#\" class=\"link-modal\">Settings-Privacy</a>\n");
      out.write("                                    </div>\n");
      out.write("                                 </div>\n");
      out.write("                              </div>\n");
      out.write("                              <div class=\"modal-footer\">\n");
      out.write("                                 <a href=\"#\" class=\"btn btn-info pull-left\">Show my profile</a>\n");
      out.write("                                 <a class=\"btn btn-info\" href=\"login.html\">Deconnexion</a>\n");
      out.write("                              </div>\n");
      out.write("                           </li>\n");
      out.write("                        </ul>\n");
      out.write("                     </li>\n");
      out.write("                  </ul>\n");
      out.write("                  <form action=\"#\" class=\"navbar-search pull-right\">\n");
      out.write("                     <input type=\"text\" placeholder=\"Search\" class=\"search-query span2\" />\n");
      out.write("                  </form>\n");
      out.write("               </div>\n");
      out.write("            </div>\n");
      out.write("         </div>\n");
      out.write("      </div>\n");
      out.write("      <div class=\"container-fluid\">\n");
      out.write("         <div class=\"row-fluid\">\n");
      out.write("            <div id=\"menu-left\" class=\"span3\">\n");
      out.write("               <div class=\"sidebar-nav\">\n");
      out.write("                  <ul class=\"nav nav-list\">\n");
      out.write("                     <li><a href=\"index.html\"><i class=\"icon-th-large\"></i><span> Dashboard</span></a></li>\n");
      out.write("                     <li><a href=\"widget.html\"><i class=\"icon-th\"></i><span> Widgets</span></a></li>\n");
      out.write("                     <li><a href=\"tables.html\"><i class=\"icon-list-alt\"></i><span> Tables</span></a></li>\n");
      out.write("                     <li><a href=\"elements.html\"><i class=\"icon-tasks\"></i><span> Elements</span></a></li>\n");
      out.write("                     <li><a href=\"media.html\"><i class=\"icon-picture\"></i><span> Media</span></a></li>\n");
      out.write("                     <li><a href=\"forms.html\"><i class=\"icon-align-center\"></i><span> Forms</span></a></li>\n");
      out.write("                     <li><a href=\"grid.html\"><i class=\"icon-indent-left\"></i><span> Grid</span></a></li>\n");
      out.write("                     <li><a href=\"buttons.html\"><i class=\"icon-gift\"></i><span> Buttons & Icons</span></a></li>\n");
      out.write("                     <li><a href=\"noty.html\"><i class=\"icon-comment\"></i><span> Notification</span></a></li>\n");
      out.write("                     <li><a href=\"callendar.html\"><i class=\"icon-calendar\"></i><span> Callendar </span></a></li>\n");
      out.write("                     <li><a href=\"bootstrap-ui.html\"><i class=\"icon-ok\"></i><span> Bootstrap ui </span></a></li>\n");
      out.write("                     <li><a href=\"chat.html\"><i class=\"icon-bullhorn\"></i><span> Chat </span></a></li>\n");
      out.write("                     <li><a href=\"inbox.html\" class=\"current\"><i class=\"icon-envelope icon-white\"></i><span> Inbox </span></a></li>\n");
      out.write("                     <li><a href=\"charts.html\" class=\"last\"><i class=\"icon-warning-sign\"></i><span>  Graphs & Charts</span></a></li>\n");
      out.write("                     <li class=\"accordion-menu\">\n");
      out.write("                        <a href=\"#collapseOne\" data-toggle=\"collapse\" class=\"accordion-toggle\"><i class=\"icon-warning-sign\"></i><span> Error Pages  <i class=\"icon-chevron-down pull-right\"></i></span></a>\n");
      out.write("                        <div class=\"accordion-body collapse dropdown\" id=\"collapseOne\">\n");
      out.write("                           <div class=\"accordion-inner\">\n");
      out.write("                              <ul class=\"nav nav-list\">\n");
      out.write("                                 <li><a href=\"404.html\">404</a></li>\n");
      out.write("                                 <li><a href=\"403.html\">403</a></li>\n");
      out.write("                                 <li><a href=\"500.html\">500</a></li>\n");
      out.write("                              </ul>\n");
      out.write("                           </div>\n");
      out.write("                        </div>\n");
      out.write("                     </li>\n");
      out.write("                  </ul>\n");
      out.write("                  <div class=\"togglemenuleft\"><a class=\"toggle-menu\"><i class=\"icon-circle-arrow-left icon-white\"></i></a></div>\n");
      out.write("               </div>\n");
      out.write("               <!--/.well -->\n");
      out.write("            </div>\n");
      out.write("            <sitemesh:write property='body'/>\n");
      out.write("         </div>\n");
      out.write("         <footer>\n");
      out.write("            <p><strong>&copy; Maniadmin 2012</strong></p>\n");
      out.write("         </footer>\n");
      out.write("\n");
      out.write("      </div>\n");
      out.write("      <!-- Le javascript\n");
      out.write("         ================================================== -->\n");
      out.write("      <!-- Placed at the end of the document so the pages load faster -->\n");
      out.write("      <script src=\"js/jquery.min.js\"></script>\n");
      out.write("      <script src=\"js/bootstrap.min.js\"></script>\n");
      out.write("      <script src=\"js/jquery.dataTables.js\"></script>\n");
      out.write("      <script src=\"js/jquery-ui.min.js\"></script>\n");
      out.write("      <script type=\"text/javascript\">\n");
      out.write("         $(document).ready(function(){\n");
      out.write("             $('.togglemenuleft').click(function(){\n");
      out.write("                 $('#menu-left').toggleClass('span1');\n");
      out.write("                 $('#menu-left').toggleClass('icons-only');\n");
      out.write("                 $('#menu-left').toggleClass('span3');\n");
      out.write("         \n");
      out.write("                 $('#content').toggleClass('span9');\n");
      out.write("                 $('#content').toggleClass('span11');\n");
      out.write("                 $(this).find('i').toggleClass('icon-circle-arrow-right');\n");
      out.write("                 $(this).find('i').toggleClass('icon-circle-arrow-left');\n");
      out.write("                 $('#menu-left').find('span').toggle();\n");
      out.write("                 $('#menu-left').find('.dropdown').toggle();\n");
      out.write("             });\n");
      out.write("         \n");
      out.write("             $('#menu-left a').click(function(){\n");
      out.write("                 $('#menu-left').find('a').removeClass('active');\n");
      out.write("                 $(this).addClass('active');\n");
      out.write("             });\n");
      out.write("              $('a').tooltip('hide');\n");
      out.write("             // sort table \n");
      out.write("             $('#example').dataTable();\n");
      out.write("             $('a.style').click(function(){\n");
      out.write("                 var style = $(this).attr('href');\n");
      out.write("                 $('.links-css').attr('href','css/' + style);\n");
      out.write("                 return false;\n");
      out.write("             });\n");
      out.write("         \n");
      out.write("             // switch style \n");
      out.write("         \n");
      out.write("             $(\".switcher\").click(function(){\n");
      out.write("                 if($(this).find('i').hasClass('icon-circle-arrow-right'))\n");
      out.write("                 $('.theme').animate({left:'0px'},500);\n");
      out.write("                 else\n");
      out.write("                 $('.theme').animate({left:'-89'},500);\n");
      out.write("         \n");
      out.write("                 $(this).find('i').toggleClass('icon-circle-arrow-right');\n");
      out.write("                 $(this).find('i').toggleClass('icon-circle-arrow-left');\n");
      out.write("             });\n");
      out.write("         });\n");
      out.write("      </script>\n");
      out.write("   </body>\n");
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
