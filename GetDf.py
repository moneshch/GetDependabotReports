import pandas as pd
def getDf(data):
    rows = []
    for iData in data:
        row = {}
        # Extract key-value pairs for each item
        for key, value in iData.items():
            if isinstance(value, dict):
                for key1, value1 in value.items():
                    if isinstance(value1, dict):
                        for key2, value2 in value1.items():
                            row[f"{key}_{key1}_{key2}"] = value2
                    elif isinstance(value1, list):
                        for i in value1:
                            if isinstance(i, dict):
                                for key3, value3 in i.items():
                                    row[f"{key}_{key1}_{key3}"] = value3
                            elif isinstance(i, dict):
                                for key4, value4 in i.items():
                                    row[f"{key}_{key1}_{key4}"] = value4
                    else:
                        row[f"{key}_{key1}"] = value1
            else:
                row[key] = value
        rows.append(row)
    
    # Create DataFrame
    df = pd.DataFrame(rows)
    return df
