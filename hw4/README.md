Output of parser
Variables are: ['B', 'E', 'A', 'J', 'M']
Domains are: {'B': ['true', 'false'], 'E': ['true', 'false'], 'A': ['true', 'false'], 'J': ['true', 'false'], 'M': ['true', 'false']}
Parents are: {'B': None, 'E': None, 'A': ['B', 'E'], 'J': ['A'], 'M': ['A']}
Tables are: {'B': [0.001, 0.999], 'E': [0.002, 0.998], 'A': [0.95, 0.05, 0.94, 0.06, 0.29, 0.71, 0.001, 0.999], 'J': [0.9, 0.1, 0.05, 0.95], 'M': [0.7, 0.3, 0.01, 0.99]}

`parsed_tables = {B: pd.Dataframe object, 'E': pd.Dataframe object, 'A': pd.Dataframe object, 'J': pd.Dataframe object, 'M': pd.Dataframe object}`

### Sample table of a variable with no parents like B

|B |withSelf|
| -------- | ------ |
| 'true'   | 0.001  |
| 'false'  | 0.999 |


### Sample table of a variable with parents like J
|A| J| ~J|
| -------- | ------ | ------ |
| 'true'   | 0.9  | 0.05|
| 'false'  | 0.1 | 0.95|


