for var in "$@"
do
    curl -X POST planner:3000/register  -H "Content-Type: application/json"  -d "{\"url\": \"http://worker:$var\"}"
done
