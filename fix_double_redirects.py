import csv

def fix_double_redirects(in_path, out_path):
    # Read the redirects into a list
    with open(in_path, 'r') as file:
        reader = csv.reader(file)
        redirects = [
            [row[0], row[1].replace("https://", "")] for row in reader if len(row) >= 2
        ]  # Skip empty or malformed rows and remove "https://"

    # Create a mapping of source to destination
    redirect_map = {row[0]: row[1] for row in redirects}

    # Detect and fix double redirects
    updated_redirects = []
    for row in redirects:
        source, destination = row[0], row[1]
        if destination in redirect_map:
            # If destination is also a source, update to point to the final target
            final_destination = redirect_map[destination]
            print(f"Double redirect found: {source} → {destination} → {final_destination}. Correcting to {source} → {final_destination}.")
            row[1] = final_destination
        updated_redirects.append(row)

    # Write the updated redirects back to the file
    with open(out_path, 'w', newline='') as file:  # Use out_path instead of file_path
        writer = csv.writer(file)
        writer.writerows(updated_redirects)

if __name__ == "__main__":
    in_path = "/Users/ppiegaze/repos/unionai/docs-builder/rd.csv"
    out_path = "/Users/ppiegaze/repos/unionai/docs-builder/new-redirects-ai-union-docs.csv"
    fix_double_redirects(in_path, out_path)
    print("Double redirects fixed and file updated.")
