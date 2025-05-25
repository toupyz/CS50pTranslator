import csv
import os
import builtins
from unittest import mock
from project import add_expense, remove_expense, view_expense, plot_expenses, filename

# Utility to reset the test file
def reset_csv():
    with open(filename, "w", newline='') as file:
        writer = csv.DictWriter(file, fieldnames=["type", "amount"])
        writer.writeheader()
        writer.writerow({"type": "food", "amount": 10.0})
        writer.writerow({"type": "fun", "amount": 20.0})

def test_add_expense(monkeypatch):
    reset_csv()
    monkeypatch.setattr('builtins.input', lambda _: "bills" if "type" in _ else "30")

    add_expense()

    with open(filename, newline='') as file:
        lines = list(csv.DictReader(file))
        assert {"type": "bills", "amount": "30.0"} in lines

def test_remove_expense(monkeypatch, capsys):
    reset_csv()
    inputs = iter(["food", "10"])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    remove_expense()

    with open(filename, newline='') as file:
        lines = list(csv.DictReader(file))
        assert not any(row['type'] == "food" and row['amount'] == "10.0" for row in lines)

def test_view_expense(capsys):
    reset_csv()
    view_expense()
    captured = capsys.readouterr()
    assert "food" in captured.out
    assert "10.0" in captured.out

def test_plot_expenses(monkeypatch):
    # Patch plt.show to prevent GUI from opening during test
    with mock.patch("matplotlib.pyplot.show"):
        reset_csv()
        plot_expenses()  # If no exceptions thrown = pass

