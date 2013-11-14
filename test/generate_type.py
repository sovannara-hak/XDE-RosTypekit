Types = DefaultDict()

def _generate_types(rtt_interface_module):
	global Types
 	for i in dir(rtt_interface_module.Types):
		try:
			a, b = i.split('_',1)
		except ValueError:
			a = None
		if a == "data": # Just to be sure
			# Create a class instead of a dict (maybe more efficient)
			try:
				Types[b] = type("type_" + b, (object,), {
					'data':  getattr(rtt_interface_module.Types, "data_" + b), 
					'value': getattr(rtt_interface_module.Types, "value_" + b),
					'set': getattr(rtt_interface_module.Types, "set_" + b),
					'iport': getattr(rtt_interface_module.Types, "iport_" + b),
					'oport': getattr(rtt_interface_module.Types, "oport_" + b)
					})
			except AttributeError: # iport and oport are not all necessarilly present
				Types[b] = type("type_" + b, (object,), {
					'data':  getattr(rtt_interface_module.Types, "data_" + b), 
					'value': getattr(rtt_interface_module.Types, "value_" + b),
					'set': getattr(rtt_interface_module.Types, "set_" + b)
					})

# XXX automatic registering when importing rtt_interface_* into a variable in rtt_interface which ought to have the _generate_types
_generate_types(rtt_interface)
_generate_types(rtt_interface_base_type)
_generate_types(rtt_interface_xde_type)
_generate_types(rtt_interface_xde_container_type)

