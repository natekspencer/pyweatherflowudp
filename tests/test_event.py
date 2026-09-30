"""Test the module version."""

from datetime import datetime, timezone

from pyweatherflowudp.const import UNIT_KILOMETERS
from pyweatherflowudp.event import CustomEvent, LightningStrikeEvent


def test_custom_event() -> None:
    """Test custom event."""
    timestamp = datetime.now(timezone.utc).timestamp()
    event = CustomEvent(timestamp, "Test")
    assert event.epoch == timestamp
    assert event.timestamp == datetime.fromtimestamp(timestamp, timezone.utc)
    assert event.name == "Test"


def test_lightning_strike_event_distance() -> None:
    """Test the lightning strike distance is None when the storm is out of range."""
    assert LightningStrikeEvent(1493322445, 27, 3848).distance == 27 * UNIT_KILOMETERS
    assert LightningStrikeEvent(1493322445, 63, 3848).distance is None
