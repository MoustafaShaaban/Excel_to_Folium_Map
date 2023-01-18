import folium
import pandas

# Source of the data file:
data = pandas.read_excel('./data.xlsx')

# Create a Pandas DataFrame:
df = pandas.DataFrame(data)

# Uncomment this line to Drop the values with missing data
# df.dropna()

# Show the first 5 rows of the data
df.head()

map = folium.Map(
    location=[28.904346, -81.2650184],
    zoom_start=14,
    tiles="OpenStreetMap"
)

for idx, record in df.iterrows():
    title = record.title
    address = record.address

    popup = folium.Popup(
        html=f"""
                <html>
                    <head>
                        
                    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.2.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-rbsA2VBKQhggwzxH7pPCaAqO46MgnOM80zW1RWuH61DGLwZJEdK2Kadq2F9CUG65" crossorigin="anonymous">

                    </head>
                    <body>
                        <h4 class="text-center">
                            <!-- You can change the number next to `h` to make the text larger or smaller options are (h1 to h6) h1 is the biggest size -->
                            <h3 class="text-center">{title}</h3><br />

                            <p class="text-center">{address}</p>
                        </h4>
                    </body>
                </html>
            """,
        show=True,
        min_width=200,
        max_width=200
    )
    latitude = record.latitude
    longitude = record.longitude

    marker = folium.Marker(
        [longitude, latitude],
        popup=popup,
    ).add_to(map)

map.save("index.html")