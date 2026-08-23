import numpy as np
import csv
import argparse

def iq_to_csv(input_file, output_file, dtype="float32"):
    # Read raw IQ samples
    data = np.fromfile(input_file, dtype=np.dtype(dtype))

    if len(data) % 2 != 0:
        print("Warning: odd number of samples. Dropping the last value.")
        data = data[:-1]

    # Split interleaved data
    i_samples = data[0::2]
    q_samples = data[1::2]

    with open(output_file, "w", newline="") as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(["I", "Q"])

        for i, q in zip(i_samples, q_samples):
            writer.writerow([i, q])

    print(f"Converted {len(i_samples)} IQ samples.")
    print(f"Saved to: {output_file}")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Convert raw IQ data to CSV")

    parser.add_argument("input", help="Input IQ file")
    parser.add_argument("output", help="Output CSV file")

    parser.add_argument(
        "--dtype",
        default="float32",
        choices=[
            "int8",
            "uint8",
            "int16",
            "uint16",
            "int32",
            "float32",
            "float64"
        ],
        help="Data type of each I/Q component"
    )

    args = parser.parse_args()

    iq_to_csv(args.input, args.output, args.dtype)