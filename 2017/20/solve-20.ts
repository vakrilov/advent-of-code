#!/usr/bin/env ts-node
import * as fs from "fs";
// const fs = require('fs')

const data: string = fs.readFileSync("input-20.txt", "utf8");

// console.log(data);

const lines = data.split("\n");
const accs = [];
for (let line of lines) {
  let strA = line.substring(line.indexOf("a=") + 3);
  strA = strA.substr(0, strA.length - 1);
  // console.log(strA);

  const [x, y, z] = strA.split(",").map((s) => parseInt(s));

  accs.push(Math.abs(x) + Math.abs(y) + Math.abs(z));
}

function findIndexOfGreatest(array) {
  var greatest;
  var indexOfGreatest;
  for (var i = 0; i < array.length; i++) {
    if (!greatest || array[i] < greatest) {
      greatest = array[i];
      indexOfGreatest = i;
    }
  }
  return indexOfGreatest;
}

const idx = findIndexOfGreatest(accs);

console.log(accs.join(","));

console.log(idx, accs[idx]);
