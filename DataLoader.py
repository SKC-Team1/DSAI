class DataLoader:
    # load the dataset
    @staticmethod
    def load_dataset():
        return "123567890"

# import os
# import re
# import pandas as pd
# from dotenv import load_dotenv

# def convert_str_lists(df):
#     # Define the regex pattern required to get the tags and keywords from the strings
#     str_list_regex_pattern = r"'(.*?)'"
#     # Make the tags accessible as lists of strings
#     df["Tags"] = df["Tags"].apply(lambda str_list: re.findall(str_list_regex_pattern, str_list))
#     # Make the keywords accessible as lists of strings
#     df["Keywords"] = df["Keywords"].apply(lambda str_list: re.findall(str_list_regex_pattern, str_list))
#     # Make the types of the articles accessible as lists of strings
#     df["Type"] = df["Type"].apply(lambda str_list: re.findall(str_list_regex_pattern, str_list))

# def abstract_load_df(filename):
#     # Load the environment variables from the .env file
#     load_dotenv()
#     # Get the dataset path from the environment variables
#     dataset_path = os.environ.get("DATASET_PATH")
#     # Load the dataset into the notebook
#     df = pd.read_csv(f"{dataset_path}/{filename}", index_col=0, parse_dates=[1])
#     # Parse the lists of strings from the dataset 
#     convert_str_lists(df)
#     # Return the dataframe
#     return df

# def load_onehotencoded():
#     return abstract_load_df("article_info_V4.csv")

# def load():
#     return abstract_load_df("article_info_V3.csv")