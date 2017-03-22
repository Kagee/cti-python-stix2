import datetime as dt
import uuid

from .constants import FAKE_TIME
from .fixtures import clock, uuid4  # noqa: F401


def test_clock(clock):  # noqa: F811
    assert dt.datetime.now() == FAKE_TIME


def test_my_uuid4_fixture(uuid4):  # noqa: F811
    assert uuid.uuid4() == "00000000-0000-0000-0000-000000000001"
    assert uuid.uuid4() == "00000000-0000-0000-0000-000000000002"
    assert uuid.uuid4() == "00000000-0000-0000-0000-000000000003"
    for _ in range(256):
        uuid.uuid4()
    assert uuid.uuid4() == "00000000-0000-0000-0000-000000000104"
