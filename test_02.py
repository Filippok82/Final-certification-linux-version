import logging
from checkout import checkout


def test_step4():
    logging.info("Test4 Starting")
    assert checkout("nikto -h https://test-stand.gb.ru/ -ssl -Tuning 4", "0 error(s)"), "Test4 Fail"
