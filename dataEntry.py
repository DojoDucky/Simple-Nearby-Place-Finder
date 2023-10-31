import sqlite3

connection = sqlite3.connect('placesData.db')
cursor = connection.cursor()

cursor.execute(""" 
CREATE TABLE IF NOT EXISTS locations (
        place_type TEXT,
        place_name TEXT,
        place_address TEXT,
        price_range INTEGER
)
""")

# Define the data as a list of tuples
data = [
    ('Restaurant', 'Shivneri Misal', 'Solapur Pune Highway', 150),
    ('Restaurant', 'Mahalaxmi Dosa & Pavbhaji Center', 'F2R9+JXR, mit corner, near by gurudatta cells', 200),
    ('Restaurant', 'Shree Ganesh Snacks', 'Opposite Mahadev Jewellers Loni Kalbhor', 180),
    ('Restaurant', 'Samiksha Hotel and Biryani House', 'Near Loni Railway Station, Pune-Solapur Road', 250),
    ('Restaurant', 'A1 Dum Biryani House', 'Opposite Vishwaraj Hospital, Loni Kalbhor', 300),
    ('Restaurant', 'Hotel Jay Bhavani', 'Shop 1, Shivsai Complex, Shevalwadi Phata, Pune-Solapur Road', 400),
    ('Restaurant', 'Hotel Samrat', 'Shop 14/2, Opposite Akashwani, Pune-Solapur Road', 500),
    ('Coffee', 'Brew Trend', 'Mit Corner', 300)
]

# Insert the data into the table
cursor.executemany("INSERT INTO locations VALUES (?, ?, ?, ?)", data)

connection.commit()

connection.close()
