from streamdb import store


def test_import():
    assert store.Config().seed == 0
