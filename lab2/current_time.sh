END_HOUR=18
END_MINUTE=0

CURRENT_HOUR=$(date +%H)
CURRENT_MINUTE=$(date +%M)
CURRENT_TIME=$(date +%H:%M)

CURRENT_TOTAL_MIN=$((10#$CURRENT_HOUR * 60 + 10#$CURRENT_MINUTE))
END_TOTAL_MIN=$((END_HOUR * 60 + END_MINUTE))

DIFF=$((END_TOTAL_MIN - CURRENT_TOTAL_MIN))

if [ $DIFF -le 0 ]; then
    echo "Current time: $CURRENT_TIME. Work day has already ended."
else
    HOURS_LEFT=$((DIFF / 60))
    MINUTES_LEFT=$((DIFF % 60))
    echo "Current time: $CURRENT_TIME. Work day ends after $HOURS_LEFT hours and $MINUTES_LEFT minutes."
fi
