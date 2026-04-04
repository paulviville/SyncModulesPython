from .TransformModule import TransformModule

class CameraModule ( TransformModule ):
	_type = "CameraModule"
	class commands ( TransformModule.commands ):
		updateCamera = "UPDATE_CAMERA"

	def __init__ ( self, UUID ):
		super( ).__init__( UUID )

		self._fov = 50
		self._aspect = 4/3
		self._near = 0.1
		self._far = 1

		self.setOnCommand( self.commands.updateCamera, self.onUpdateCamera )

	@property
	def camera ( self ):
		return {
			"fov": self._fov,
			"aspect": self._aspect,
			"near": self._near,
			"far": self._far
		}
	
	def onUpdateCamera ( self, data ):
		camera = data[ "camera" ]
		self.updateCamera( camera )

	def updateCamera ( self, camera, sync=False ):
		if camera.get( "fov ") is not None:
			self._fov = camera[ "fov" ]
		if camera.get( "aspect ") is not None:
			self._aspect = camera[ "aspect" ]
		if camera.get( "near ") is not None:
			self._near = camera[ "near" ]
		if camera.get( "far ") is not None:
			self._far = camera[ "far" ]

		self.onChange( self.commands.updateCamera, self.camera )

		if sync is True:
			self.output( self.commands.updateCamera, { "camera": self.camera } )

	def getState ( self ):
		return {
			**super( ).getState( ),
			"camera": self.camera
		}
	
	def setState ( self, state ):
		super( ).setState( state )
		self.updateCamera( state[ "camera" ] )