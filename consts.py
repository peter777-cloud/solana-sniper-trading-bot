from lino_secrets import SUPABASE_URL, SUPABASE_KEY, WS_TRENDING, WS_GAINERS, WS_NEWEST
MAX_TRIES = 5
trending_pairs_string = "Trending Pairs"
trending_pairs_string_slugged = trending_pairs_string.replace(" ", "_").lower()
top_gaining_pairs_string = "Top Gaining Pairs"
top_gaining_pairs_string_slugged = top_gaining_pairs_string.replace(" ", "_").lower()
newest_pairs_string = "Newest Pairs"
newest_pairs_string_slugged = newest_pairs_string.replace(" ", "_").lower()