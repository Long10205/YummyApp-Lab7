class GPSSignalLostError(Exception):
    """Ngoai le khi thiet bi mat tin hieu GPS."""


def get_current_location():
    """Lay toa do GPS; trong unit test se duoc mock."""
    return (10.0, 105.0)
