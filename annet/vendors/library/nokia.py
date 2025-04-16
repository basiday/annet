from annet.annlib.netdev.views.hardware import HardwareView
from annet.vendors.base import AbstractVendor
from annet.vendors.registry import registry


@registry.register
class NokiaVendor(AbstractVendor):
    NAME = "nokia"

    def match(self) -> list[str]:
        return ["Nokia"]

    @property
    def reverse(self) -> str:
        return "delete"

    @property
    def hardware(self) -> HardwareView:
        return HardwareView("Nokia")
