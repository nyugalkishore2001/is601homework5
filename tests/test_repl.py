import pytest
from unittest.mock import patch
from io import StringIO
from repl import start_repl

def test_repl_add(monkeypatch, capsys):
    inputs = ["1", "2", "3", "7"]  # Add 2 + 3, then exit
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    
    start_repl()
    
    captured = capsys.readouterr()
    assert "The result of 2 + 3 is: 5" in captured.out

def test_repl_view_history(monkeypatch, capsys):
    inputs = ["1", "2", "3", "5", "7"]  # Add 2 + 3, view history, then exit
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    
    start_repl()
    
    captured = capsys.readouterr()
    assert "Calculation History:" in captured.out
    assert "2 + 3 = 5" in captured.out

def test_repl_clear_history(monkeypatch, capsys):
    inputs = ["1", "2", "3", "6", "5", "7"]  # Add 2 + 3, clear history, view history, then exit
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    
    start_repl()
    
    captured = capsys.readouterr()
    assert "Calculation history cleared." in captured.out
    assert "No history available." in captured.out

def test_repl_exit(monkeypatch, capsys):
    inputs = ["7"]  # Exit immediately
    monkeypatch.setattr('builtins.input', lambda _: inputs.pop(0))
    
    start_repl()
    
    captured = capsys.readouterr()
    assert "Exiting REPL. Goodbye!" in captured.out