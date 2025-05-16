#!/usr/bin/env python3

#Import libraries          "@abc.edu"          "@xyz.edu"
import re
import csv


def contains_domain(address, domain="abc.edu"):
    """Returns True if the email address contains the given domain,
    in the domain position, false if not."""
    patron = r"[\w\.-]@{}$".format(domain)
    if re.search(patron, address):
        return True
    return False

def replace_domain(address, old_domain="abc.edu", new_domain="xyz.edu"):
    """Replaces the old domain with the new domain in
    the received address."""
    if contains_domain(address, old_domain):
        patron_viejo = r"{}$".format(re.escape(old_domain))
        address =  re.sub(patron_viejo,new_domain, address)
    return address

def main():
    """Processes the list of emails, replacing any instances of the
    old domain with the new domain."""
    old_domain_path = "C:/Users/Javi/Downloads/user_emails.csv"     #"/home/student/data/user_emails.csv"  
    new_domain_path = "C:/Users/Javi/Downloads/user_emails_updated.csv" # "/home/student/data/updated_user_emails.csv"  
    with open(old_domain_path, "r") as old_file:
        old_leido = list(csv.reader(old_file))
        nuevalist = []
        for i in old_leido:
            nombre, correo = i
            correo = replace_domain(correo)
            nuevalist.append([nombre, correo])
        with open(new_domain_path, "w", newline="") as nuevo:
            writerrr = csv.writer(nuevo)
            for row in nuevalist:
                writerrr.writerow(row)

            
main()

