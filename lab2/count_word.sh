if [ $# -ne 2 ]; then
    echo "Usage: $0 <filename> <word>"
    exit 1
fi

FILE=$1
WORD=$2

if [ ! -f "$FILE" ]; then
    echo "Error: File '$FILE' not found."
    exit 1
fi

COUNT=$(grep -ow "$WORD" "$FILE" | wc -l)
echo "The word '$WORD' appears $COUNT time(s) in '$FILE'."
