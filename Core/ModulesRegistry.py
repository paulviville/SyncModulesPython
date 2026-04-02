from .ModuleCore import ModuleCore

class ModulesRegistry ( ModuleCore ):
	def __init__ ( self, UUID ):
		ModuleCore.__init__( self, UUID )
		print( "ModulesRegistry" )