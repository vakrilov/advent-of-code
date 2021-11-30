import { input2 as input } from "./input-1";

const passports = input.split("\n\n");

const check = (str: string, field: string) => {
  return str.indexOf(`${field}:`) >= 0;
};

const valid = passports.filter(
  (str) =>
    check(str, "byr") &&
    check(str, "iyr") &&
    check(str, "eyr") &&
    check(str, "hgt") &&
    check(str, "hcl") &&
    check(str, "ecl") &&
    check(str, "pid")
);

console.log(valid.length);
