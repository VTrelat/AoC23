#!/bin/zsh

getinput() {
  if [[ $1 -ge 1 && $1 -le 25 ]]; then
    curl -s --cookie ./.cfg/sessioncookie.txt https://adventofcode.com/2022/day/$1/input > inputs/input$1.txt;
    echo "\U2705\t" "Successfully downloaded input for day $1."
    return 0
  else
    echo "\U274C\t" "Invalid day: $1"
    return 1
  fi
}

js () {
  echo -e "import * as fs from 'fs';
const data = fs.readFileSync('../inputs/input$1.txt', { encoding: 'utf-8', flag: 'r' })";
}

py () {
  echo -e "with open('../inputs/input$1.txt', 'r') as f:
    data = f.read()";
}

makefile () {
  case $2 in
    "py")
      py $1 > solutions/day$1_1.py;
      py $1 > solutions/day$1_2.py;
      ;;
    "js")
      js $1 > solutions/day$1_1.mjs;
      js $1 > solutions/day$1_2.mjs
      ;;
  esac
  echo "\U2705\t" "Successfully created $lang for day $1."
  return 0
}

day=$(date | cut -w -f 2)
lang="py"

while getopts "d:hl:" opt; do
  case $opt in
    d)
      day=$OPTARG
      ;;
    h)
      echo "Usage: aoc.sh [-d day] [-h] [-l lang (py|js) (default: py) (optional)]"
      exit 0
      ;;
    l)
      lang="$OPTARG"
      ;;
    \?)
      echo "\U274C\t" "Invalid option: -$OPTARG" >&2
      exit 1
      ;;
  esac
done

(getinput $day); makefile $day $lang; echo "\n\t\t\t\U1F384\t" "Happy coding!" "\U1F384\n"
