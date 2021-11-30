#!/usr/bin/env ts-node
import * as fs from "fs";
// const fs = require('fs')

const data: string = fs.readFileSync("input-9.txt", "utf8");

// console.log(data);

let inGarbage = false;
let refined = "";
let gc = 0;

for (let i = 0; i < data.length; i++) {
  const sym = data[i];
  if (sym === "!") {
    i++;
  } else if (!inGarbage) {
    if (sym === "{" || sym === "}") {
      refined += sym;
    }
    if (sym === "<") {
      inGarbage = true;
    }
  } else if (inGarbage) {
    if (sym === ">") {
      inGarbage = false;
    } else {
      gc++;
    }
  }
}

console.log(refined);

let score = 0;
let lvl = 0;
for (let i = 0; i < refined.length; i++) {
  if (refined[i] === "{") {
    lvl++;
    score += lvl;
  } else {
    lvl--;
  }
//   console.log(lvl, score);
}

console.log(score);
console.log(gc);

