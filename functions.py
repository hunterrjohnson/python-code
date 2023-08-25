# Function to check missingness in data frame and return summary data frame

def check_missing(dat):
    
    # Function to count missing and get proportion missing
    def null_check(var):
        missing_count = var.isin(['','NULL']).sum() + var.isna().sum()
        total_rows = len(var)
        missing_proportion = missing_count / total_rows
        
        result_dat = pd.DataFrame({
            'VARIABLE': [var.name],
            'N_MISSING': [missing_count],
            'PROP_MISSING': [missing_proportion]
        })
        return result_dat

    # Summarize results in data frame
    result_dats = [null_check(dat[column]) for column in dat.columns] # Apply null_check to each column
    final_result = pd.concat(result_dats, ignore_index = True) # Concatenate results
    return final_result
