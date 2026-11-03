import csv
import os

activities = {
    "1": "WALKING",
    "2": "WALKING_UPSTAIRS",
    "3": "WALKING_DOWNSTAIRS",
    "4": "SITTING",
    "5": "STANDING",
    "6": "LAYING"
}

def prepare_dataset(folder, output_file, prefix):

    with open(folder + "/X_" + prefix + ".txt") as xfile, \
         open(folder + "/y_" + prefix + ".txt") as yfile, \
         open(folder + "/subject_" + prefix + ".txt") as sfile:

        features = ["feature_" + str(i) for i in range(1, 562)]

        with open(output_file, "w", newline="") as outfile:

            writer = csv.writer(outfile)

            writer.writerow(features + ["subject", "activity"])

            for x, y, s in zip(xfile, yfile, sfile):

                values = x.split()
                label = activities[y.strip()]
                subject = s.strip()

                writer.writerow(values + [subject, label])

    print(output_file + " created successfully!")


# Prepare training dataset
prepare_dataset("train", "HAR_train_complete.csv", "train")

# Prepare testing dataset
prepare_dataset("test", "HAR_test_complete.csv", "test")

print("Both datasets prepared successfully!")