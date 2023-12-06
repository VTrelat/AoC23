import * as fs from "fs";
console.log(fs.readFileSync("/Users/vincent/Documents/AoC23/inputs/input6.txt", { encoding: "utf-8", flag: "r" }).trim().split("\n").map((l) =>Number(l.split(":")[1].trim().split(" ").filter((w) => w.length > 0).reduce((acc, v) => acc + v, ""))).reduce((t, d) => {return Math.ceil(Math.sqrt(t * t - 4 * d));}));
