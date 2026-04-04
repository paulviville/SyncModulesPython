from .Core.ModuleCore import ModuleCore

class LineModule ( ModuleCore ):
	_type = "LineModule"
	class commands ( ModuleCore.commands ):
		updateLine = "UPDATE_LINE"

	def __init__( self, UUID ):
		super( ).__init__( UUID )

		self._origin = [ 0, 0, 0 ]
		self._end = [ 0, 0, 0 ]

		self.setOnCommand( self.commands.updateLine, self.onUpdateLine )

	@property
	def line ( self ):
		return {
			"origin": self._origin[ : ],
			"end": self._end[ : ]
		}

	def onUpdateLine ( self, data ):
		line = data[ "line" ]
		self.updateLine( line )

	def updateLine ( self, line, sync=False ):
		origin = line.get( "origin" )
		end = line.get( "end" )

		if origin is not None:
			self._origin[ :len( origin ) ] = origin[ :3 ]
		if end is not None:
			self._end[ :len( end ) ] = end[ :3 ]

		self.onChange( self.commands.updateLine, self.line )

		if sync is True:
			self.output( self.commands.updateLine, { "line": self.line } )

	def getState ( self ):
		return { "line": self.line }
	
	def setState ( self, state ):
		self.updateLine( state[ "line" ] )
