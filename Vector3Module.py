from .Core.ModuleCore import ModuleCore

class Vector3Module ( ModuleCore ):
	type = "Vector3Module"
	class commands ( ModuleCore.commands ):
		updateVector = "UPDATE_VECTOR"

	_vector = [ 0, 0, 0 ]

	def __init__ ( self, UUID ):
		super( ).__init__( UUID )
		self.setOnCommand( self.commands.updateVector, lambda data: self.onUpdateVector( data ) )
		
	def onUpdateVector ( self, data ):
		vector = data[ "vector" ]
		self.updateVector( vector )

	def updateVector ( self, vector, sync=False ):
		self._vector[ :len( vector ) ] = vector[ :3 ]

		self.onChange( self.commands.updateVector, self.vector )

		if sync is True:
			self.output( self.commands.updateVector, { "vector": self.vector } )

	@property
	def vector ( self ):
		return self._vector[ : ]
	
	def getState ( self ):
		return { "vector": self.vector }
	
	def setState ( self, state ):
		self.updateVector( state[ "vector" ] )