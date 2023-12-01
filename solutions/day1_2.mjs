import * as fs from "fs";

console.log(
    fs
        .readFileSync("/Users/vincent/Documents/AoC23/inputs/input1.txt", { encoding: "utf-8", flag: "r" })
        .trim()
        .split("\n")
        .map((l) => l.replaceAll("one", "one1one").replaceAll("two", "two2two").replaceAll("three", "three3three").replaceAll("four", "four4four").replaceAll("five", "five5five").replaceAll("six", "six6six").replaceAll("seven", "seven7seven").replaceAll("eight", "eight8eight").replaceAll("nine", "nine9nine"))
        .map((l) => l.split("").reduce((acc, c) => acc + (c >= "0" && c <= "9" ? c : ""), ""))
        .map((n) => parseInt(n[0] + n[n.length - 1]))
        .reduce((acc, n) => acc + n, 0)
);
