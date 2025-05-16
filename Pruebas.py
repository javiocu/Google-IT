#!/usr/bin/env python3

#Import libraries
import csv
import re

def contains_domain(address, domain = "abc.edu"):
  """Returns True if the email address contains the given domain,
    in the domain position, false if not."""
  patron = rf"[\w\.-]+@{re.escape(domain)}$"
  salida = re.fullmatch(patron, address)
  if salida:
        return True
  return False

def replace_domain(address, old_domain = "abc.edu", new_domain = "xyz.edu"):
  """Replaces the old domain with the new domain in
  the received address."""
  patron = rf"@{re.escape(old_domain)}"
  address = re.sub(patron, rf"@{re.escape(new_domain)}$",address)
  return address

def main():
  """Processes the list of emails, replacing any instances of the
    old domain with the new domain."""
  csv_location_path = "C:/Users/Javi/Downloads/user_emails.csv"
  csv_nuevo_location = "C:/Users/Javi/Downloads/user_emails_updated.csv"
  with open(csv_location_path,"r") as file:
    correos_antigua_lista = list(csv.reader(file))
    lista_actualizada = []
    for row in correos_antigua_lista:
      direccion_nueva = row[1]
      if contains_domain(row[1]):
        direccion_nueva = replace_domain(row[1])
      lista_actualizada.append([row[0],direccion_nueva])
    with open(csv_nuevo_location, "w", newline="") as file_nuevo:
      writer = csv.writer(file_nuevo)
      writer.writerows(lista_actualizada)


            
main()