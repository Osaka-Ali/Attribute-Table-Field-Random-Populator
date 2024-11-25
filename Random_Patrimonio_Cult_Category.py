import pandas as pd
import numpy as np

# Create a DataFrame (table) with 200 rows and 1 column
df = pd.DataFrame({'Numbers': np.zeros(197)})

# Define your four variables
var1, var2, var3, var4 = 1, 2, 3, 4

# Assign random numbers to the DataFrame
df['Numbers'] = np.random.choice([var1, var2, var3, var4], size=197)

# Save the DataFrame to a CSV file
df.to_csv('random_table.csv', index=False)