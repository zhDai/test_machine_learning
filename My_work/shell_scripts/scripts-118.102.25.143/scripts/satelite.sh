#!/bin/bash

initpath=$1
if [ -d $initpath ];then
	cd $initpath
	for name in `ls`
	do
		file1=${initpath}/${name}
		if [ -d ${file1} ];then
			cd $file1
			for name1 in `ls`
			do
				file2=$file1/$name1
				if [ -d ${file2} ];then
					cd $file2
					export PGPASSWORD=123456
					for name2 in `ls`
					do
						file3=$file2/$name2
						/opt/PostgreSQL/9.5/bin/psql -U zhdai -d zbase -c "insert into satelite.Japan(date,adress,picpath)values("${name2:0-14:10}",'"$name"','"$file3"')"

					done
				fi
			done
		fi
	done
fi


