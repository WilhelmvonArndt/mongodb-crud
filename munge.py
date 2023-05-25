import pandas as pd

df = pd.read_csv("data/listings.csv")

df.info()
df["price"] = df["price"].str.replace(",", "")
df["price"] = df["price"].str.replace("$", "").astype(float)


sek_to_usd = 0.096 #Currency conversion rate based on USD = 10.42 SEK

df["price"] = '$' + ((df["price"] * sek_to_usd).round(2)).astype(str)

df.to_csv('listings_clean.csv')

#Code which makes raw data more presentable

df_raw = df.copy()

end = ' ...'

df_raw['amenities'] = (df_raw['amenities'].str[:30] + end)
df_raw['host_about'] = (df_raw['host_about'].str[:30] + end)
df_raw['neighborhood_overview'] = df_raw['neighborhood_overview'].str[:30] + end
df_raw['description'] = df['description'].str[:30] + end

df_raw.to_csv('raw_cleaned_data.csv')

print(df_raw['amenities'][0])