#!/bin/bash
if python3 ./paint.py
then
	for i in `seq 5`; do
		git commit --allow-empty -m 'commit'
		git push
	done
fi

