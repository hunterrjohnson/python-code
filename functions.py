# Function to check missingness in data frame and return summary data frame
def check_missing(dat):
    
    # Function to count missing and get proportion missing
    def null_check(var):
        total_rows = len(var)
        missing_count = var.isna().sum() + var.isin(['','NULL','Null','null','NA','na']).sum()
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

# Function to check completeness in data frame and return summary data frame
def check_complete(dat):
    
    # Function to check complete and get proportion complete
    def complete_check(var):
        total_rows = len(var)
        complete_count = total_rows - (var.isna().sum() + var.isin(['','NULL','Null','null','NA','na']).sum())
        complete_proportion = complete_count / total_rows
        
        result_dat = pd.DataFrame({
            'VARIABLE': [var.name],
            'N_COMPLETE': [complete_count],
            'PROP_COMPLETE': [complete_proportion]
        })
        
        return result_dat
    
    # Summarize results in data frame
    result_dats = [complete_check(dat[column]) for column in dat.columns] # Apply complete_check to each column
    final_result = pd.concat(result_dats, ignore_index = True) # Concatenate results
    return final_result

# Function to get first non-missing element of each column
def get_example(dat):
    dat_ex = dat.apply(lambda col: col[col.first_valid_index()]).to_frame().reset_index()
    dat_ex.columns = ['VARIABLE','VALUE']
    return dat_ex
