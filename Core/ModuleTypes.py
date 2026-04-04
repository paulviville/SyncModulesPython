from .ModuleCore import ModuleCore
from ..ScalarModule import ScalarModule
from ..Vector3Module import Vector3Module
from ..TransformModule import TransformModule
from ..PrimitiveModule import PrimitiveModule
from ..CameraModule import CameraModule
from ..LineModule import LineModule

ModuleTypes = {
	"ModuleCore": ModuleCore,
	"ScalarModule": ScalarModule,
	"Vector3Module": Vector3Module,
	"TransformModule": TransformModule,
	"PrimitiveModule": PrimitiveModule,
	"CameraModule": CameraModule,
	"LineModule": LineModule
}