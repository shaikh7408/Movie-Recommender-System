# Movie-Recommender-System
![Screenshot (350)](https://github.com/user-attachments/assets/db2ff355-8a6f-401a-a250-76f035c4aeb3)
![image](https://github.com/user-attachments/assets/fd650887-6d6e-44bf-91f4-b9e1e5bcbcf4)
![Screenshot (349)](https://github.com/user-attachments/assets/9795f261-e5c7-4452-a658-6bb63c48f2d9)

# Kaggle Dataset: [TMDB 5000 Movie Dataset]

## Description
This dataset contains Movies detail . It was originally sourced from Kaggle .

## Files
- `tmdb_5000_moives.csv`: The main dataset file containing movie details [4809]rows and [23] columns.
- `tmdb_5000_credit.csv`: This dataset file describing and contain the data[4809]rows and [4] columns. movies Acotrs,Directors and its crew who's working BTS 


## Usage
To load the dataset in Python, use the following code:

```python
import pandas as pd

# Load the main dataset
movies_detail=pd.read_csv('tmdb_5000_movies.csv')
movies_credit=pd.read_csv('tmdb_5000_credits.csv')


# Display the first few rows
print(movies_detail.head(3))
