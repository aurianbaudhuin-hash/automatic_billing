import csv


def fetch_last_invoice_number():
    """gets the last invoice number from company_data.csv and updates it"""
    rows = []
    output = 0
    with open('input/company_data.csv', newline='') as f:
        reader = csv.reader(f)
        for row in reader:
            if row[0] == 'last invoice number':  
                output = int(row[1])
                row[1] = str(int(row[1])+1)
            rows.append(row)

    # Réécrire le fichier
    with open('input/company_data.csv', 'w', newline='') as f:
        writer = csv.writer(f)
        writer.writerows(rows)
    return output

def collect_invoice_data():
    data = {}
    company_data = {}

    with open("input/company_data.csv", newline="", encoding="utf-8") as g:
        reader = csv.reader(g)
        for row in reader:
            key = row[0].strip()
            value = row[1].strip()
            company_data[key] = value


    with open("input/template file.csv", newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, delimiter=";")
        
        for row in reader:
            client = row["Client name"]
            
            # Cleaning data
            hours = float(row["Hours"])
            rate = float(row["Rate"])
            
            total = float(row["Total"].replace(",", "."))
            
            taxes = row["Taxes"]
            if taxes:
                taxes = float(taxes.replace("%", ""))
            else:
                taxes = 0
            
            entry = {
                "date": row["Date"],
                "description": row["Description"],
                "hours": hours,
                "rate": rate,
                "taxes": taxes,
                "total": total
            }
            
            # Add to dictionary
            if client not in data:
                invoice_number = fetch_last_invoice_number()
                data[client] = [invoice_number, row["Email"]]
            
            data[client].append(entry)




