import pytest
from core.MasterCode import MJCI

def test_execute_handshake_changes_status_and_returns_message():
    instance = MJCI(user="tester")
    assert instance.connection_status == "Awaiting_Handshake"
    msg = instance.execute_handshake()
    assert instance.connection_status == "CONNECTED_VIA_GRACE"
    assert "Access Granted" in msg

def test_apply_patch_returns_expected_text():
    instance = MJCI(user="tester")
    result = instance.apply_patch({"type": "test", "details": "none"})
    assert "Analyzing Error" in result
    assert "System Restored" in result