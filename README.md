# AirBnB MongoDB Analysis

The following code uses MongoDB CRUD to perform a set of analysis on data retrieved from AirBnB, data which can be accessed [here](http://data.insideairbnb.com/sweden/stockholms-l%C3%A4n/stockholm/2022-12-29/data/listings.csv.gz). Below are the first five rows of data in markdown format:

|    | id     | listing_url                         | scrape_id      | last_scraped | source          | name                                               | description                         | neighborhood_overview                | picture_url                                                                                             | host_id | host_url                                  | host_name        | host_since | host_location       | host_about                          | host_response_time | host_response_rate | host_acceptance_rate | host_is_superhost | host_thumbnail_url                                                                                         | host_picture_url                                                                                              | host_neighbourhood | host_listings_count | host_total_listings_count | host_verifications                 | host_has_profile_pic | host_identity_verified | neighbourhood                         | neighbourhood_cleansed  | neighbourhood_group_cleansed | latitude | longitude | property_type               | room_type       | accommodates | bathrooms | bathrooms_text   | bedrooms | beds | amenities                            | price               | minimum_nights    | maximum_nights | minimum_minimum_nights | maximum_minimum_nights | minimum_maximum_nights | maximum_maximum_nights | minimum_nights_avg_ntm | maximum_nights_avg_ntm | calendar_updated | has_availability | availability_30 | availability_60 | availability_90 | availability_365 | calendar_last_scraped | number_of_reviews | number_of_reviews_ltm | number_of_reviews_l30d | first_review | last_review | review_scores_rating | review_scores_accuracy | review_scores_cleanliness | review_scores_checkin | review_scores_communication | review_scores_location | review_scores_value | license | instant_bookable | calculated_host_listings_count | calculated_host_listings_count_entire_homes | calculated_host_listings_count_private_rooms | calculated_host_listings_count_shared_rooms | reviews_per_month |      |      |      |
|----|--------|-------------------------------------|----------------|--------------|-----------------|----------------------------------------------------|-------------------------------------|--------------------------------------|---------------------------------------------------------------------------------------------------------|---------|-------------------------------------------|------------------|------------|---------------------|-------------------------------------|--------------------|--------------------|----------------------|-------------------|------------------------------------------------------------------------------------------------------------|---------------------------------------------------------------------------------------------------------------|--------------------|---------------------|---------------------------|------------------------------------|----------------------|------------------------|---------------------------------------|-------------------------|------------------------------|----------|-----------|-----------------------------|-----------------|--------------|-----------|------------------|----------|------|--------------------------------------|---------------------|-------------------|----------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------------|------------------|------------------|-----------------|-----------------|-----------------|------------------|-----------------------|-------------------|-----------------------|------------------------|--------------|-------------|----------------------|------------------------|---------------------------|-----------------------|-----------------------------|------------------------|---------------------|---------|------------------|--------------------------------|---------------------------------------------|----------------------------------------------|---------------------------------------------|-------------------|------|------|------|
| 0  | 75590  | https://www.airbnb.com/rooms/75590  | 20221229235426 | 2022-12-30   | city scrape     | Amazing nature location by a lake                  | "Apartment on the top floor, ov..." | Expect a wonderful stay in bea...    | https://a0.muscache.com/pictures/7430cc80-7a4f-4642-8eca-46cfa917dd08.jpg                               | 397766  | https://www.airbnb.com/users/show/397766  | Peter            | 2011-02-18 | "Stockholm, Sweden" | Easy going and pragmatic when ...   |                    |                    | 0%                   | f                 | https://a0.muscache.com/im/users/397766/profile_pic/1372944928/original.jpg?aki_policy=profile_small       | https://a0.muscache.com/im/users/397766/profile_pic/1372944928/original.jpg?aki_policy=profile_x_medium       |                    | 1                   | 2                         | "['email', 'phone', 'work_email']" | t                    | t                      | "Nacka, Stockholm County, Sweden"     | Skarpn√§cks             |                              | 59.30117 | 18.12833  | Entire rental unit          | Entire home/apt | 3            |           | 1 bath           | 2.0      | 1.0  | "[""Shampoo""                        | ""Iron""            | ""Long term..."   | $91.1          | 30                     | 100                    | 30.0                   | 30.0                   | 100.0                  | 100.0                  | 30.0             | 100.0            |                 | t               | 28              | 58               | 88                    | 178               | 2022-12-30            | 10                     | 0            | 0           | 2013-08-02           | 2016-07-08             | 4.8                       | 5.0                   | 4.89                        | 4.89                   | 5.0                 | 4.78    | 4.78             |                                | f                                           | 1                                            | 1                                           | 0                 | 0    | 0.09 |      |
| 1  | 164448 | https://www.airbnb.com/rooms/164448 | 20221229235426 | 2022-12-30   | city scrape     | Double room in central Stockholm with Wi-Fi        | I am renting out a nice double...   |                                      | https://a0.muscache.com/pictures/1101571/13429928_original.jpg                                          | 784312  | https://www.airbnb.com/users/show/784312  | Li               | 2011-07-06 | "Stockholm, Sweden" | "I am a recently retired lady, ..." | within an hour     | 100%               | 100%                 | t                 | https://a0.muscache.com/im/users/784312/profile_pic/1314897997/original.jpg?aki_policy=profile_small       | https://a0.muscache.com/im/users/784312/profile_pic/1314897997/original.jpg?aki_policy=profile_x_medium       | S√∂dermalm         | 2                   | 2                         | "['email', 'phone']"               | t                    | t                      |                                       | S√∂dermalms             |                              | 59.31389 | 18.06087  | Private room in rental unit | Private room    | 2            |           | 1 shared bath    | 1.0      | 2.0  | "[""Dryer""                          | ""Bathtub""         | ""Smoke al..."    | $82.94         | 3                      | 300                    | 3.0                    | 3.0                    | 300.0                  | 300.0                  | 3.0              | 300.0            |                 | t               | 27              | 57               | 87                    | 177               | 2022-12-30            | 355                    | 33           | 0           | 2011-07-30           | 2022-11-27             | 4.85                      | 4.87                  | 4.81                        | 4.96                   | 4.97                | 4.83    | 4.76             |                                | t                                           | 2                                            | 0                                           | 2                 | 0    | 2.55 |      |
| 2  | 170651 | https://www.airbnb.com/rooms/170651 | 20221229235426 | 2022-12-30   | city scrape     | Petit Charm Rooftop next to heaven                 | My place is perfect for 1 pers...   |                                      | https://a0.muscache.com/pictures/74dc2c29-1f7a-49ed-8b4f-d845183740d4.jpg                               | 814021  | https://www.airbnb.com/users/show/814021  | Marie            | 2011-07-13 | "Stockholm, Sweden" | Im a happy person living with ...   | within a few hours | 100%               | 29%                  | f                 | https://a0.muscache.com/im/pictures/user/137c6966-c9a2-42a9-8b8e-dbb1e7dd0a24.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/137c6966-c9a2-42a9-8b8e-dbb1e7dd0a24.jpg?aki_policy=profile_x_medium | S√∂dermalm         | 1                   | 1                         | "['email', 'phone']"               | t                    | t                      |                                       | S√∂dermalms             |                              | 59.31702 | 18.02946  | Entire condo                | Entire home/apt | 2            |           | 1.5 baths        | 1.0      | 2.0  | "[""Shampoo""                        | ""Private hot tub"" | ..."              | $101.28        | 4                      | 30                     | 4.0                    | 4.0                    | 30.0                   | 30.0                   | 4.0              | 30.0             |                 | t               | 9               | 23               | 33                    | 248               | 2022-12-30            | 42                     | 3            | 0           | 2011-08-14           | 2022-10-02             | 4.68                      | 4.84                  | 4.55                        | 4.89                   | 4.92                | 4.84    | 4.74             |                                | f                                           | 1                                            | 1                                           | 0                 | 0    | 0.3  |      |
| 3  | 206221 | https://www.airbnb.com/rooms/206221 | 20221229235426 | 2022-12-30   | city scrape     | Doubleroom at S√∂dermalm &trendySofo               | <b>The space</b><br />The regi...   |                                      | https://a0.muscache.com/pictures/1792713/2c120093_original.jpg                                          | 1022374 | https://www.airbnb.com/users/show/1022374 | Elisabeth        | 2011-08-26 | Sweden              | I'm a positive person who love...   | a few days or more | 0%                 | 0%                   | f                 | https://a0.muscache.com/im/users/1022374/profile_pic/1344590239/original.jpg?aki_policy=profile_small      | https://a0.muscache.com/im/users/1022374/profile_pic/1344590239/original.jpg?aki_policy=profile_x_medium      |                    | 1                   | 2                         | "['email', 'phone']"               | t                    | f                      |                                       | S√∂dermalms             |                              | 59.31074 | 18.08128  | Shared room in rental unit  | Shared room     | 2            |           | 1 shared bath    | 1.0      | 2.0  | "[""Shampoo""                        | ""Iron""            | ""Hangers""       | ..."           | $64.22                 | 3                      | 14                     | 3.0                    | 3.0                    | 14.0                   | 14.0             | 3.0              | 14.0            |                 | t               | 28               | 58                    | 88                | 360                   | 2022-12-30             | 79           | 0           | 0                    | 2011-11-30             | 2019-12-08                | 4.92                  | 4.83                        | 4.83                   | 4.94                | 4.9     | 4.94             | 4.83                           |                                             | f                                            | 1                                           | 0                 | 0    | 1    | 0.59 |
| 4  | 208366 | https://www.airbnb.com/rooms/208366 | 20221229235426 | 2022-12-30   | city scrape     | Central apt. in Sofo .Perfect 4 Families & Kids    | <b>The space</b><br />LOCATION...   |                                      | https://a0.muscache.com/pictures/5648534/0238ff82_original.jpg                                          | 993889  | https://www.airbnb.com/users/show/993889  | Bartholomew Lion | 2011-08-19 | "Stockholm, Sweden" | "Stockholm, Sweden. Non smoking..." | within an hour     | 100%               | 17%                  | f                 | https://a0.muscache.com/im/pictures/user/d09de775-8991-48db-b3c6-e5f0f58674f5.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/d09de775-8991-48db-b3c6-e5f0f58674f5.jpg?aki_policy=profile_x_medium |                    | 1                   | 1                         | "['email', 'phone']"               | t                    | t                      |                                       | S√∂dermalms             |                              | 59.30903 | 18.08032  | Entire condo                | Entire home/apt | 6            |           | 1 bath           | 1.0      | 4.0  | "[""Children\u2019s books and to..." | $79.58              | 3                 | 1125           | 3.0                    | 3.0                    | 1125.0                 | 1125.0                 | 3.0                    | 1125.0                 |                  | t                | 0               | 2               | 2               | 4                | 2022-12-30            | 41                | 0                     | 0                      | 2012-06-05   | 2021-12-20  | 4.69                 | 4.57                   | 4.43                      | 4.95                  | 4.92                        | 4.7                    | 4.49                |         | f                | 1                              | 1                                           | 0                                            | 0                                           | 0.32              |      |      |      |
| 5  | 220851 | https://www.airbnb.com/rooms/220851 | 20221229235426 | 2022-12-30   | city scrape     | One room in appartement                            | Welcome!<br /><br /><b>The spa...   | Many restaurangs wery close an...    | https://a0.muscache.com/pictures/2085606/7a706118_original.jpg                                          | 412283  | https://www.airbnb.com/users/show/412283  | Fredric          | 2011-02-27 | "Stockholm, Sweden" | I am into arts yoga meditation...   | a few days or more | 33%                | 52%                  | f                 | https://a0.muscache.com/im/pictures/user/e0c057ab-8506-4226-8ed6-109de8c6fc4e.jpg?aki_policy=profile_small | https://a0.muscache.com/im/pictures/user/e0c057ab-8506-4226-8ed6-109de8c6fc4e.jpg?aki_policy=profile_x_medium | Kungsholmen        | 2                   | 4                         | "['email', 'phone']"               | t                    | t                      | "Stockholm, Stockholm County, Sweden" | Kungsholmens            |                              | 59.33351 | 18.03693  | Private room in rental unit | Private room    | 1            |           | 1 shared bath    | 1.0      | 1.0  | "[""BBQ grill""                      | ""Bathtub""         | ""Oven..."        | $43.2          | 3                      | 20                     | 3.0                    | 3.0                    | 20.0                   | 20.0                   | 3.0              | 20.0             |                 | t               | 0               | 0                | 0                     | 243               | 2022-12-30            | 59                     | 8            | 0           | 2011-09-29           | 2022-10-12             | 4.7                       | 4.71                  | 4.66                        | 4.91                   | 4.88                | 4.83    | 4.71             |                                | f                                           | 1                                            | 0                                           | 1                 | 0    | 0.43 |      |

## Data munging

The formatting in the .csv was usable for the get-go, there was however an error in the pricing where the price column displayed a price in dollars which was originally listed in SEK (Swedish Krona), leading to a discrepancy in price (due to SEK/USD exchange rate > 10x). This issue was resolved by converting the price values to USD using python and the pandas module using the following [code](/munge.py):

```python
df["price"] = df["price"].str.replace(",", "")
df["price"] = df["price"].str.replace("$", "").astype(float)


sek_to_usd = 0.096 #Currency conversion rate based on USD = 10.42 SEK

df["price"] = '$' + ((df["price"] * sek_to_usd).round(2)).astype(str)

df.to_csv('listings_clean.csv')
```


Moreover, in order to properly display the raw data, I limited the columns: *amenities, host_about, neighborhood_overview,* and *description* to 30 characters, this code can also be found, along with the above code [here](/munge.py).

```python
df_raw = df.copy()

end = ' ...'

df_raw['amenities'] = (df_raw['amenities'].str[:30] + end)
df_raw['host_about'] = (df_raw['host_about'].str[:30] + end)
df_raw['neighborhood_overview'] = df_raw['neighborhood_overview'].str[:30] + end
df_raw['description'] = df['description'].str[:30] + end
```

Choosing two superhosts by their `host_id`, and showing all of the listings offered by both of the two hosts. Projecting the `name`, `price`, `neighbourhood`, `host_name`, and `host_is_superhost` for each result.

Code:
```js
db.listings.find({
    host_id: {
        $in:[784312,914316]},
},
    {"_id":0,
    "name":1,
    "price":1,
    "neighbourhood":1,
    "host_name":1,
    "host_is_superhost":1,
    }
)
```
Output:
```js
[
  {
    name: 'Double room in central Stockholm with Wi-Fi',
    host_name: 'Li',
    host_is_superhost: 't',
    neighbourhood: '',
    price: '$82.94'
  },
  {
    name: 'Single room in central Stockholm with Wi-Fi',
    host_name: 'Li',
    host_is_superhost: 't',
    neighbourhood: '',
    price: '$78.14'
  },
  {
    name: 'Bunk bed close by Alvsjo Exhibition',
    host_name: 'Ea',
    host_is_superhost: 't',
    neighbourhood: '',
    price: '$33.6'
  }
```

Findings all of the places that have more than 2 `beds` in a neighborhood of your choice, ordered by `review_scores_rating` descending, presenting the `name`, `beds`, `review_scores_rating`, and `price` columns.

The ``` review_scores_rating: { $ne: null, $ne: "" }``` was added so that the listings without rating wasn't shown up at the top of our output, without this our first 3 output would've consisted of listings with empty ratings.

Code:

```js
db.listings.find(
    {
        neighbourhood_cleansed: "Södermalms",
        beds: {
            $gt: 2
        },
        review_scores_rating: {
            $ne: null,
            $ne: ""
        }
    },
    {
        "_id": 0,
        "name": 1,
        "beds": 1,
        "review_scores_rating": 1,
        "price": 1
    }
).sort({
    "review_scores_rating": -1
})
```

Output:
```js
[
  {
    name: 'Central & calm city apartment',
    beds: 4,
    price: '$170.78',
    review_scores_rating: 5
  },
  {
    name: 'Quiet oasis in trendy neighborhood by the water!',
    beds: 4,
    price: '$250.56',
    review_scores_rating: 5
  },
  {
    name: 'New york feeling in Södermalm',
    beds: 5,
    price: '$172.8',
    review_scores_rating: 5
  },

```

Showing the number of listings per host:

```js
db.listings.aggregate([
  {"$group": {"_id": "$host_id", "count": {"$sum": 1}}}
])
```

Output:
```js
[
  { _id: 492963558, count: 1 },
  { _id: 469528727, count: 1 },
  { _id: 96452720, count: 1 },
```

Finding the average `review_scores_rating` per neighborhood, and only show the ones above a `95`, sorted in descending order of rating.

```js
db.listings.aggregate([
  {
    "$group": {
      "_id": "$neighbourhood_cleansed",
      "average_rating": { "$avg": "$review_scores_rating" }
    }
  },
  {
    $match: {
      average_rating: { $gte: 4.75 }
    }
  }
]).sort({
    "average_rating": -1
})
```

```js
[
  { _id: 'Spånga-Tensta', average_rating: 4.78264705882353 },
  { _id: 'Södermalms', average_rating: 4.774491725768321 },
  { _id: 'Norrmalms', average_rating: 4.771027397260275 },
  { _id: 'Hägersten-Liljeholmens', average_rating: 4.7684375 },
  { _id: 'Hässelby-Vällingby', average_rating: 4.766436781609196 },
  { _id: 'Enskede-Årsta-Vantörs', average_rating: 4.761466666666666 },
  { _id: 'Bromma', average_rating: 4.753356164383562 }
]
```

## Using PyMongo to recreat earlier MongoDB query

I've been able to recreate the fifth query using pymongo, the full code can be found [here](/python_mongo.py),

The output of the Pymongo code follows:

```python
{'name': 'Central & calm city apartment', 'beds': 4.0, 'price': '$170.78', 'review_scores_rating': 5.0}
{'name': 'Quiet oasis in trendy neighborhood by the water!', 'beds': 4.0, 'price': '$250.56', 'review_scores_rating': 5.0}
{'name': 'New york feeling in Södermalm', 'beds': 5.0, 'price': '$172.8', 'review_scores_rating': 5.0}
```