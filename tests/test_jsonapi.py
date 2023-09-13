from src.jsonapi import jsonapi


def test_encode_complex():
    cx = complex(1, 2)

    actual = jsonapi.dumps(cx)

    assert actual == '{"real": 1.0, "imag": 2.0, "__extended_json_type__": "complex"}'


def test_decode_complex():
    encoded = jsonapi.dumps(complex(1, 2))

    actual = jsonapi.loads(encoded)

    assert actual == complex(1, 2)


def test_encode_range():
    rg = range(4)

    actual = jsonapi.dumps(rg)

    assert actual == '{"start": 0, "stop": 4, "step": 1, "__extended_json_type__": "range"}'


def test_decode_range():
    encoded = jsonapi.dumps(range(4))

    actual = jsonapi.loads(encoded)

    assert actual == range(4)