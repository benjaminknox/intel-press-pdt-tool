from django import template

class search_fragment(template.Node):

	def __int__(self, string):
		self.template = 'Template'

	def is_usable():
		return True

	def render(self,context):
		html = '<div id="search-form">'
		html+= '<div class="pull-right">'
		html+= '<form action="{{ request.get_full_path }}" class="form-inline" method="post">'
		html+= '<input type="text" class="datepicker" name="date" style="width: 100px" placeholder="date" />'
		html+= '<input type="text" name="search" class="input-medium search-query" />'
		html+= '<button type="submit" class="btn">Go</button>'
		html+= '</form><!-- (bootstrap) .form-inline -->'
		html+= '</div><!-- (bootstrap) .pull-right -->'
		html+= '<div class="clearfix"></div>'
		html+= '</div><!-- #search-form -->'

		return html