import uuid

class ModuleCore:
	_type = "ModuleCore"
	class commands:
		setState = "SET_STATE"



	def __init__( self, UUID ):
		self._UUID = UUID
		self._outputFn = None
		self._commandCallbacks = { }
		self._changeCallbacks = { }
		# self.setOnCommand( self.commands.setState, lambda state: print( "SET_STATE", self.type, state ) )
		self.setOnCommand( self.commands.setState, lambda state: self.setState( state ) )

	@property
	def UUID ( self ):
		return self._UUID
	
	@property
	def type ( self ):
		return self._type

	def setOutputFn ( self, outputFn ):
		self._outputFn = outputFn

	def input ( self, payload ):
		command = payload[ "command" ]
		data = payload[ "data" ]
		self.onCommand( command, data )

	def output ( self, command, data ):
		payload =  {
			"moduleUUID": str( self._UUID ),
			"command": command,
			"data": data
		}
		if self._outputFn is not None:
			self._outputFn( payload )

	def setOnCommand ( self, command, callback ):
		if command not in self._commandCallbacks:
			self._commandCallbacks[ command ] = [ ]
		self._commandCallbacks[ command ].append( callback )

	def onCommand ( self, command, data ):
		if command in self._commandCallbacks:
			for callback in self._commandCallbacks[ command ]:
				callback( data )

	def setOnChange ( self, change, callback ):
		if change not in self._changeCallbacks:
			self._changeCallbacks[ change ] = [ ]
		self._changeCallbacks[ change ].append( callback )

	def onChange ( self, change, data ):
		if change in self._changeCallbacks:
			for callback in self._changeCallbacks[ change ]:
				callback( data )

	def getState ( self ):
		return { }

	def setState ( self, state ):
		print( "core setstate", self.UUID)
		return
	
	def delete ( self ):
		return