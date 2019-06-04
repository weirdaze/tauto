class Chips:
    name = ''
    serdes_num_front = ''
    serdes_num_fabric = ''
    serdes_speed_front = ''
    serdes_speed_fabric = ''
    model = ''
    macs = []

    '''chipset = {
        'name': name,
        'serdes_num_front': serdes_num_front,
        'serdes_num_fabric': serdes_num_fabric,
        'serdes_speed_front': serdes_speed_front,
        'serdes_speed_fabric': serdes_speed_fabric,
        'model': model,
    }'''

    def __init__(self, chip):
        self.name = chip['name']
        self.serdes_num_front = chip['serdes_num_front']
        self.serdes_num_fabric = chip['serdes_num_fabric']
        self.serdes_speed_front = chip['serdes_speed_front']
        self.serdes_speed_fabric = chip['serdes_speed_fabric']
        self.model = chip['model']
        for mac in chip['macs']:
            self.macs.append = mac

        pass
