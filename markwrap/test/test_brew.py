import markwrap.brew as brew
import logging


'''
Not asserting Homebrew is actually called with correct arguments.
Please manually test and verify before committing changes.
'''
def test_brew_list(caplog):
	## ARRANGE ##
	caplog.set_level(logging.DEBUG)
	EXPECTED_LOG_1 = "INFO     root:brew.py:14 Process started   :  /usr/local/bin/brew list -1"
	EXPECTED_LOG_2 = "INFO     root:brew.py:19 Process terminated:  /usr/local/bin/brew list -1"

	## ACT ##
	brew.list()

	## ASSERT ##
	lines = caplog.text.splitlines()
	assert len(lines) == 2
	assert lines[0] == EXPECTED_LOG_1
	assert lines[1] == EXPECTED_LOG_2

def test_brew_update(caplog):
	## ARRANGE ##
	caplog.set_level(logging.DEBUG)
	EXPECTED_LOG_1 = "INFO     root:brew.py:22 Process started   :  /usr/local/bin/brew update"
	EXPECTED_LOG_2 = "INFO     root:brew.py:27 Process terminated:  /usr/local/bin/brew update"

	## ACT ##
	brew.update()

	## ASSERT ##
	lines = caplog.text.splitlines()
	assert len(lines) == 2
	assert lines[0] == EXPECTED_LOG_1
	assert lines[1] == EXPECTED_LOG_2

def test_brew_upgrade(caplog):
	## ARRANGE ##
	caplog.set_level(logging.DEBUG)
	EXPECTED_LOG_1 = "INFO     root:brew.py:30 Process started   :  /usr/local/bin/brew upgrade"
	EXPECTED_LOG_2 = "INFO     root:brew.py:35 Process terminated:  /usr/local/bin/brew upgrade"

	## ACT ##
	brew.upgrade()

	## ASSERT ##
	lines = caplog.text.splitlines()
	assert len(lines) == 2
	assert lines[0] == EXPECTED_LOG_1
	assert lines[1] == EXPECTED_LOG_2

def test_brew_validateInstall(caplog):
	## ARRANGE ##
	caplog.set_level(logging.DEBUG)
	EXPECTED_LOG_1 = "INFO     root:brew.py:38 Validating Homebrew install at /usr/local/bin/brew"
	EXPECTED_LOG_2 = "INFO     root:brew.py:43 Homebrew found at /usr/local/bin/brew"
	EXPECTED_LOG_3 = "INFO     root:brew.py:48 Validated Homebrew install at /usr/local/bin/brew"

	## ACT ##
	brew.validateInstall()

	## ASSERT ##
	lines = caplog.text.splitlines()
	assert len(lines) == 3
	assert lines[0] == EXPECTED_LOG_1
	assert lines[1] == EXPECTED_LOG_2
	assert lines[2] == EXPECTED_LOG_3
