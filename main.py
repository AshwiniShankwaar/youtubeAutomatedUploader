import getExcelData as data
import uploadVideo
import os

parent_dir = os.getcwd()
def main():
    df = data.getExceldata(parent_dir)
    # print(df.head())
    for index, row in df.iterrows():
        # print(f"Row {index + 1}:")
        filename = parent_dir+"PATH_TO_YOUR_FILE"
        # print(filename)
        uploadVideo.uploadVideo(
            filename,
            row["Title"],
            row["Description"],
            "22",
            row['Keywords'],
            "public"
        )

if __name__ == "__main__":
    main()