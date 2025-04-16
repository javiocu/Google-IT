def sequence(low, high):
    # high  --> low separo por comas
    final = ""
    for i in range(high, low):
      if i == high:
        valor = final + "," + i 
      else:
        valor = i
    print(valor)

sequence(1, 3)
# Should print the sequence 3, 2, 1 two times, as shown above.