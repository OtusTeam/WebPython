import pytest

from helper import get_least


@pytest.mark.parametrize(
    'src, exp_result',
    [
        ([0, 1, 2, 3], 0),
        ([-1, 0, 1, 2, 3], 0),
        ([-1, 1, 2, 3], 1),
    ]
)
def test_success_get_least(src, exp_result):
    result = get_least(*src)
    assert result == exp_result


def test_fail_get_least():
    args = ['-1', '0', 1, 2, 3]
    with pytest.raises(TypeError):  # Contex Manager
        get_least(*args)
