import json

from src.jsonapi import jsonapi


def test_encode_complex_number():
    cx = complex(1,2)

    actual = json.dumps(cx, cls=jsonapi.BetterEncoder)

    assert actual == '{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}'


def test_decode_complex_number():
    encoded_cx = json.dumps(complex(1,2), cls=jsonapi.BetterEncoder)

    actual = json.loads(encoded_cx, cls=jsonapi.BetterDecoder)

    assert actual == complex(1,2)


def test_encode_range():
    rg = range(1, 10, 3)

    actual = json.dumps(rg, cls=jsonapi.BetterEncoder)

    assert actual == '{"start": 1, "stop": 10, "step": 3, "__extended_json_type__": "range"}'


def test_decode_range():
    encoded_rg = json.dumps(range(1,10,3), cls=jsonapi.BetterEncoder)

    actual = json.loads(encoded_rg, cls=jsonapi.BetterDecoder)

    assert actual == range(1,10,3)