import polars as pl

def process_csv_polars(raw_file_path, aggregated_file_path):

    input_df = pl.read_csv(raw_file_path)
    result_df = input_df.groupby(["Song", "Date"]).agg([pl.col("Number of Plays").alias("Total Number of Plays for Date").sum()])
    result_df.write_csv(aggregated_file_path)
