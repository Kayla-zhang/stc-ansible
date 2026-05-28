
play:
	ansible-playbook main.yaml

debug:
	ansible-playbook main.yaml -vvvv

unittest: yapf
	pytest

test: yapf
	python -m tests.playbook $(TEST_LABSERVER) --all

yapf:
	@yapf --style '{based_on_style: google, indent_width: 4, column_limit: 120}' -i module_utils/*.py
	@yapf --style '{based_on_style: google, indent_width: 4, column_limit: 120}' -i library/*.py
	@yapf --style '{based_on_style: google, indent_width: 4, column_limit: 120}' -i tests/*.py

lint:
	pylint --rcfile=.pylint.rc module_utils/*.py

TEST_SUBDIR :=./playbooks/
# Set TEST_LABSERVER to the IP/hostname of your VIAVI TC LabServer
TEST_LABSERVER ?= 127.0.0.1

FILES := $(shell ls $(TEST_SUBDIR)*.yaml)
jenkins-regression:
	$(foreach N, $(FILES), python emulator.py -l $(TEST_LABSERVER) $(N);)

-include makefile.local
