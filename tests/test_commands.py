"""Tests for TOTO Washlet command matching."""

from __future__ import annotations

import pytest

from custom_components.toto_washlet.commands import TotoData, TotoWashletCode


def test_matches_exact_frame() -> None:
    """An exact frame matches its command."""
    assert (
        TotoWashletCode.from_frames(TotoWashletCode.REAR.value)
        is TotoWashletCode.REAR
    )


@pytest.mark.parametrize(
    ("frame", "expected_code"),
    [
        (TotoData(0x80, 0x2, 0x4), TotoWashletCode.REAR),
        (TotoData(0xA8, 0x2, 0x4), TotoWashletCode.SOFT_REAR),
        (TotoData(0x40, 0x2, 0x4), TotoWashletCode.FRONT),
        (TotoData(0x91, 0x2, 0x4), TotoWashletCode.SOFT_FRONT),
    ],
)
def test_matches_unique_single_frame_command_with_different_rc_code(
    frame: TotoData,
    expected_code: TotoWashletCode,
) -> None:
    """A unique command byte matches even when its RC fields differ."""
    assert TotoWashletCode.from_frames([frame]) is expected_code


def test_does_not_match_ambiguous_command_byte() -> None:
    """An RC mismatch does not match a shared stateful command byte."""
    assert TotoWashletCode.from_frames([TotoData(0xEC, 0x4, 0x4)]) is None


def test_does_not_match_multiframe_command_by_command_byte() -> None:
    """Command-byte fallback does not apply to multi-frame commands."""
    assert TotoWashletCode.from_frames([TotoData(0xDA, 0x0, 0x0)]) is None
