# Perfume Dataset

The dataset contains approximately 1,000 perfumes from multiple brands. Each row represents a fragrance and describes its concentration, category, target audience, and longevity.

## Dataset Properties

| Column | Type | Description |

| brand | string | Perfume brand
| perfume | string | Fragrance name
| type | string | Concentration
| category | string | Scent family or descriptive category
| target_audience | string | Intended audience
| longevity | string | Expected longevity

The `id` column contains a unique numeric identifier for each entry. It will be used as Recombee's `itemId` and is not registered as a property.

The `recombee_properties.py` script registers the six properties above as strings using the official Recombee Python SDK.

## Source

[Dataset source](https://www.kaggle.com/datasets/ayushghawana/perfume-dataset)
