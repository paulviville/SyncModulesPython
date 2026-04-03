from .Core.ModuleCore import ModuleCore

class ScalarModule ( ModuleCore ):
	_type = "ScalarModule"
	class commands ( ModuleCore.commands ):
		updateValue = "UPDATE_VALUE"

	_value = 0

	def __init__( self, UUID ):
		super( ).__init__( UUID )

		self.setOnCommand( self.commands.updateValue, lambda data: self.onUpdateValue( data ) )

	def onUpdateValue ( self, data ):
		value = data[ "value" ]
		self.updateValue( value )

	def updateValue ( self, value, sync=False ):
		self._value = value
		
		self.onChange( self.commands.updateValue, value )

		if sync is True:
			self.output( self.commands.updateValue, { "value": value } )

	def getState ( self ):
		return { "value": self._value }
	
	def setState( self, state ):
		self.updateValue( state[ "value" ] )
		