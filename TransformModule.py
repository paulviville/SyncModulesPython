from .Core.ModuleCore import ModuleCore

class TransformModule ( ModuleCore ):
	_type = "TransformModule"
	class commands ( ModuleCore.commands ):
		updateTransform = "UPDATE_TRANSFORM"

	def __init__( self, UUID ):
		super( ).__init__( UUID )

		self._translation = [ 0, 0, 0 ]
		self._rotation = [ 0, 0, 0, 1 ]
		self._scale = [ 1, 1, 1 ]

		self.setOnCommand( self.commands.updateTransform, self.updateTransform )

	def onUpdateTransform ( self, data ):
		transform = data[ "transform" ]
		self.updateTransform( transform )

	def updateTransform ( self, transform, sync=False ):
		translation = transform.get( "translation" )
		rotation = transform.get( "rotation" )
		scale = transform.get( "scale" )

		if translation is not None:
			self._translation[ :len( translation ) ] = translation[ :3 ]
		if rotation is not None:
			self._rotation[ :len( rotation ) ] = rotation[ :4 ]
		if scale is not None:
			self._scale[ :len( scale ) ] = scale[ :3 ]

		self.onChange( self.commands.updateTransform, self.transform )

		if sync is True:
			self.output( self.commands.updateTransform, { "transform": self.transform } )

	@property
	def transform ( self ):
		return {
			"translation": self._translation[ : ],
			"rotation": self._rotation[ : ],
			"scale": self._scale[ : ]
		}
	
	def getState ( self ):
		return { "transform": self.transform }
	
	def setState ( self, state ):
		self.updateTransform( state[ "transform" ] )