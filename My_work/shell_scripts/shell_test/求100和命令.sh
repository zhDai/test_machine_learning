#!/bin/bash

#100整数之和

declare -i sum_value
sum_value=0
declare -i i=1

while [ $i -le 100 ]; do
	let sum_value+=$i
	let i++
done

echo "总和：$sum_value"
