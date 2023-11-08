#!/bin/zsh

COOKIE=$(cat /Users/vincent/Documents/AoC23/.cfg/sessioncookie.txt | grep 'session' | cut -w -f 7)
YEAR=$(cat /Users/vincent/Documents/AoC23/.cfg/config.txt | grep 'YEAR' | cut -d = -f 2)

submit () {
    SUBMIT_URL="https://adventofcode.com/$1/day/$2/answer"
    
    response=$(curl -s -X POST -b "session=${COOKIE}" -d "level=$3&answer=$4" "${SUBMIT_URL}")

    case "$response" in
        *"That's the right answer!"*)
        echo "\U2705\t" "That's the right answer!"
        ;;
        *"not the"*)
        echo "\U274C\t" "That's not the right answer."
        ;;
        *"too recently"*)
        echo "\U274C" $(echo $response | awk '/<article><p>/,/<\/p><\/article>/' | sed -e 's/<[^>]*>//g' | sed -e 's/^[[:space:]]*//g' | sed -e 's/[[:space:]]*$//g' | cut -d "[" -f 1)
        ;;
        *)
        echo "\U274C" "There was an issue with your submission."
        ;;
    esac

    # response=$(echo "$response" | awk '/<article><p>/,/<\/p><\/article>/')

    # echo "$response" | sed -e 's/<[^>]*>//g' | sed -e 's/^[[:space:]]*//g' | sed -e 's/[[:space:]]*$//g'
}

# Set the puzzle's day and year.
DAY=$(date | cut -w -f 3)
LEVEL="1"
ANSWER=""

if [ -t 0 ]; then
    while getopts "y:d:l:ha:" opt; do
    case $opt in
        y)
            year=$OPTARG
            ;;
        d)
            day=$OPTARG
            ;;
        h)
            echo "Usage: aoc.sh [-y year] [-d day] [-h] [-l level (1|2) (default: 1)] [-a answer]"
            exit 0
            ;;
        l)
            LEVEL="$OPTARG"
            ;;
        a)
            ANSWER="$OPTARG"
            ;;
        \?)
        echo "\U274C\t" "Invalid option: -$OPTARG" >&2
        exit 1
        ;;
    esac
    done
else
  # Input from stdin, read answer from stdin
  read -r ANSWER
fi

echo "\t\t\t\U1F384\t" "Submitting answer for day $DAY, year $YEAR, level $LEVEL, answer $ANSWER" "\U1F384\n"
submit $YEAR $DAY $LEVEL $ANSWER