#!/usr/bin/env python3

class Device:
    def __init__(self, model) -> None:
        self.model = model

    def scan_for_vulnerabilities(self):
        raise NotImplementedError('This method must be defined for the rest of the existing subclasses')


class Computer(Device):
    def scan_for_vulnerabilities(self):
        return f'[+] Computer -> Security analysis completed: Software update required, multiple software out-of-date detected'


class Router(Device):
    def scan_for_vulnerabilities(self):
        return f'[+] Router -> Security analysis completed: Multiple critical ports detected as open, it is recommended to close these ports'


class MobilePhone(Device):
    def scan_for_vulnerabilities(self):
        return f'[+] Mobile phone -> Security analysis completed: Multiple applications detected with excessive permissions'


# Polymorphism
def scan_device(device):
    print(f'{device.scan_for_vulnerabilities()}')


pc = Computer("Dell XPS")
router = Router("Tp-Link Archer C50")
mobile = MobilePhone("Samsung Galaxy S21")

scan_device(pc)
scan_device(router)
scan_device(mobile)
