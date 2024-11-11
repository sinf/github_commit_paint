#!/bin/bash
if python3 ./paint.py
then
	git commit --allow-empty -m 'commit'
	git push
fi

