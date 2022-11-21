#!/usr/bin/env ts-node
let n = 1;
let xn = 8;
let yn = 9;

const target = 325489;

while (yn < target) {

    xn += 8;
    if(yn + xn > target){
        break;
    }
    n++;
    yn += xn;

    console.log(yn);
}

console.log(`N: ${n}`);
console.log(`Left: ${target - yn}`);