import uuid
from .ModuleCore import ModuleCore
from .ModuleTypes import ModuleTypes

class ModulesRegistry ( ModuleCore ):
	_type = "ModulesRegistry"
	class commands ( ModuleCore.commands ):
		addModule = "ADD_MODULE"
		removeModule = "REMOVE_MODULE"

	def __init__ ( self, outputFn ):
		UUID = uuid.UUID(int=0)
		ModuleCore.__init__( self, UUID )
		self._modules = { }
		self._outputFn = None
		self._modules[ UUID ] = self
		self.setOutputFn( outputFn )
		self._outputFn = outputFn
		self.setOnCommand( self.commands.addModule, lambda data: self.onAddModule( data ) )

	def onAddModule ( self, data ):
		type = data[ "type" ]
		UUID = uuid.UUID( data[ "UUID" ] )
		self.addModule( type, UUID )

	def onRemoveModule ( self, data ):
		UUID = uuid.UUID( data[ "UUID" ] )
		self.removeModule( UUID )

	def addModule ( self, type, UUID, sync=False ):
		print( "addModule", type)

		if UUID in self._modules:
			return

		module = None
		if type in ModuleTypes:
			module = ModuleTypes[ type ]( UUID )
		else:
			module = ModuleCore( UUID )
		
		self._modules[ UUID ] = module
		module.setOutputFn( self._outputFn )

		self.onChange( self.commands.addModule, module )
		
		if sync is True:
			self.output( self.commands.addModule, { "type": module.type, "UUID": str( UUID ) } )
		
		return module

	def removeModule ( self, UUID, sync=False ):
		if UUID not in self._modules:
			return
		
		module = self._modules[ UUID ]
		self.onChange( self.commands.removeModule, module )
		module.delete( )
		del( self._modules[ UUID ] )

		if sync is True:
			self.output( self.commands.removeModule, { "UUID": str( UUID ) } )


	def modulesList ( self ):
		return list( self._modules )

	def getModule ( self, moduleUUID ):
		return self._modules.get( moduleUUID )

	def getState ( self ):
		return { }

	def setState ( self, state ):
		modulesData = state[ "modulesData" ]
		for moduleData in modulesData:
			UUID = uuid.UUID( moduleData[ "UUID" ] )
			type = moduleData[ "type" ]
			self.addModule( type, UUID )
		return