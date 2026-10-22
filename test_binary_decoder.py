import pytest
from binary_decoder_gui import decode_bits, encode_text


def test_decode_spaced():
    assert decode_bits("01001000 01101001") == "Hi"


def test_decode_no_spaces():
    assert decode_bits("0100100001101001") == "Hi"


def test_decode_newlines():
    assert decode_bits("01001000\n01101001") == "Hi"


def test_decode_empty():
    with pytest.raises(ValueError):
        decode_bits("")


def test_decode_invalid_characters():
    with pytest.raises(ValueError):
        decode_bits("0102")


def test_decode_wrong_length():
    with pytest.raises(ValueError):
        decode_bits("0101")


def test_encode_hi():
    assert encode_text("Hi") == "01001000 01101001"


def test_encode_empty():
    with pytest.raises(ValueError):
        encode_text("")


def test_encode_unsupported_character():
    with pytest.raises(ValueError):
        encode_text("€")


def test_round_trip():
    assert decode_bits(encode_text("Stream Visionquest")) == "Stream Visionquest"