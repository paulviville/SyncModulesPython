from .TransformModule import TransformModule

class PrimitiveModule ( TransformModule ):
	_type = "PrimitiveModule"
	class commands ( TransformModule.commands ):
		updatePrimitive = "UPDATE_PRIMITIVE"

	class primitiveTypes:
		Sphere = "Sphere"
		Box = "Box"

	def __init__ ( self, UUID ):
		super( ).__init__( UUID )
		
		self._primitive = self.primitiveTypes.Sphere
		self.setOnCommand( self.commands.updatePrimitive, self.onUpdatePrimitive )

	def onUpdatePrimitive ( self, data ):
		primitive = data[ "primitive" ]
		self.updatePrimitive( primitive )

	def updatePrimitive ( self, primitive, sync=False ):
		self._primitive = primitive

		self.onChange( self.commands.updatePrimitive, self.transform )
		if sync is True:
			self.output( self.commands.updatePrimitive, { "primitive": self.primitive } )

	@property
	def primitive ( self ):
		return self._primitive
	
	def getState ( self ):
		return {
			**super( ).getState( ),
			"primitive": self.primitive
		}
	
	def setState ( self, state ):
		super( ).setState( state )
		self.updatePrimitive( state[ "primitive" ] )
		