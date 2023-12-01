import * as fs from "fs";

console.log(
    fs
        .readFileSync("/Users/vincent/Documents/AoC23/inputs/input1.txt", { encoding: "utf-8", flag: "r" })
        .trim()
        .split("\n")
        .map((l, i) => l.split("").reduce((acc, c) => acc + (c >= "0" && c <= "9" ? c : ""), ""))
        .map((n) => parseInt(n[0] + n[n.length - 1]))
        .reduce((acc, n) => acc + n, 0)
);
