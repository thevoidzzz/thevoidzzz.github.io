"""The page stays a static record of numbers a command already printed."""

from pathlib import Path

PAGE = Path(__file__).resolve().parents[1] / "index.html"


def _text() -> str:
    return PAGE.read_text(encoding="utf-8")


def test_the_first_screen_is_the_wait() -> None:
    text = _text()
    heading = text.index("<h1>Waiting</h1>")
    first_link = text.index("https://github.com/thevoidzzz/")
    assert heading < first_link
    assert "It has not committed it." in text
    assert "status to committed" in text


def test_the_local_order_is_the_printed_demo() -> None:
    text = _text()
    marks = [
        "python -m anchora.sample",
        "8001",
        "Book accruals",
        "8002",
        "1750.50",
        "Drop the journal lines.",
        "8000",
        "trajectory_pass_rate 0.667",
        "python -m keel",
        "block_rate 1.000",
    ]
    positions = [text.index(mark) for mark in marks]
    assert positions == sorted(positions)
    assert "2-core" in text
    assert "does not create one" in text


def test_omissions_stay_on_the_page() -> None:
    text = _text()
    for mark in (
        "missed_refusals 9",
        "retrieval_ms_p95 11.034",
        "english_hit_at_5 0.000",
        "spanish_hit_at_5 1.000",
        "trajectory_pass_rate 0.667",
        "completed_tasks 3",
        "false_refusals 0",
        "false_positives 0",
        "https://github.com/thevoidzzz/anchora",
        "https://github.com/thevoidzzz/numera",
        "https://github.com/thevoidzzz/keel",
        "https://github.com/thevoidzzz/latch",
    ):
        assert mark in text


def test_the_page_has_no_client_and_no_form() -> None:
    text = _text().lower()
    assert "<form" not in text
    assert "<script" not in text
    assert "fetch(" not in text
