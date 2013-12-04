'''
Module for khan academy exercises in coursebuilder.
'''

def register_module():
	"""Registers this module in the directory."""

	# Register custom tag
	tags.registry.add_tag_binding('khanex', KhanExerciseTag)

	# register handlers
	zip_handler = (
	    '/khan-exercises', sites.make_zip_handler(ZIP_FILE))
	render_handler = (
		'khan-exercises/khan-exercises/indirect/', KhanExerciseRenderer)

	#register module
	global custom_module
	custom_module = custom_module.Module(
		'Khan Academy Exercise',
		'A set of pages for delivering Khan Academy Exercises via ',
		'Course Builder.',
		[], [render_handler, zip_handler],)
	return custom_module

def get_schema(self, unused_handler):
	"""Make schema with a list of all exercises by inspecting a zip file."""

	reg = schema_fields.FieldRegistry('Khan Exercises')
	reg.add_property(
		schema_fields.SchemaField(
			'name', 'Exercises', 'select', optional=True,
			select_data=items,
			description=("The relative URL name of the exercise.")))
	return reg

def render(self, node):
	"""Embed just a <script> tag that will in turn create and <iframe>."""
	name = node.attrib.get('name')
	caption = name.replace('-', ' ')
	return cElementTree.XML(
        """
<div style='width:450px;'>
Khan Academy Exercise: %s
<br/>
<script>
// customize the style of the exercise iframe
var ity_ef_style = "width: 750px;";
</script>
<script src="%s" type="text/javascript"></script>
</div>""" % (
	cgi.escape(caption), 'khan-exercises/embed.js?static:%s' % name ))