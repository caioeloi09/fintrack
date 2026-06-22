import pytest
from fintrack.core.budget import Budget


def test_set_and_get_limit():
    budget = Budget()
    budget.set_limit("food", 500)
    assert budget.limit_for("food") == 500


def test_set_limit_negative_raises():
    budget = Budget()
    with pytest.raises(ValueError):
        budget.set_limit("food", -10)


def test_set_limit_zero_raises():
    budget = Budget()
    with pytest.raises(ValueError):
        budget.set_limit("food", 0)


def test_limit_for_unknown_category_is_none():
    budget = Budget()
    assert budget.limit_for("food") is None


def test_remaining_returns_difference():
    budget = Budget()
    budget.set_limit("food", 500)
    assert budget.remaining("food", 200) == 300

def test_remaining_unknown_category_is_none():
    budget = Budget()
    assert budget.remaining("food", 100) is None


def test_is_exceeded_true_when_over_limit():
    budget = Budget()
    budget.set_limit("food", 100)
    assert budget.is_exceeded("food", 150) is True


def test_is_exceeded_false_when_under_limit():
    budget = Budget()
    budget.set_limit("food", 100)
    assert budget.is_exceeded("food", 80) is False


def test_is_exceeded_false_at_exact_limit():
    budget = Budget()
    budget.set_limit("food", 100)
    assert budget.is_exceeded("food", 100) is False


def test_is_exceeded_unknown_category_is_false():
    budget = Budget()
    assert budget.is_exceeded("food", 9999) is False