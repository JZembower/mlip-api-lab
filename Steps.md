1. Clone git repository
2. Create venv and install packages.
3. Run app.py to check functionality.
4. After a successful run, update analyze.py with the API key connection to .env file along with the get_itinerary function.
   1. Don't commit an API key hardcoded into the analyze.py because this is a security problem.
   2. get_itinerary function needs to have good descriptions of the response and specify JSON format. 
5. If successful, check this run on the app and perform an itinerary check using the curl command for a certain region.
   1. An example is: curl "http://localhost:8000/api/v1/itinerary?destination=Kyoto"
6. After a successful JSON response, commit changes ensuring gitignore accounts for the files that must remain secure to me.